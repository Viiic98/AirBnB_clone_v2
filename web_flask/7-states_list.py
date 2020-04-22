#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def l_states():
    """ List all states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(db):
    """ Close the current sessions after each request """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
