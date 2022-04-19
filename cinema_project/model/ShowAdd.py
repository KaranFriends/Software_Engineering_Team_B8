from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class ShowAdd(FlaskForm):
    show_date = StringField("First Name", validators=[InputRequired(), Length(min=4, max=20, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "First Name"})
    show_time = StringField("Last Name", validators=[InputRequired(), Length(min=4, max=20, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Last Name"})
    show_submit = SubmitField(label = "Add Show")