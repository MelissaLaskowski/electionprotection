from flask import render_template, request, make_response, redirect, session, app, url_for, flash
from _init_ import app
from flask_login import current_user, login_user, logout_user, login_required

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


@app.route('/')
def landing_page():
	activated = True
	if activated == True:
		startTime = ElectionTimespan.getStartTime(dbManager, connection)
		endTime = ElectionTimespan.getEndTime(dbManager, connection)
		if not startTime or not endTime:
			#TODO perhaps we should create more specific errors, and perhaps we shouldn't, this is an important security decision that we need to make
			return not_found('GENERIC ERROR')

		return render_template("activated.html", startTime=startTime, endTime=endTime)
	else:
		return render_template("login.html")

#login functionality for users 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #if they submitted all the necessary features of the login form
    if form.validate_on_submit():
    	#check if the user is in the database
    	user = Voter.getVoter(dbManager, connection, form.fullName.data)
    	#confirm users password
    	if user is None or not user.check_password(form.ssn.data, form.dob.data):
    		#notify user authentication did not work
    		return not_found('Incorrect Info')
    	#login_user(user)
    	return vote_page(user)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/during')
def vote_page(user):
	#voter page endpoint
	#if request.method == 'POST':
	#	result = request.form
	#	fullName = result['Full Birthname']
	#	dob = result['DOB']
	#	ssn = result['SSN']

	currentVoter = user

	return render_template('during.html', currentVoter=currentVoter)

	return render_template('during.html')

@app.route('/after')
def results_page():
	data = Vote.getAllVotes(dbManager, connection)
	return render_template('after.html', data=data)

@app.route('/check', methods=['GET', 'POST'])
def results_check_page():
	if request.method == 'POST':
		result = request.form
		searchQuery = result['search']
		# TODO searchQuery should be cleaned before it is passed as a parameter to the DB!
		data = Vote.getVote(dbManager, connection, searchQuery)
		if not data:
			return not_found('Your voter ID does not match any voter IDs recorded for this election. Please return to the previous page and make sure your voter ID is entered correctly.')
		
		return render_template('check.html', data=data)
	else:
		return render_template('check.html', data=None)
