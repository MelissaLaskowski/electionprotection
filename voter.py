from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from _init_ import login

class Voter(UserMixin):
	def __init__(self, full_legal_name, password_hash, has_voted):
		self.full_legal_name = full_legal_name
		self.password_hash = password_hash
		self.has_voted = has_voted

	@login.user_loader
	def getVoter(dbManager, connection, full_legal_name):
		myQuery = "SELECT * FROM authorized_voters WHERE (full_legal_name = '" + str(full_legal_name) + "')"
		data = dbManager.run_query(connection, myQuery)
		print(data)
		#if the data brings back a valid user
		if data is not None:
			#check if they have voted
			if data[0][2] == 'false':
				return Voter(data[0][0], data[0][1], data[0][2])
			else:
				return None
		else:

			return None


	def check_password(self, ssn, dob):
		myHash = generate_password_hash(ssn+dob)
		print("Checking password, ssn: " + str(ssn) + ", dob: " + str(dob) + ", hash: " + str(myHash))
		print("stored hash: " + str(self.password_hash))
		return check_password_hash(self.password_hash, ssn+dob)
