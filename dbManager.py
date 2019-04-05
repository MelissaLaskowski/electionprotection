from flask import Flask
import mysql.connector
from _init_ import app
import csv

#open database connection
def open_connection():
	connection = mysql.connector.connect(user='admin', password='ElectionProtectionPass', host='127.0.0.1', database='electiondata')
	return connection

#runs given queiries against the database
def run_query(connection, myQuery):
	myCursor = connection.cursor(prepared=True)
	myCursor.execute(myQuery)
	myData = myCursor.fetchall()
	return myData

#close the database connection
def close_connection(connection):
	connection.close()
	return

#after a user has voted, mark them as voted
def mark_voted(fullName):
	connection = open_connection()
	cursor = connection.cursor()
	query=("UPDATE authorized_voters SET has_voted='true' WHERE full_legal_name='"+fullName+"';")
	print(query)
	cursor.execute(query)
	connection.commit()