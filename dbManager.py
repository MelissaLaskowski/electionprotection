from flask import Flask
import mysql.connector
from _init_ import app

data=[
	{
		'name':'Audrin',
		'place': 'kaka',
		'mob': '7736'
	},
	{
		'name': 'Stuvard',
		'place': 'Goa',
		'mob' : '546464'
	}
]

#open database connection
def open_connection():
	#change any of the names below depending on db creation
	connection = mysql.connector.connect(user='admin', password='ElectionProtectionPass', host='127.0.0.1', database='electionData')
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

