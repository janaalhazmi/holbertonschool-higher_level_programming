#!/usr/bin/python3
"""This is a modul for Creating a Basic HTML Template in Flask"""

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    """render the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """render to the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """render to the contact page"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
