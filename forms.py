from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    full_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('SSN', validators=[DataRequired()])
    submit = SubmitField('Sign In')