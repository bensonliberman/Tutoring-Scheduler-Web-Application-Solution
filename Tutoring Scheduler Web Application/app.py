"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
import backend
app = Flask(__name__)

# WILL LINK THESE LATERS RIGHT NOW JUST FOR IMAGE REFERENCE FOR SDD and 
#login and createaccount are commented out while I work on other stuff
'''
@app.route('/')
def loginPage():
    return render_template('login.html')

@app.route('/CreateAccount')
def createAcctPage():
    return render_template('createAccount.html')


'''
@app.route('/')
def homepage():
    pageType = backend.userClass
    return render_template('homepageLayout.html', pageType = pageType)


@app.route('/BecomeATutor')
def becomeATutorPage(): 
    pageType = backend.userClass
    return render_template('becomeATutor.html', pageType=pageType)
 
@app.route('/MyProfile')
def createAcctPage():
    pageType=backend.userClass
    userMajor = backend.studentMajor
    userClubs = backend.clubs
    userGradYear = backend.studentGradYear
    return render_template('myProfile.html', userMajor = userMajor, userClubs= userClubs, userGradYear=userGradYear, pageType=pageType )

@app.route('/MyCalendar')
def calendarPage(): 
    pageType = backend.userClass
    return render_template('calendar.html', pageType=pageType)

@app.route('/UpdatePassword')
def updatePasswordPage(): 
    pageType = backend.userClass
    return render_template('updatePassword.html', pageType=pageType)

@app.route('/TutoringApplications')
def viewTutAppsPage(): 
    pageType = backend.userClass
    return render_template('viewTutApps.html', pageType=pageType)
 


   




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
