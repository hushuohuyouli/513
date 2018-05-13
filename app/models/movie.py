from app.extensions import db
import datetime
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer,primary_key=True)
    movie_name = db.Column(db.String(100))
    movie_img = db.Column(db.String(500))
    movie_url =db.Column(db.String(500))
    movie_type = db.Column(db.String(500))
    # time = db.Column(db.DateTime,datetime.now())

class Movie_test(db.Model):
    __tablename__ = 'movie_test'
    id = db.Column(db.Integer,primary_key=True)
    movie_name = db.Column(db.String(100),unique=True)
    movie_img = db.Column(db.String(500),unique=True)
    movie_url =db.Column(db.String(500),unique=True)
    movie_type = db.Column(db.String(500),unique=True)
