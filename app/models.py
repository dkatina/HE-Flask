from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)



class Student(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]  = mapped_column(db.String(255))
    last_name: Mapped[str]  = mapped_column(db.String(255))
    date_of_birth: Mapped[date]  = mapped_column(db.Date)
    grade: Mapped[int]  = mapped_column(db.Integer)
    phone: Mapped[str]  = mapped_column(db.String(255))
    email: Mapped[str]  = mapped_column(db.String(255))

  
