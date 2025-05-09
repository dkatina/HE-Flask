# Python Flask: Student API

## Project Specifications

**Read-Only Files**
- tests/*

**Environment**  

- Python version: 3.7
- Flask version: 1.1.2
- Flask-SQLAlchemy: 2.4.4
- Default Port: 8000

**Commands**
- install: 
```bash
python3 -m venv venv; source venv/bin/activate; pip3 install -r requirements.txt; 
```
- run: 
```bash
flask init-db; flask run -p 8000
```
- test: 
```bash
pytest
```
    
## Question description

In this task, you have to implement a simple REST API to manage a collection of students in the school system.

Each student record has the following set of fields:

- `id`: The unique ID of the student. (Integer)
- `first_name`: The name of the student. (String)
- `last_name`: The last name of the student. (String)
- `date_of_birth`: The date of birth of the student. (Date)
- `grade`: The grade of the student. (Integer)
- `phone`: The phone number of the student. (String)
- `email`: The email of the student. (String)
    
### Example of a student data JSON object:
```
{
    "id": 1,
    "first_name": "Scarlett",
    "last_name": "Evans",
    "date_of_birth": "2010-05-01",
    "grade": 8,
    "phone": "+11111111111",
    "email": "scarlet@email.com"
}
```

## Requirements:

You are provided with the implementation of the Student model. The REST service must expose the `/students` endpoint, which allows for managing the collection of student records in the following way:

`POST /students`:

- creates a new student record
- expects a JSON student object without an id property as a body payload. You can assume that the given object is always valid.
- adds the given student object to the collection of student records and assigns a unique integer id to it. The first created student record must have id 1, the second one 2, and so on.
- the response code is 201, and the response body is the created student record

`GET /students`:

- returns a collection of all student records
- the response code is 200, and the response body is an array of all student records ordered by their ids in increasing order

`GET /students/<id>`:

- returns a student record with the given id
- if the matching student exists, the response code is 200 and the response body is the matching student record
- if there is no student with the given id in the collection, the response code is 404

`PATCH /students/<id>`:

- updates a student record with the given id
- expects a JSON student object without an id property as a body payload. You can assume that the given object is always valid.
- the response code is 200, and the response body is the updated student record
- if there is no student with the given id in the collection, the response code is 404

`DELETE` request to `/students/<id>`:

- the response code is 405 because the API does not allow deleting student records for any id value
