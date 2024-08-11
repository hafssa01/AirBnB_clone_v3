#!/usr/bin/python3
"""
Creation of Flask app, and register the blueprint app_views to Flask instance
"""
from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_engine(exception):
    """
    Remove the current SQLAlchemy Session.
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Return a custom message for the 404 error
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
