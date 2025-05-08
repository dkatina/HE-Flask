from datetime import datetime
from flask import Blueprint, jsonify, abort, request

from sqlalchemy import select
from app.models import Student, db
from app import ma

students_blueprint = Blueprint("students", __name__)


class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student

student_schema = StudentSchema()
student_schema = StudentSchema(many=True)



@students_blueprint.route("/students", methods=["POST"])
def __create_student():
    '''
    Complete the following code to create a new student and add the student to 
    the database.following data is passed into the request. 
    {
        'first_name':
        'last_name':
        'date_of_birth':
        'grade':
        'email':

    }
    Reminder to validate incoming data.
    return a json response of newly added student with status code 201.
    '''
    


@students_blueprint.route("/students", methods=['GET'])
def __students():
    '''
    Complete the following code to get list of students.
    return json response of list of students.
    '''
   





