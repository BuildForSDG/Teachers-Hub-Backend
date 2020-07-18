import psycopg2
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..validators.course_validator import ValidateCourse
from .controller import CourseController
from ..users.controller import UserController

course = Blueprint('course', __name__)
course_controller = CourseController()
user_controller = UserController()


@course.route('/api/v1/courses', methods=['POST'])
@jwt_required
def add_new_course():
    """Registers a Course."""
    data = request.get_json()
    try:
        if data:
            if not user_controller.check_admin_user():
                return jsonify({"message": "only Admins allowed"}), 401
            validate_course = ValidateCourse(data)
            if validate_course.validate_course_category() and \
                validate_course.validate_course_duration():
                if course_controller.check_instructor_exists(data['course_instructor']):
                    if not course_controller.query_course_on_category(data):
                        course_controller.create_course(data)
                        return jsonify({"message": "course added successfully"}), 200
                    else:
                        return jsonify({"message": "course already exists in category"}), 400
                else:
                    return jsonify({"message": "user does not exist or not registered as instructor"}), 400
            elif not validate_course.validate_course_category():
                return jsonify({"message": "enter valid course category"}), 400
            elif not validate_course.validate_course_duration():
                return jsonify({"message": "enter valid course duration"}), 400
        else:
            return jsonify({"message": "course details not provided"}), 400
    except Exception as e: # work on python 3.x
        return jsonify({"message":  repr(e) + " is missing"})
@course.route('/api/v1/courses/<course_id>', methods=['DELETE'])
@jwt_required
def delete_course(course_id):
    """
    Function enables admin to delete a course from the database.

    """
    try:
        if not user_controller.check_admin_user():
            return jsonify({"message": "only Admins allowed"}), 401
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
                'course_category': course[1],
                'course_title': course[2],
                'course_description': course[3],
                'course_duration': course[4],
                'total_enrolled': course[5],
                'date_added': course[6],
                'course_instructor': course[7]
            },
            'message': 'course fetched!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'The course id should be an integer!'
        }), 400


@course.route('/api/v1/courses/<course_id>', methods=['PUT'])
@jwt_required
def update_course(course_id):
    """
    Function enables user to modify a course from the database.
    """
    data = request.get_json()

    if data:
        if not user_controller.check_admin_user():
            return jsonify({"message": "only Admins allowed"}), 401
        validate_course = ValidateCourse(data)
        try:
            course_id = int(course_id)
            if not course_controller.query_course(course_id):
                return jsonify({
                    'message': 'Course does not exist in database'
                }), 400
            elif validate_course.validate_course_category() and \
               validate_course.validate_course_duration():
                if course_controller.check_instructor_exists(data['course_instructor']):
                    course_controller.update_course(data, course_id)
                    return jsonify({"message": "course updated successfully"}), 200
                else:
                    return jsonify({"message": "user does not exist or not registered as instructor"}),400
            elif not validate_course.validate_course_category():
                return jsonify({"message": "enter valid course category"}), 400
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

@course.route('/api/v1/courses/enrolled', methods=['GET'])
@jwt_required
def get_enrolled_course():
    """
    Function enables user to fetch courses enrolled for
    """
    enrolledCourses = course_controller.get_enrolled_courses()
    return jsonify({
        'enrolled_courses': enrolledCourses
    }), 200

@course.route('/api/v1/courses/enrolled/<course_id>', methods=['GET'])
@jwt_required
def get_enrolled_course_state(course_id):
    """
    Function enables user to get state of enrolled course
    """
    enrolledCourseState = course_controller.check_if_already_enrolled(course_id)

    if not enrolledCourseState:
        return jsonify({
            'message': "Not Registered"
        })
    else:
        return jsonify({
            'message': 'Registered'
        })