from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.String(8), nullable=False)
    addressline1 = db.Column(db.String(20), nullable=False)
    addressline2 = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(8), nullable=False)
    state = db.Column(db.String(8), nullable=False)
    zip = db.Column(db.String(8), nullable=False)
    country = db.Column(db.String(8), nullable=False)
    cards = db.relationship('Card', backref='user', lazy=True)
    promotions = db.Column(db.String(1))
    user_type = db.Column(db.Integer, nullable=False)

class Card(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    cardNumber = db.Column(db.String(12), nullable=False)
    cardName = db.Column(db.String(15), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    expirationDate = db.Column(db.String(8), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)