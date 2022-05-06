from wtforms import StringField, PasswordField, SubmitField, validators, EmailField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields import DateField
from flask_wtf import FlaskForm

class AddCard(FlaskForm):
    cardName = StringField("Name On Card" ,validators=[InputRequired(), Length(min=4, max=20, message='Card Name must be  %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Name On Card"})
    cardnumber = StringField("Card Number", validators=[InputRequired(), Length(min=12, max=12, message='Card Number must be  %(min)d characters')], render_kw={"placeholder": "Card Number"})
    cvv = StringField("CVV", validators=[InputRequired(), Length(min=3, max=3, message='Name length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "cvv"})
    expirationDate = DateField("Expiration Date", validators=[InputRequired()], render_kw={"placeholder": "Expiration Date"}, format='%Y-%m-%d')
    submit = SubmitField(label = "Add Card")  