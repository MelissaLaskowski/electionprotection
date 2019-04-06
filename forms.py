from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    fullName = StringField('Full Name', validators=[DataRequired()])
    ssn = PasswordField('Social Security Number (only the numbers)', validators=[DataRequired()])
    dob = PasswordField('Date of Birth (MMDDYYY, only the numbers, no slashes or dashes)', validators=[DataRequired()])
    submit = SubmitField('Sign In')