#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, Amenity, Place
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_live():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places)


@app.teardown_appcontext
def close(db):
    """ Close the current sessions after each request """
    storage.close()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
