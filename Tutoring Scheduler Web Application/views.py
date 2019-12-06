from flask import Flask, render_template
import backend
import calendar

from app import app

@app.route('/')
def homepage():
    pageType = backend.userClass
    calMonth = backend.month
    return render_template('homepageLayout.html', pageType = pageType, calMonth=calMonth)

