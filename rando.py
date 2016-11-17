from flask import flask
import logging
from random import randint


random_number=randint(0,9)

app = Flask(__name__)

app.route('/random')
def myrando():
	return '<h1>{}</h1>'.format(randint(0,9))

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500