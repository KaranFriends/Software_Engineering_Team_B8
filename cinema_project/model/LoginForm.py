from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField("Email",validators=[InputRequired(), Length(min=5, max=30, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "password"})
    submit = SubmitField(label = "Login")