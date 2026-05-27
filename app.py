#!/usr/bin/env python3
"""
Flask web application for the webapp project
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')


@app.route('/api/hello')
def api_hello():
    """API endpoint that returns a JSON response"""
    return {'message': 'Hello from the Flask API!'}


if __name__ == '__main__':
    app.run(debug=True, port=5000)
