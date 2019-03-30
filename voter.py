from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from _init_ import login

class Voter(UserMixin):
	def __init__(self, full_legal_name, dob, ssn, has_voted, salt):
		self.full_legal_name = full_legal_name
		self.dob = dob
		self.ssn = ssn
		self.has_voted = has_voted
		self.salt = salt

	@login.user_loader
	def getVoter(dbManager, connection, full_legal_name):
		myQuery = "SELECT * FROM authorized_voters WHERE (full_legal_name = '" + str(full_legal_name) + "')"
		data = dbManager.run_query(connection, myQuery)
		try:
			return Voter(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4])
		except:
			return None

	def set_password(self, ssn, dob):
		self.password_hash = generate_password_hash(ssn+dob)

	def check_password(self, ssn, dob):
		return check_password_hash(self.password_hash, ssn+dob)
