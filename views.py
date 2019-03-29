from flask import render_template, request, make_response, redirect, session, app
from _init_ import app
from datetime import timedelta

import dbManager
from voter import Voter
from vote import Vote
from election_timespan import ElectionTimespan
from forms import LoginForm

connection = dbManager.open_connection()

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

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
		return render_template("before.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	return redirect(url_for('/during'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/during', methods=['POST'])
def vote_page():
	#voter page endpoint
	if request.method == 'POST':
		result = request.form
		fullName = result['Full Birthname']
		dob = result['DOB']
		ssn = result['SSN']

		currentVoter = Voter.getVoter(dbManager, connection, fullName)

		if not currentVoter:
			return not_found('Your information does not match any registered voter. Please return to the previous page and make sure your information is entered correctly.')
		
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
