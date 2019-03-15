from flask import request

class ElectionTimespan:
	def __init__(self, start_time, end_time):
		self.start_time = start_time
		self.end_time = end_time

	def getStartTime(dbManager, connection):
		try:
			data = dbManager.run_query(connection, "SELECT start_time FROM election_timespan")[0][0]
		except:
			return None
		
		return data

	def getEndTime(dbManager, connection):
		try:
			data = dbManager.run_query(connection, "SELECT end_time FROM election_timespan")[0][0]
		except:
			return None
		
		return data

