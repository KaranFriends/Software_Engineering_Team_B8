from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed


class AddMovie(FlaskForm):
    movie_title = StringField("Title",validators=[InputRequired(message='Movie title is required.'), Length(min=1, max=100, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Title"})
    movie_director = StringField("Director",validators=[InputRequired(message='Movie director is required.'), Length(min=3, max=100, message='Director length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Director"})
    movie_cast = StringField("Cast",validators=[InputRequired(message='Movie cast is required.'), Length(min=3, max=100, message='Cast length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Cast"})
    movie_producer = StringField("Producer",validators=[InputRequired(message='Producer is required.'), Length(min=3, max=100, message='Producer length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Producer"})
    movie_synopsis = StringField("Synopsis",validators=[InputRequired(message='Synopsis is required.'), Length(min=5, max=200, message='Synopsis length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Synopsis"})
    movie_status = StringField("Showing",validators=[InputRequired(message='Movie status is required.'), Length(min=1, max=30, message='Valid movie status is required')], render_kw={"placeholder": "Status"})
    movie_video = StringField("trailer Link",validators=[InputRequired(message='Movie trailer link is required.'), Length(min=5, max=200, message='Valid link to movie traier is required')], render_kw={"placeholder": "Trailer link"})
    movie_submit = SubmitField(label = "Submit")