from app.models import Flight,Passenger,User
from app import db
import hashlib



def load_flight() :
    return Flight.query.all()

def load_passenger(fl_id=None, kw=None):
    query = Passenger.query

    if fl_id:
        query = query.filter(Passenger.flight_id.__eq__(fl_id))

    if kw:
        query = query.filter(Passenger.name.contains(kw))

    return query.all()


def get_flight_by_id(fl_id):
    return Flight.query.get(fl_id)

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()


def register(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, username=username.strip(), password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()