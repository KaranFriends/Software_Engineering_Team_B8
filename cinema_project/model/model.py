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
     reviews = db.relationship('Review', backref='user', lazy=True)
     bookings = db.relationship('Booking', backref='user', lazy=True)

class Card(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     cardNumber = db.Column(db.String(12), nullable=False)
     cardName = db.Column(db.String(15), nullable=False)
     cvv = db.Column(db.String(3), nullable=False)
     expirationDate = db.Column(db.String(8), nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
         nullable=False)
     bookings = db.relationship('Booking', backref='card', lazy=True)

class Ticket(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         ticket_category_id=db.Column(db.Integer, nullable=False)
         ticket_category_quantity=db.Column(db.Integer, default=0, nullable=False)
         seat_no=db.Column(db.Integer, nullable=False)
         ticketBookings = db.relationship('TicketBooking', backref='ticket', lazy=True)

class Review(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         review_comment = db.Column(db.String(12), nullable=False)
         review_rating = db.Column(db.Integer, nullable=False)
         user_ID=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Movie(db.Model, UserMixin):
          id = db.Column(db.Integer, primary_key=True, nullable=False)
          movie_title = db.Column(db.String(12), nullable=False) #char(50)
          movie_director_name = db.Column(db.String(12), nullable=False) #char(50)
          movie_cast_name = db.Column(db.String(12), nullable=False) #char(50)
          movie_producer_name = db.Column(db.String(12), nullable=False)
          movie_synopsis = db.Column(db.String(12), nullable=False)
          movie_rating = db.Column(db.String(12), nullable=False) #changed to movie rating and is string type
          #movie_trailer = db.Column(db.String(50), nullable=False) #changed to string to contain url
          movie_picture = db.Column(db.String(50), nullable=False) #changed to string for now to contain link to image
          movie_video = db.Column(db.String(50), nullable=False) #changed to string to contain url
          #category_ID=db.Column(db.Integer, db.ForeignKey('moviecategory.id'), nullable=False)
          shows = db.relationship('Show', backref='movie', lazy=True)
          moviesorted = db.relationship('Moviecategory', backref='movie', lazy=True)



class Moviecategory(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         category_name = db.Column(db.String(12), nullable=False)
         movie_ID=db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)


class Show(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         show_date = db.Column(db.Date, nullable=False)
         show_time = db.Column(db.Time, nullable=False)
         movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
         showroom_id = db.Column(db.Integer, db.ForeignKey("showroom.id"), nullable=False)
         bookings = db.relationship('Booking', backref='show', lazy=True)
         seatAvail= db.relationship('Seat', backref='show', lazy=True)


class Showroom(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         total_seats = db.Column(db.Integer, nullable=False)
         shows = db.relationship('Show', backref='showroom', lazy=True)

class Seat(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    show_ID=db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    seatNumber=db.Column(db.Integer, nullable=False)


class Booking(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
         show_id = db.Column(db.Integer, db.ForeignKey("show.id"), nullable=False)
         card_id = db.Column(db.Integer, db.ForeignKey("card.id"), nullable=False)
         booking_date = db.Column(db.Date, nullable=False)
         booking_time = db.Column(db.Time, nullable=False)
         ticketBookings = db.relationship('TicketBooking', backref='booking', lazy=True)


class TicketBooking(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"), nullable=False)
         ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.id"), nullable=False)
         booking_price = db.Column(db.Integer, nullable=False)


class TicketPrice(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         ticket_price = db.Column(db.Integer, nullable=False)
         ticket_category_name = db.Column(db.Enum, nullable=False)


# # table for storing images directly
class Img(db.Model, UserMixin):
          id=db.Column(db.Integer, primary_key=True, nullable=False)
          img=db.Column(db.Text, unique=True, nullable=False)
          name=db.Column(db.String(12), nullable=False )
          mimeType=db.Column(db.String(20), nullable=False)


