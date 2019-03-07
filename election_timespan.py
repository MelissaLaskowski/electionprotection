from flask import request

class ElectionTimespan:
	def __init__(self, start_time, end_time):
		self.start_time = start_time
		self.end_time = end_time

	def getStartTime(dbManager, connection):
		data = dbManager.run_query(connection, "SELECT start_time FROM electiondata.election_timespan")[0][0]
		return data

	def getEndTime(dbManager, connection):
		data = dbManager.run_query(connection, "SELECT end_time FROM electiondata.election_timespan")[0][0]
		return data

