# Create Model -> Create Table

from db import db

#Board
class Board(db.Model) :
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', back_populates='boards')
    
    
    
    
#User
class User(db.Model) :
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')