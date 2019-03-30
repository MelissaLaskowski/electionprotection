from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    fullName = StringField('Full Name', validators=[DataRequired()])
    ssn = PasswordField('Social Secutiry Number', validators=[DataRequired()])
    dob = PasswordField('Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	fullName = StringField('Full Name', validators=[DataRequired()])
	ssn = PasswordField('SSN', validators=[DataRequired()])
	dob = PasswordField('DOB', validators=[DataRequired()])

	def validate_ssn(self, ssn):
		len(ssn) == 9