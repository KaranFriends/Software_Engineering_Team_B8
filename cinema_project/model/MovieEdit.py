from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class MovieEdit(FlaskForm):
    movie_title = StringField("Title",validators=[InputRequired(), Length(min=5, max=30, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    movie_director = StringField("Director",validators=[InputRequired(), Length(min=5, max=30, message='Director length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    movie_cast = StringField("Cast",validators=[InputRequired(), Length(min=5, max=30, message='Cast length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    movie_producer = StringField("Prodcuer",validators=[InputRequired(), Length(min=5, max=30, message='Producer length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    movie_synopsis = StringField("Synopsis",validators=[InputRequired(), Length(min=5, max=30, message='Synopsis length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    movie_status = StringField("Showing",validators=[InputRequired(), Length(min=5, max=30, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    movie_video = StringField("trailer Link",validators=[InputRequired(), Length(min=5, max=30, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    movie_submit = SubmitField(label = "Submit")