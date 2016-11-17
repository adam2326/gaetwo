from flask import flask
import logging
from random import randint


app = Flask(__name__)

@app.route('/random')
def myrando():
	return 'random'

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
