from flask import Flask
import mysql.connector
from _init_ import app
import csv
from werkzeug.security import generate_password_hash

#open database connection
def open_connection():
	#change any of the names below depending on db creation
	connection = mysql.connector.connect(user='admin', host='127.0.0.1', database='electionData')
	return connection

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
			hash = generate_password_hash(row[1]+row[2])
			print(hash, row[0], row[3])
			query ="INSERT INTO authorized_voters (full_legal_name, password, has_voted) VALUES ( %s, %s, %s );"

			print(query)
			cursor.execute(connection, query, (row[0], hash, row[3]))
		else:
			print(row)
			line_num+=1