from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class ChangePasswordVerifyOTP(FlaskForm):
    otp = IntegerField("OTP", validators=[InputRequired()], render_kw={"placeholder": "OTP"})
    submit = SubmitField(label = "Verify")    