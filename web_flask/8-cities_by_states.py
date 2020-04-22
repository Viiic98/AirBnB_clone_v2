#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_state():
    """ List states and cities """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def close(db):
    """ Close the current sessions after each request """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
