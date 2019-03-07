from flask import render_template
from _init_ import app

import dbManager

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

@app.route('/during')
def vote_page():
	#voter page endpoint
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