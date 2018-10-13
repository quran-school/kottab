#!/usr/bin/env python

from entity import Session, engine, Base
from model import User, Student

Base.metadata.create_all(engine)
session = Session()

def get_students():
    students = session.query(Student).all()
    return students

def add_student(email, first_name, last_name, mobile, date_of_birth, gender, nationality):
    student = Student(email, first_name, last_name, mobile, date_of_birth, gender, nationality)
    session.add(student)
    session.commit()

def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    student.delete()
    session.commit()
