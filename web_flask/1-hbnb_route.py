#!/usr/bin/python3
<<<<<<< HEAD
"""the `1-hbnb_route` module
starts a flask web application listening on `0.0.0.0:5000`
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def index():
    """returns `Hello HBNB!` message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns `HBNB` message"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 212529db4b955a72d996660137790c2497399ff5
