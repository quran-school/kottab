from sqlalchemy import Column, String, Boolean, Integer, Date, ForeignKey
from entity import Entity, Base
from sqlalchemy.orm import relationship

class User(Entity, Base):
    __tablename__ = 'users'

    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    mobile = Column(String)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'user',
        'polymorphic_on':type
    }

    def __init__(self, email, first_name, last_name, mobile):
        Entity.__init__(self)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile

class Student(User):
    __tablename__ = 'students'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    date_of_birth = Column(Date)
    gender = Column(String)
    nationality = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':'student',
    }

    def __init__(self, email, first_name, last_name, mobile, date_of_birth, gender, nationality):
        User.__init__(self, email, first_name, last_name, mobile)
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.nationality = nationality

class Sponsor(User):
    __tablename__ = 'sponsors'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    address = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':'sponsor',
    }

    def __init__(self, email, first_name, last_name, mobile, address):
        User.__init__(self, email, first_name, last_name, mobile)
        self.address = address
