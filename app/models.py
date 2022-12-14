from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, DateTime,Enum
from app import db, app
from sqlalchemy.orm import relationship
from datetime import  datetime
from enum import Enum as UserEnum
from flask_login import UserMixin




class UserRole(UserEnum):
    USER = 1
    ADMIN = 2

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Flight(BaseModel):
    name = Column(String(50), nullable=False)
    image = Column(String(100))
    seats=Column(Integer, default=0)
    departure = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    Passenger = relationship('Passenger', backref='Flight', lazy=True)
    arrival_time = Column(DateTime,default=datetime.now())
    departure_time = Column(DateTime,default=datetime.now())

    def __str__(self):
        return self.name


class Passenger(BaseModel):
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    Date_of_birth = Column(DateTime,default=datetime.now())
    gender = Column(Text)
    flight_id = Column(Integer, ForeignKey(Flight.id), nullable=False)

    def __str__(self):
        return self.name


class Rank(BaseModel):
    name = Column(String(10),nullable=False)
    rank = Column(Float, nullable=False)
    flight_id = Column(Integer, ForeignKey(Flight.id), nullable=False)

    def __str__(self):
        return self.name

class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name




if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # p1 = Passenger(first_name='Phan',
        #                last_name='Tan',
        #                gender='nam',
        #                flight_id=1)
        #
        # p2 = Passenger(first_name='Phan',
        #                last_name='Tan',
        #                gender='nam',
        #                flight_id=2)
        # p3 = Passenger(first_name='Phan',
        #                last_name='Tan',
        #                gender='nam',
        #                flight_id=6)
        #
        # db.session.add_all([p1, p2, p3])
        # db.session.commit()
        #
        # f1=Flight(name ='jet' ,image='static/image/1.jpg' ,seats=500, departure ='HCM' ,destination ='HaNoi' , price =1000000,
        #         )
        # f2=Flight(name ='bambo' ,image='static/image/2.jpg' ,seats=40, departure ='DongThap' ,destination ='USA' , price =23000000
        #           )
        # f3=Flight(name ='vietnam airlines' ,image='static/image/3.jpg' ,seats=700, departure ='HCM' ,destination ='CanTho' , price =1000000
        #          )
        # f4=Flight(name ='vietnam airlines' ,image='static/image/3.jpg' ,seats=700, departure ='HCM' ,destination ='CanTho' , price =1000000
        #       )
        # f5=Flight(name ='bambo' ,image='static/image/2.jpg' ,seats=40, departure ='DongThap' ,destination ='USA' , price =23000000
        #           )
        # f6=Flight(name ='jet' ,image='static/image/1.jpg' ,seats=500, departure ='HCM' ,destination ='HaNoi' , price =1000000
        # )
        #
        # db.session.add_all([f1,f2,f3,f4,f5])
        # db.session.commit()


