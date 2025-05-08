from datetime import datetime
from flask import Blueprint, jsonify, abort, request

from app import db
from app.models import Student

students_blueprint = Blueprint("students", __name__, url_prefix="/students")

@students_blueprint.route("", methods=["POST"])
def __create_student():
    '''
    Complete the following code to create a new student  and the student to 
    the database.following data is passed into the request.
    {
        'first_name':
        'last_name':
        'date_of_birth':
        'grade':
        'email':

    }
    return a json response of newly added student with status code 201.
    '''
    


@students_blueprint.route("")
def __students():
    '''
    Complete the following code to get list of students.
    return json response of list of students.
    '''
   





