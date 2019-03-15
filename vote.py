class Vote:
	def __init__(self, voter_id, candidate_id):
		self.voter_id = voter_id
		self.candidate_id = candidate_id

	#TODO figure out how to return a vote object or array of vote objects efficiently
	def getVote(dbManager, connection, myVoterID):
		myQuery = "SELECT votes.voter_id, votes.candidate_id, candidates.candidate_name FROM votes INNER JOIN candidates ON votes.candidate_id=candidates.candidate_id where votes.voter_id='"+myVoterID+"';"
		
		try:
			data = dbManager.run_query(connection, myQuery)[0]
		except:
			return None
		
		return data

	def getAllVotes(dbManager, connection):
		myQuery = "SELECT votes.voter_id, votes.candidate_id, candidates.candidate_name FROM votes INNER JOIN candidates ON votes.candidate_id=candidates.candidate_id;"
		data = dbManager.run_query(connection, myQuery)
		return data
