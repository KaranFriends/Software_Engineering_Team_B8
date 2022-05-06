from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class UserEdit(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired(message='First name must be entered.'), Length(min=1, max=20, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "First Name"})
    last_name = StringField("Last Name", validators=[InputRequired(message='Last name must be entered.'), Length(min=1, max=20, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Last Name"})
    email = EmailField("Email", validators=[InputRequired(message='Email must be entered.'), Length(min=5, max=30, message='Email length must be between %(min)d and %(max)dcharacters'), validators.Email("Please enter your email address.")], render_kw={"placeholder": "Email"})
    dob = DateField("Date of Birth", validators=[InputRequired(message='Date of birth must be entered.')], render_kw={"placeholder": "Date Of Birth"}, format='%Y-%m-%d')
    addressline1 = StringField("Address Line 1", validators=[InputRequired(message='Address must be entered.'), Length(min=4, max=20, message='Must enter valid address.')], render_kw={"placeholder": "Address Line 1"})
    addressline2 = StringField("Address Line 2", validators=[Length(min=4, max=20, message='Valid address must be entered.')], render_kw={"placeholder": "Address Line 2"})
    city = StringField("City", validators=[InputRequired(message='City must be entered.'), Length(min=4, max=20, message='Valid city name must be entered.')], render_kw={"placeholder": "City"})
    state = StringField("State", validators=[InputRequired(message='State must be entered.'), Length(min=4, max=20, message='Valid state name must be entered. Abbreviation not accepted.')], render_kw={"placeholder": "State"})
    zip = StringField("ZIP Code", validators=[InputRequired(message='Zip code must be entered.'), Length(min=4, max=20, message='Valid zip code must be entered.')], render_kw={"placeholder": "ZIP"})
    country = StringField("Country", validators=[InputRequired(message='Country must be entered.'), Length(min=4, max=20, message='Valid country must be entered. No abbreviation allowed.')], render_kw={"placeholder": "Country"})
    user_submit = SubmitField(label = "Deactivate")