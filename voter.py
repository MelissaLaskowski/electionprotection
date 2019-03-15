class Voter:
	def __init__(self, full_legal_name, dob, ssn, has_voted, salt):
		self.full_legal_name = full_legal_name
		self.dob = dob
		self.ssn = ssn
		self.has_voted = has_voted
		self.salt = salt

	def getVoter(dbManager, connection, full_legal_name):
		myQuery = "SELECT * FROM authorized_voters WHERE (full_legal_name = '" + str(full_legal_name) + "')"
		data = dbManager.run_query(connection, myQuery)
		try:
			return Voter(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4])
		except:
			return None
