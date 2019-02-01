from flask import render_template
from _init_ import app

@app.route('/')
def landing_page():
	#default landing page
	return "let's get voting!"