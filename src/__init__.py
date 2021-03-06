from flask import Flask, jsonify
from src.users.view import user
from src.courses.view import course
from src.courseModules.view import module
from src.partners.view import organization
from src.communityQuestions.view import question
from decouple import config
from flask_cors import CORS
from src.articles.view import article
from src.comments.view import comment
from flask_jwt_extended import JWTManager


app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(user)
app.register_blueprint(course)
app.register_blueprint(module)
app.register_blueprint(article)
app.register_blueprint(comment)
app.register_blueprint(organization)
app.register_blueprint(question)
app.config['JWT_SECRET_KEY'] = config("SECRET_KEY")
jwt = JWTManager(app)



@app.route('/')
def index():
    return jsonify({"message": "welcome to teachers hub"})
