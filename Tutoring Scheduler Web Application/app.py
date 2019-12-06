"""
This script runs the application using a development server.
"""

from flask import Flask, render_template,flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import backend
import calendar


app = Flask(__name__)

app.secret_key = 'skoeruosijfoaiighiries'

from views import *


if __name__ == '__main__':
    
    app.run(debug=True)
