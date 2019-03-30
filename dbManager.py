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
	voterReader = csv.reader(open('DB/voter_data.csv', newline=''))
	line_num = 0
	for row in voterReader:
		if line_num != 0:
			hash = generate_password_hash(row[1]+row[2])
			print(hash)
			"INSERT INTO authorized_voters (full_legal_name, ssn, has_voted) VALUES ( "+row[0]+" , "+hash+" , "+row[3] +" );"

		else:
			print(row)
			line_num+=1