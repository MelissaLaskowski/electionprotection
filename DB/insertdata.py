import mysql.connector
import csv
def register_user(cursor, connection):
	
	voterReader = csv.reader(open('DB/voters.csv', newline=''))
	line_num = 0
	for row in voterReader:
		#do this check to avoid the headers to the csv file
		if line_num != 0:
			#the hash is generated from the ssn and dob
			
			values = (" '"+row[0]+"' , '"+row[1]+"' , '"+row[2]+"' ")
			query =("INSERT INTO authorized_voters VALUES ( "+ values + ");")

			cursor.execute(query)
			connection.commit()
		else:
			line_num+=1

def add_time(cursor, connection):
	timeReader = csv.reader(open('DB/election_timespan.csv', newline=''))
	line_num = 0
	for row in timeReader:
		#do this check to avoid the headers to the csv file
		if line_num != 0:
			#the hash is generated from the ssn and dob
			
			values = (" '"+row[0]+"' , '"+row[1]+"' ")
			query =("INSERT INTO election_timespan VALUES ( "+ values + ");")

			cursor.execute(query)
			connection.commit()
		else:
			line_num+=1

def add_candidates(cursor, connection):
	candidatesReader = csv.reader(open('DB/candidates.csv', newline=''))
	line_num = 0
	for row in candidatesReader:
		#do this check to avoid the headers to the csv file
		if line_num != 0:
			#the hash is generated from the ssn and dob
			
			values = (" '"+row[0]+"' , '"+row[1]+"' ")
			query =("INSERT INTO candidates VALUES ( "+ values + ");")
			cursor.execute(query)
			connection.commit()
		else:
			line_num+=1

def main():
	connection = mysql.connector.connect(user='electionAdmin', host='127.0.0.1', database='electiondata')
	cursor = connection.cursor()
	#insert authorized user data
	register_user(cursor, connection)
	#insert election time data
	add_time(cursor, connection)
	#insert candidate data
	add_candidates(cursor, connection)
main()