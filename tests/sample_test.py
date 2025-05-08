from pytest import fail

from tests.helpers import json_of_response


def test_create_student(client, app):
    student_params = dict(
        first_name="Scarlett",
        last_name="Evans",
        date_of_birth="2010-05-01",
        grade=8,
        phone="+11111111111",
        email="scarlet@email.com"
    )

    response = client.post("/students", json=student_params)
    assert response.status_code == 201
    assert json_of_response(response) == dict(id=1, **student_params)

def test_invalid_create_student(client, app):
    student_params = dict(
        first_name="Scarlett",
        last_name="Evans",
        date_of_birth="2010-05-01",
        grade=8,
        phone="+11111111111"
    )

    response = client.post("/students", json=student_params)
    assert response.status_code == 400
    assert "email" in json_of_response(response)


def test_all_students_returns_all_students_json_ordered_by_id(client, app):
    students_params = [
        dict(
            first_name="Scarlett",
            last_name="Evans",
            date_of_birth="2010-05-01",
            grade=8,
            phone="+11111111111",
            email="scarlet@email.com"
        ),
        dict(
            first_name="Lily",
            last_name="Davies",
            date_of_birth="2010-03-15",
            grade=8,
            phone="+11222222222",
            email="lily@email.com"
        )
    ]

    for student_params in students_params:
        response = client.post("/students", json=student_params)

        if response.status_code != 201:
            fail('POST /students is not implemented')

    response = client.get("/students")

    expected = [dict(id=index, **student_params) for index, student_params in enumerate(students_params, start=1)]

    assert response.status_code == 200
    assert json_of_response(response) == expected
