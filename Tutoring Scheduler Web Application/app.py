"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
import backend
import calendar


app = Flask(__name__)

from views import *


# WILL LINK THESE LATERS RIGHT NOW JUST FOR IMAGE REFERENCE FOR SDD and 
#login and createaccount are commented out while I work on other stuff
'''
@app.route('/')
def loginPage():
    pageType = backend.userClass
    return render_template('login.html', pageType=pageType)

@app.route('/CreateAccount')
def createAcctPage():
    return render_template('createAccount.html')


@app.route('/')
def homepage():
    pageType = backend.userClass
    calMonth = backend.month
    return render_template('homepageLayout.html', pageType = pageType, calMonth=calMonth)


@app.route('/BecomeATutor')
def becomeATutorPage(): 
    pageType = backend.userClass
    return render_template('becomeATutor.html', pageType=pageType)

@app.route('/MyProfile')
def profilePage():
    pageType=backend.userClass
    userMajor = backend.studentMajor
    userClubs = backend.clubs
    userGradYear = backend.studentGradYear
    return render_template('myProfile.html', userMajor = userMajor, userClubs= userClubs, userGradYear=userGradYear, pageType=pageType )


@app.route('/MyCalendar')
def calendarPage(): 
    pageType = backend.userClass
    calMonth = backend.month
   
    return render_template('calendar.html', pageType=pageType, calMonth = calMonth)

@app.route('/MyWeeklyCalendar')
def weeklyCalendarPage(): 
    pageType = backend.userClass
    calMonth = backend.month
    return render_template('weeklyCalendar.html', pageType=pageType, calMonth = calMonth)


@app.route('/UpdatePassword')
def updatePasswordPage(): 
    pageType = backend.userClass
    return render_template('updatePassword.html', pageType=pageType)

@app.route('/TutoringApplications')
def viewTutAppsPage(): 
    pageType = backend.userClass
    return render_template('viewTutApps.html', pageType=pageType)
 
@app.route('/ApplicationDetail')
def viewAppDetailsPage():
    pageType = backend.userClass
    applicantName = backend.appName
    applicantID = backend.appid
    applicantRecLetter = backend.appRec
    applicantEmail = backend.email
    return render_template('tutAppDetail.html', pageType = pageType, applicantName = applicantName,
                           applicantID = applicantID, applicantRecLetter = applicantRecLetter,applicantEmail = applicantEmail)

@app.route('/SystemInfo')
def viewSystemInfoPage(): 
    pageType = backend.userClass
    return render_template('systemInfo.html', pageType=pageType)

@app.route('/AdminManagement')
def adminMmgtPage(): 
    pageType = backend.userClass
    return render_template('adminMmgt.html', pageType=pageType)
   
@app.route('/ManageTutors')
def tutMmgtPage(): 
    pageType = backend.userClass
    return render_template('tutMmgt.html', pageType=pageType)

@app.route('/WeeklyView')
def weeklyApptViewPage(): 
    pageType = backend.userClass
    calMonth = backend.month
    return render_template('/weeklyView.html', pageType=pageType, calMonth=calMonth)
   
@app.route('/FindATutor')
def tutorSelctPage(): 
    pageType = backend.userClass
    
    return render_template('/tutorSelect.html', pageType=pageType)

@app.route('/ScheduleAppointment')
def schedApptPage(): 
    pageType = backend.userClass
    calMonth=backend.month
    
    return render_template('/schedAppt.html', calMonth=calMonth, pageType=pageType)

@app.route('/TutorLocationAssignment')
def tutLocationAssignmetPage(): 
    pageType = backend.userClass
    
    return render_template('/tutAssignment.html', pageType=pageType)

@app.route('/MyTutoringAvailability')
def tutAvailabilityPage(): 
    pageType = backend.userClass
    
    return render_template('/tutAvailability.html', pageType=pageType)

@app.route('/EditDaily')
def editDailyAvailabilityPage(): 
    pageType = backend.userClass
    
    return render_template('/dailyAvail.html', pageType=pageType)

@app.route('/EditBlackoutDates')
def editBlackoutDatesPage(): 
    pageType = backend.userClass
    
    return render_template('/blackoutAvail.html', pageType=pageType)

@app.route('/MyWorkRecord')
def workRecordPage(): 
    pageType = backend.userClass
    
    return render_template('/workRecord.html', pageType=pageType)

@app.route('/ManageTutoringFacilities')
def manageFacilPage(): 
    pageType = backend.userClass
    
    return render_template('/manageFacil.html', pageType=pageType)

'''

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
