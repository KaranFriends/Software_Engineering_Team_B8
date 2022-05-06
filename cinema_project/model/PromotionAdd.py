from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm


class PromotionAdd(FlaskForm):
    code = StringField("Code",validators=[InputRequired(message='Promotion code is required.'), Length(min=5, max=30, message='Promotion code length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Promotion code"})
    discount = IntegerField("Discount",validators=[InputRequired()], render_kw={"placeholder": "email"})
    submit = SubmitField(label = "Submit")