#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import *
from models import storage

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """Displays the states and cities which are
    listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')