from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class PromotionAdd(FlaskForm):
    code = StringField("Code",validators=[InputRequired(), Length(min=5, max=30, message='Director length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "email"})
    submit = SubmitField(label = "Submit")