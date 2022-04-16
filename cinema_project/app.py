from distutils.log import error
from wsgiref.validate import validator
from flask import Flask, flash, g, make_response, redirect, render_template, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, login_user, logout_user, current_user
from graphviz import render
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import emailService
import random
from model.model import User
#from model.model import User, Card #Ticket, Review, Movie, MovieCategory, Show, Showroom, Booking, TicketBooking, TicketPrice, Img
from model.LoginForm import LoginForm
from model.RegistrationForm import RegistrationForm
from model.UserEditForm import UserEditForm
from model.ChangePasswordEnterEmail import ChangePasswordEnterEmail
from model.ChangePasswordVerifyOTP import ChangePasswordVerifyOTP
from model.ChangePasswordNewPassword import ChangePasswordNewPassword
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'adjaiosjdioasjdio'
app.config['REMEBER_COOKIE_DURATION'] = timedelta(hours=3)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

@app.before_first_request
def create_tables():
    db.create_all()


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
          movie_status = db.Column(db.Integer, nullable=False) 
          movie_trailer = db.Column(db.Integer, nullable=False) 
          movie_picture = db.Column(db.Integer, nullable=False)
          movie_video = db.Column(db.Integer, nullable=False) 
          category_ID=db.Column(db.Integer, db.ForeignKey('moviecategory.id'), nullable=False)
          shows = db.relationship('Show', backref='movie', lazy=True)



class Moviecategory(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         category_name = db.Column(db.String(12), nullable=False)
         movies = db.relationship('Movie', backref='moviecategory', lazy=True)


class Show(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         show_date = db.Column(db.Date, nullable=False)
         show_time = db.Column(db.Time, nullable=False)
         movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
         showroom_id = db.Column(db.Integer, db.ForeignKey("showroom.id"), nullable=False)
         bookings = db.relationship('Booking', backref='show', lazy=True)
         seatAvail= db.relationship('Seatavail', backref='show', lazy=True)


class Showroom(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         total_seats = db.Column(db.Integer, nullable=False)
         shows = db.relationship('Show', backref='showroom', lazy=True)
         seats=db.relationship('Seat', backref='showroom', lazy=True)

class Seat(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    seatAvail=db.relationship('Seatavail', backref='seat', lazy=True)

class Seatavail(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    show_ID=db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    seat_ID= db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    available=db.Column(db.Integer, nullable=False) #0 for false, 1 for true, sqlite does not have boolean data type


class Booking(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
         show_id = db.Column(db.Integer, db.ForeignKey("show.id"), nullable=False)
         card_id = db.Column(db.Integer, db.ForeignKey("card.id"), nullable=False)
         booking_date = db.Column(db.Date, nullable=False)
         booking_time = db.Column(db.Time, nullable=False)
         booking_price = db.Column(db.Integer, nullable=False)
         ticketBookings = db.relationship('TicketBooking', backref='booking', lazy=True)


class TicketBooking(db.Model, UserMixin):
         id = db.Column(db.Integer, primary_key=True, nullable=False)
         booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"), nullable=False)
         ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.id"), nullable=False)


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






# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

@app.route('/index')
def index():
    if session['email']:
        if User.query.filter_by(email = session['email']).first().user_type == 1:
            flash("admin cannot access this portal")
            return render_template('login.html', form=LoginForm())
    return render_template('index.html')


@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    error=None
    if request.method == 'POST':
        user = User.query.filter_by(email = form.email.data).first()
        if form.validate_on_submit():
            print(request.form.get('remember'))
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    session['email'] = user.email
                    if request.form.get('remember') == "1":
                        print(request.form.get('remember'))
                        resp = make_response(render_template('index.html'))
                        resp.set_cookie('email', user.email)
                        return resp
                    if user.user_type == 1:
                        return redirect(url_for('admin_portal3'))
                    else:
                        return redirect(url_for('index'))
                else:
                    flash('Invalid Login credentials',"error")
                    return render_template('login.html', form = form)
            flash('Invalid Login credentials')
            return render_template('login.html', form = form)
    else:
        # request.form.setlist('remember',["1"])
        return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    session['email'] = None
    resp.delete_cookie('email')
    return resp


@app.route('/movie_details')
def movie_details():
    return render_template('movie_details.html')

@app.route('/admin_portal3')
def admin_portal3():
    return render_template('admin_portal3.html')

@app.route('/promotions')
def promotions():
    return render_template('promotions.html')

@app.route('/edit_profile', methods=['POST','GET'])
# @login_required
def edit_profile():
    if session['email']:
        error=None
        if request.method == 'POST':
            user = User.query.filter_by(email = session['email']).first()
            card = Card.query.filter_by(user_id = user.id).first()
            form = UserEditForm()
            if form.validate_on_submit():    
                user.first_name = form.first_name.data
                user.last_name = form.last_name.data
                user.dob = str(form.dob.data).split(" ")[0]
                user.addressline1 = form.addressline1.data
                user.addressline2 = form.addressline2.data
                user.city = form.city.data
                user.state = form.state.data
                user.zip = form.zip.data
                user.country = form.country.data
                if request.form.get('promotion'):
                    user.promotions = "1"
                else:
                    user.promotion = "0"
                # card.cardNumber = form.cardnumber.data
                # card.cardName = form.cardName.data
                # card.cvv = form.cvv.data
                # card.expirationDate = str(form.expirationDate.data).split(" ")[0]
                
                # db.session.flush()
                db.session.add(user)
                # db.session.add(card)
                db.session.commit()
                flash('Profile has been updated')
                return render_template('edit_profile.html',form=form)
        user = User.query.filter_by(email = session['email']).first()
        # card = Card.query.filter_by(user_id = user.id).first()
        form = UserEditForm()
        if user.user_type == 0:
            form.first_name.data = user.first_name
            form.last_name.data = user.last_name
            form.email.data = user.email
            form.dob.data = datetime.strptime(str(user.dob), '%Y-%m-%d')
            form.addressline1.data = user.addressline1
            form.addressline2.data = user.addressline2
            form.city.data = user.city
            form.state.data = user.state
            form.zip.data = user.zip
            # form.cardName.data = card.cardName
            # form.cardnumber.data = card.Number
            # form.cvv.data = card.cvv
            # form.expirationDate.data = datetime.strptime(str(card.expirationDate), '%Y-%m-%d')
            
            return render_template('edit_profile.html',form=form, promo=user.promotions)
        else:
            flash('Admin cannot access that page')
            return render_template('login.html', form = LoginForm())
    flash('Please Login first to access page')
    return render_template('login.html', form = LoginForm())

@app.route('/suprise')
# @login_required
def suprise():
    return render_template('suprise.html')

@app.route('/forgotPassword', methods=['POST', 'GET'])
def forgotPassword():
    form = ChangePasswordEnterEmail()
    if request.method == 'POST':
        user = User.query.filter_by(email = form.email.data).first()
        print(user)
        if user:
            # number = random.randint(1000,9999)
            # session['otp'] = number
            # session['otp_email'] = form.email.data
            # print(number)
            print("-------------------------------------------")
            if form.validate_on_submit():
                number = random.randint(1000,9999)
                session['otp'] = number
                session['otp_email'] = form.email.data
                print(number)
                print("********************************************")
                emailService.emailS(form.email.data, "OTP is "+str(number),"Verfiy OTP")
                return redirect(url_for('verifyOTP'))
        flash("Email Not Registered")
        return render_template('changePasswordEnterEmail.html', form=form)
    return render_template('changePasswordEnterEmail.html', form=form)

@app.route('/verifyOTP', methods=['POST', 'GET'])
def verifyOTP():
    form = ChangePasswordVerifyOTP()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.otp.data == session['otp']:
                return redirect(url_for('changePassword'))
            flash("Wrong OTP entered")
            return render_template('verifyOTP.html', form=form)
    return render_template('verifyOTP.html', form=form)

@app.route('/changePassword', methods=['POST', 'GET'])
def changePassword():
    form = ChangePasswordNewPassword()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email = session['otp_email']).first()
            user.password = bcrypt.generate_password_hash(form.password1.data)
            db.session.add(user)
            db.session.commit()
            flash("Password Changed Successfully")
            resp = make_response(redirect('login'))
            session['otp_email'] = None
            session['otp'] = None
            resp.delete_cookie('email')
            return resp
    return render_template('changePassword.html', form=form)

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email = form.email.data).first()
            if user:
                flash("Email already registered")
                return render_template('register.html', form=form)
            else:
                if emailService.emailS(form.email.data, "Thank you for registration", "Welcome"):
                    if request.form.get('promotion'):
                        promo = "1"
                    else:
                        promo = "0"
                    user=User(email = form.email.data,\
                        password = bcrypt.generate_password_hash(form.password2.data),\
                        first_name = form.first_name.data,\
                        last_name = form.last_name.data,\
                        dob = str(form.dob.data).split(" ")[0],\
                        addressline1 = form.addressline1.data,\
                        addressline2 = form.addressline2.data,\
                        city = form.city.data,\
                        state = form.state.data,\
                        zip = form.zip.data,\
                        country = form.country.data,\
                        promotions = promo,\
                        user_type = 0
                        )
                    db.session.add(user)
                    db.session.commit()
                    user = User.query.filter_by(email = form.email.data).first()
                    id = user.id
                    card=Card(cardNumber=bcrypt.generate_password_hash(form.cardnumber.data),\
                        cardName=bcrypt.generate_password_hash(form.cardName.data),\
                        cvv=bcrypt.generate_password_hash(form.cvv.data),\
                        expirationDate=bcrypt.generate_password_hash(str(form.expirationDate.data).split(" ")[0]),\
                        user_id=user.id)
                    db.session.add(card)
                    db.session.commit()
                    # session.pop('email', None)
                    # request.cookies.pop('email', None)
                    flash('Registration successful')
                    return render_template('login.html', form=LoginForm())
                else:
                    flash('Please provide a valid Email Address')
                    return render_template('register.html', form=form)
        else:
            flash('Welcome to registration page')
            return render_template('register.html', form=form)
    else:
        flash('Welcome to registration page')
        return render_template('register.html', form=form)

# @app.before_request
# def before_request():
#     g.user = None

#     if 'user_id' in session:
#         users
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user

if __name__ == '__main__':
    app.run(debug=True)