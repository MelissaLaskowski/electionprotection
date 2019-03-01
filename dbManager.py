from flask import Flask
import mysql.connector
from _init_ import app

#open database connection
def open_connection():
	#change any of the names below depending on db creation
	connection = mysql.connector.connect(user='admin', host='127.0.0.1', database='electionData')
	return connection

#close the database connection
def close_connection(connection):
	connection.close()
	return