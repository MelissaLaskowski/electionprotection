from flask import Flask
import mysql.connector
from _init_ import app
import csv
from werkzeug.security import generate_password_hash

#open database connection
def open_connection():
	connection = mysql.connector.connect(user='admin', password='ElectionProtectionPass', host='127.0.0.1', database='electiondata')
	return connection

#runs given queiries against the database
def run_query(connection, myQuery):
	myCursor = connection.cursor()
	myCursor.execute(myQuery)
	myData = myCursor.fetchall()
	return myData

#close the database connection
def close_connection(connection):
	connection.close()
	return

def register():
	#this is separate from run query becuase it does not fetch anything, just insert
	connection = open_connection()
	cursor = connection.cursor()
	voterReader = csv.reader(open('DB/voter_data.csv', newline=''))
	line_num = 0
	for row in voterReader:
		#do this check to avoid the headers to the csv file
		if line_num != 0:
			#the hash is generated from the ssn and dob
			password = generate_password_hash(row[1]+row[2])
			name =""; 
			if "'" in row[0]:
				for char in row[0]:
					if char== "'":
						name+="''"
					else:
						name+=char
			else:
				name = row[0]
			values = (" '"+name+"' , '"+password+"' , '"+row[3]+"' ")
			query =("INSERT INTO authorized_voters VALUES ( "+ values + ");")
			print(query)

			cursor.execute(query)
			connection.commit()
		else:
			line_num+=1
	close_connection(connection)

#after a user has voted, mark them as voted
def mark_voted(fullName):
	connection = open_connection()
	cursor = connection.cursor()
	query=("UPDATE authorized_voters SET has_voted='true' WHERE full_legal_name='"+fullName+"';")
	print(query)
	cursor.execute(query)
	connection.commit()