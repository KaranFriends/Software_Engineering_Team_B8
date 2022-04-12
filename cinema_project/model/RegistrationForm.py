from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired(), Length(min=4, max=20, message='First Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "First Name"})
    last_name = StringField("Last Name", validators=[InputRequired(), Length(min=4, max=20, message='Last Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Last Name"})
    email = EmailField("Email", validators=[InputRequired(), Length(min=5, max=30, message='Email must be between %(min)d and %(max)dcharacters'), validators.Email("Please enter your email address.")], render_kw={"placeholder": "Email"})
    dob = DateField("Date of Birth", validators=[InputRequired()], render_kw={"placeholder": "Date Of Birth"}, format='%Y-%m-%d')
    addressline1 = StringField("Address Line 1", validators=[InputRequired(), Length(min=4, max=20, message='Address must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Address Line 1"})
    addressline2 = StringField("Address Line 2", validators=[InputRequired(), Length(min=4, max=20, message='Address must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Address Line 2"})
    city = StringField("City", validators=[InputRequired(), Length(min=4, max=20, message='City Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "City"})
    state = StringField("State", validators=[InputRequired(), Length(min=4, max=20, message='State Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "State"})
    zip = StringField("ZIP Code", validators=[InputRequired(), Length(min=5, max=5, message='ZIP length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "ZIP"})
    country = StringField("Country", validators=[InputRequired(), Length(min=4, max=20, message='Country Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Country"})
    cardName = StringField("Name On Card" ,validators=[InputRequired(), Length(min=4, max=20, message='Card Name must be  %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Name On Card"})
    cardnumber = StringField("Card Number", validators=[InputRequired(), Length(min=12, max=12, message='Card Number must be  %(min)d characters')], render_kw={"placeholder": "Card Number"})
    cvv = StringField("CVV", validators=[InputRequired(), Length(min=3, max=3, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "cvv"})
    expirationDate = DateField("Expiration Date", validators=[InputRequired()], render_kw={"placeholder": "Expiration Date"}, format='%Y-%m-%d')
    password1 = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=20), validators.EqualTo('password2', message='Passwords must match')], render_kw={"placeholder": "Password"})
    password2 = PasswordField("Confirm Password", validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Confirm Password"})
    # promotion = SelectField("Apply for promotion")
    submit = SubmitField(label = "Register")  