from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm

class ChangePasswordEnterEmail(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), validators.Email("Please enter your email address.")], render_kw={"placeholder": "Email"})
    submit = SubmitField(label = "Send OTP")    
