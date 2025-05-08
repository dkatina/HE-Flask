from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    grade = db.Column(db.Integer)
    phone = db.Column(db.String)
    email = db.Column(db.String)

    def to_dict(self):
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            date_of_birth=self.date_of_birth.isoformat(),
            grade=self.grade,
            phone=self.phone,
            email=self.email
        )
