from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False) #note: in sqlite, primary key column is not nullable by default
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
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cardNumber = db.Column(db.String(12), nullable=False)
    cardName = db.Column(db.String(15), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    expirationDate = db.Column(db.String(8), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

#also change id name??????
class Ticket(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        ticket_category_id=db.Column(db.Integer, nullable=False)
        ticket_category_quantity=db.Column(db.Integer, default=0, nullable=False)
        seat_no=db.Column(db.Integer, nullable=False)

class Review(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        review_comment = db.Column(db.String(12), nullable=False)
        review_rating = db.Column(db.String(12), nullable=False)  #int(1)
        user_ID=db.Column(db.String(12), db.ForeignKey("User.id"), nullable=False) #int(1)

#not finished
class Movie(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        movie_title = db.Column(db.String(12), nullable=False) #char(50)
        movie_director_name = db.Column(db.String(12), nullable=False) #char(50)
        movie_cast_name = db.Column(db.String(12), nullable=False) #char(50)
        movie_producer_name = db.Column(db.String(12), nullable=False) #char(50)
        movie_synopsis = db.Column(db.String(12), nullable=False) #char(10)
        movie_status = db.Column(db.String(12), nullable=False) #int(1)
        movie_trailer = db.Column(db.String(12), nullable=False) #int(100)
        movie_picture = db.Column(db.String(12), nullable=False) #int(100)
        movie_video = db.Column(db.String(12), nullable=False) #int(100)
        category_id = db.Column(db.Integer, db.ForeignKey("MovieCategory.id"), nullable=False)

#not finished
class MovieCategory(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        category_name = db.Column(db.String(12), nullable=False) #char(10)

#not finished
class Show(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        show_date = db.Column(db.Date, nullable=False)
        show_time = db.Column(db.Time, nullable=False)
        movie_id = db.Column(db.Integer, db.ForeignKey("Movie.id"), nullable=False)
        showroom_id = db.Column(db.Integer, db.ForeignKey("Showroom.id"), nullable=False)
        vacant_seats = db.Column(db.ARRAY[db.Integer], nullable=False)

#not finished
class Showroom(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        total_seats = db.Column(db.Integer, nullable=False)


class Booking(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)
        show_id = db.Column(db.Integer, db.ForeignKey("Show.id"), nullable=False)
        card_id = db.Column(db.Integer, db.ForeignKey("Card.id"), nullable=False)
        booking_date = db.Column(db.Date, nullable=False)
        booking_time = db.Column(db.Time, nullable=False)
        booking_price = db.Column(db.Integer, nullable=False)


class TicketBooking(db.Model, UserMixin):
        booking_id = db.Column(db.Integer, db.ForeignKey("Booking.id"), nullable=False)
        ticket_id = db.Column(db.Integer, db.ForeignKey("Ticket.id"), nullable=False)


class TicketPrice(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        ticket_price = db.Column(db.Integer, nullable=False)
        ticket_category_name = db.Column(db.Enum, nullable=False)


# table for storing images directly
class Img(db.Model, UserMixin):
        id=db.Column(db.Integer, primary_key=True, nullable=False)
        img=db.Column(db.Text, unique=True, nullable=False)
        name=db.Column(db.String(12), nullable=False )
        mimeType=db.Column(db.String(20), nullable=False)