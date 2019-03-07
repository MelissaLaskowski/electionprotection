from flask import render_template, request
from _init_ import app

import dbManager
from voter import Voter

connection = dbManager.open_connection()

@app.route('/')
def landing_page():
	activated = True
	if activated == True:
		return render_template("activated.html")
	else:
		return render_template("before.html")

#@app.route('/activated')
#def landing_page():
#	return render_template("activated.html")

@app.route('/during', methods=['POST'])
def vote_page():
	#voter page endpoint
	if request.method == 'POST':
		result = request.form
		fullName = result['Full Birthname']
		dob = result['DOB']
		ssn = result['SSN']

		data = dbManager.run_query(connection, "SELECT * FROM electiondata.authorized_voters WHERE (full_legal_name = '" + str(fullName) + "')")

		currentVoter = Voter(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4])
		
		return render_template('during.html', currentVoter=currentVoter)

	return render_template('during.html')

@app.route('/after')
def results_page():
	return render_template('after.html')

@app.route('/check')
def results_check_page():
	return render_template('check.html')

@app.route('/db_test')
def db_test_page():
	data = dbManager.run_query(connection, "SELECT * from votes")
	return render_template('db_test.html', data=data)