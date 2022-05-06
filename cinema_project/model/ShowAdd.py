from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField, TimeField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class ShowAdd(FlaskForm):
    show_date = DateField("Show Date", validators=[InputRequired(message='Show date is required.')], render_kw={"placeholder": "Show Date"}, format='%Y-%m-%d')
    show_time = TimeField("Show Time", validators=[InputRequired(message='Show time is required.')], render_kw={"placeholder": "Show Time"}, format='%H:%M')
    show_submit = SubmitField(label = "Add Show")