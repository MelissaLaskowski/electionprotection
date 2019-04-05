from flask import render_template, request, make_response, redirect, session, app, url_for, flash
from _init_ import app
from flask_login import current_user, login_user, logout_user, login_required

# imports OS and STRUCT are used to generate cryptographically secure random integers in python
import os
import struct

# using re to clean data from the user
import re

import dbManager
from voter import Voter
from vote import Vote
from election_timespan import ElectionTimespan
from forms import LoginForm

#a global connection for all the SQL queries
connection = dbManager.open_connection()

#response page if there is an error
@app.errorhandler(404)
def not_found(error):
	resp = make_response(render_template('error.html', error=error), 404)
	return resp


@app.route('/', methods=['GET', 'POST'])
def landing_page():
	startTime = ElectionTimespan.getStartTime(dbManager, connection)
	endTime = ElectionTimespan.getEndTime(dbManager, connection)
	if not startTime or not endTime:
		return not_found('GENERIC ERROR')

	form = LoginForm()

	#if they submitted all the necessary features of the login form
	if form.validate_on_submit():
		#check if the user is in the database
		user = Voter.getVoter(dbManager, connection, form.fullName.data)

		#confirm users password
		if user is None or not user.check_password(form.ssn.data, form.dob.data):

			#notify user authentication did not work
			return not_found('Either you have already voted or the information you entered did not match any on record. If you have not yet voted, please try again.')
		
		#login_user(user)
		return vote_page(user)
	return render_template("login.html", title='Sign In', form=form, startTime=startTime, endTime=endTime)

#login functionality for users 
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	#if they submitted all the necessary features of the login form
	if form.validate_on_submit():

		cleanSSN = re.sub(r"\D", "", form.ssn.data)
		cleanDOB = re.sub(r"\D", "", form.dob.data)

		#check if the user is in the database
		user = Voter.getVoter(dbManager, connection, form.fullName.data)

		#confirm users password
		if user is None or not user.check_password(cleanSSN, cleanDOB):
			#notify user authentication did not work
			return not_found('Either you have already voted or the information you entered did not match any on record. If you have not yet voted, please try again.')
		
		#login_user(user)
		return vote_page(user)
	return render_template('login.html', title='Sign In', form=form)

@app.route('/during')
def vote_page(user):
	#voter page endpoint

	if dbManager.isElectionActive(dbManager, connection):
		currentVoter = user
		myQuery = "SELECT * FROM candidates"
		candidates = dbManager.run_query(connection, myQuery)

		return render_template('during.html', currentVoter=currentVoter, candidates=candidates)
	else:
		return not_found('The election is over!')

@app.route('/after')
def results_page():
	if dbManager.isElectionOver(dbManager, connection):
		data = Vote.getAllVotes(dbManager, connection)
		return render_template('after.html', data=data)
	else:
		return not_found('The election has not yet concluded, please try again after the election end time.')

@app.route('/check', methods=['GET', 'POST'])
def results_check_page():
	if dbManager.isElectionOver(dbManager, connection):
		if request.method == 'POST':
			result = request.form
			searchQuery = result['search']
			data = Vote.getVote(dbManager, connection, searchQuery)
			if not data:
				return not_found('Your voter ID does not match any voter IDs recorded for this election. Please return to the previous page and make sure your voter ID is entered correctly.')
			
			return render_template('check.html', data=data)
		else:
			return render_template('check.html', data=None)
	else:
		return not_found('The election has not yet concluded, please try again after the election end time.')

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
	if request.method == 'POST':
		if dbManager.isElectionActive(dbManager, connection):
			result = request.form.getlist('candidate[]')
			full_legal_name = request.form.getlist('full_legal_name')[0]
			candiateID = result[0]

			# generate a cryptographically secure unsigned int
			randomVoterID = struct.unpack('I', os.urandom(4))[0]

			myQuery = "INSERT INTO votes (voter_id, candidate_id) VALUES ("+str(randomVoterID)+", "+str(candiateID)+");"
			cursor = connection.cursor()
			cursor.execute(myQuery)
			connection.commit()

			dbManager.mark_voted(full_legal_name)

			return render_template('verify.html', voterID=randomVoterID)
		else:
			return not_found('The election is over!')