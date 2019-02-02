from flask import render_template
from _init_ import app

@app.route('/')
def landing_page():
	#default landing page
	return render_template("landing.html")

@app.route('/vote')
def vote_page():
	#voter page endpoint
	return render_template('vote.html')

@app.route('/results')
def results_page():

	return render_template('results.html')