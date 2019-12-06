"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import sqlite3
from flask import Flask, render_template, request, redirect, flash
import backend
import calendar
import os

app = Flask(__name__)
app.secret_key = 'some secret key'

# WILL LINK THESE LATERS RIGHT NOW JUST FOR IMAGE REFERENCE FOR SDD and 
#login and createaccount are commented out while I work on other stuff

@app.route('/', methods=['GET', 'POST'])
def loginPage():
    pageType = backend.userClass
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        try:
            with sqlite3.connect('System_Data.db') as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT tuID, password FROM User_Account WHERE tuID=? and password=?", (id, password))
                result = cursor.fetchall()[0]
            return render_template('homepageLayout.html', pageType=pageType)
        except:
            flash('Incorrect id or password. Try Again')
            return render_template('login.html', pageType=pageType)
    return render_template('login.html', pageType=pageType)


@app.route('/CreateAccount', methods=['GET', 'POST'])
def createAcctPage():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        first = name.split(' ')[0]
        last = name.split(' ')[1]
        with sqlite3.connect('System_Data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO User_Account values(?, ?, ?, ?, ?, ?)",
                               (id, password, first, last, email, ''))
            conn.commit()
    return render_template('createAccount.html')


@app.route('/UpdatePassword', methods=['GET', 'POST'])
def updatePasswordPage():
    pageType = backend.userClass
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        new_password = request.form['new_password']
        new_password2 = request.form['new_password2']
        if new_password == new_password2:
            with sqlite3.connect('System_Data.db') as conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("SELECT tuID, password FROM User_Account WHERE tuID=? and password=?",
                                   (id, password))
                    cursor.fetchall()
                except:
                    flash('Id does not exist')
                cursor.execute("UPDATE User_Account SET password=? WHERE tuID=?", (new_password, id))
                conn.commit()
        else:
            flash('New password does not match repeat new password. Try Again')
    return render_template('updatePassword.html', pageType=pageType)

@app.route('/MyProfile')
def profilePage():
    pageType=backend.userClass
    id = '8'
    with sqlite3.connect('System_Data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Profile WHERE tuID=?", (id))
        result = cursor.fetchall()[0]
    userMajor = result[1]
    userClubs = result[2]
    userGradYear = result[3]
    return render_template('myProfile.html', userMajor = userMajor, userClubs= userClubs, userGradYear=userGradYear, pageType=pageType )

@app.route('/MyWorkRecord')
def workRecordPage():
    pageType = backend.userClass
    id = '1'
    with sqlite3.connect('System_Data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Work_Record WHERE tuID=?", (id))
        result = cursor.fetchall()[0]
        hours = result[1]

    return render_template('/workRecord.html', pageType=pageType, id=id, hours=hours)

@app.route('/Home')
def homepage():
    pageType = backend.userClass
    calMonth = backend.month
    return render_template('homepageLayout.html', pageType = pageType, calMonth=calMonth)


@app.route('/BecomeATutor')
def becomeATutorPage(): 
    pageType = backend.userClass
    return render_template('becomeATutor.html', pageType=pageType)

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

@app.route('/ManageTutoringFacilities')
def manageFacilPage(): 
    pageType = backend.userClass
    
    return render_template('/manageFacil.html', pageType=pageType)

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
