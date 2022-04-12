from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm

class ChangePasswordNewPassword(FlaskForm):
    password1 = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=20), validators.EqualTo('password2', message='Passwords must match')], render_kw={"placeholder": "Password"})
    password2 = PasswordField("Confirm Password", validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField(label = "Verify")    