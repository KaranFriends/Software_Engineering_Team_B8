from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class SearchAndFilter(FlaskForm):
    text = StringField("Search Movie", validators=[InputRequired()], render_kw={"placeholder": "Search Movie"})
    filter1 = SubmitField(label = "Horrow")
    filter2 = SubmitField(label = "Comedy")
    filter3 = SubmitField(label = "Action")
    search = SubmitField(label = "Search")