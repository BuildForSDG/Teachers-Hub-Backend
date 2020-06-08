import psycopg2
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity

from ..validators.course_validator import ValidateCourse
from .controller import CourseController

from functools import wraps


course = Blueprint('course', __name__)
course_controller = CourseController()

# This custom decorator that verifies the JWT is present in
# the request, as well as insure that the user has a role of
# `Admin` in the access token


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        role = str(current_user['role'])[1:-1].replace('\'', '')
        #print(role)
        if role == 'Admin':
            return f(*args, **kwargs)
        else:
            return jsonify(msg='Only Course Administrators can perform this action!'), 403

    return wrapper


@course.route('/api/v1/courses', methods=['POST'])
@admin_required
def add_new_course():
    """Registers a Course."""
    data = request.get_json()

    if data:
        validate_course = ValidateCourse(data)
        try:
            if validate_course.validate_course_name() and \
               validate_course.validate_course_duration():
                course_controller.create_course(data)
                return jsonify({"message": "course added successfully"}), 200
            elif not validate_course.validate_course_name():
                return jsonify({"message": "enter valid course name"}), 400
            elif not validate_course.validate_course_duration():
                return jsonify({"message": "enter valid course duration"}), 400
        except psycopg2.Error:
            return jsonify({"message": "course name already exists"}), 400
    else:
        return jsonify({"message": "course details not provided"}), 400


@course.route('/api/v1/courses/<course_id>', methods=['DELETE'])
@admin_required
def delete_course(course_id):
    """
    Function enables admin to delete a course from the database.

    """
    try:
        course_id = int(course_id)
        if not course_controller.query_course(course_id):
            return jsonify({
                'message': 'Course does not exist in database'
            }), 400

        course_controller.delete_course(course_id)
        return jsonify({
            'message': 'Course deleted!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The course id should be an integer!'
        }), 400


@course.route('/api/v1/courses/<course_id>', methods=['GET'])
def view_course(course_id):
    """
    Function enables user to view a course from the database.
    """
    try:
        course_id = int(course_id)
        if not course_controller.query_course(course_id):
            return jsonify({
                'message': 'Course does not exist in database'
            }), 400
        course = course_controller.query_course(course_id)
        return jsonify({
            'course': {
                'course_id': course[0],
                'course_name': course[1],
                'course_title': course[2],
                'course_description': course[3],
                'course_duration': course[4]
            },
            'message': 'course fetched!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The course id should be an integer!'
        }), 400


@course.route('/api/v1/courses/<course_id>', methods=['PUT'])
@admin_required
def update_course(course_id):
    """
    Function enables user to modify a course from the database.
    """
    data = request.get_json()

    if data:
        validate_course = ValidateCourse(data)
        try:
            course_id = int(course_id)
            if not course_controller.query_course(course_id):
                return jsonify({
                    'message': 'Course does not exist in database'
                }), 400
            elif validate_course.validate_course_name() and \
                    validate_course.validate_course_duration():
                course_controller.update_course(data, course_id)
                return jsonify({"message": "course updated successfully"}), 200
            elif not validate_course.validate_course_name():
                return jsonify({"message": "enter valid course name"}), 400
            elif not validate_course.validate_course_duration():
                return jsonify({"message": "enter valid course duration"}), 400
        except ValueError:
            return jsonify({"message": "course id should be an integer"}), 400
        except Exception:
            return jsonify({"message": "course exists already"}), 400
    else:
        return jsonify({"message": "course details not provided"}), 400


@course.route('/api/v1/courses', methods=['GET'])
def view_all_courses():
    """
    Function enables user to view all the available courses from the database.
    """
    if not course_controller.query_all_courses():
        return jsonify({
            'message': 'No available courses in the database'
        }), 400
    courses = course_controller.query_all_courses()
    return jsonify({
        'courses': courses,
        'message': 'courses fetched!'
    }), 200


@course.route('/api/v1/courses/<course_id>/enroll', methods=['POST'])
@jwt_required
def enroll_for_course(course_id):
    """
    Function enables user to enroll for a specific course.
    """
    if not course_controller.query_course(course_id):
        return jsonify({
            'message': 'course doesnot exist in database'
        }), 400

    elif course_controller.check_if_already_enrolled(course_id):
        return jsonify({
            'message': 'already enrolled for this course'
        }), 400
    else:
        course_controller.enroll_course(course_id)
        return jsonify({
            'message': 'successfully enrolled'
        }), 200
