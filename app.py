"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import sqlite3
from flask import Flask, render_template, request, redirect, flash
import backend
import calendar
import os
from flask_ngrok import run_with_ngrok

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


@app.route('/Home')
def homepage():
    pageType = backend.userClass
    calMonth = backend.month
    return render_template('homepageLayout.html', pageType = pageType, calMonth=calMonth)

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
    userGradYear = result[2]
    userClubs = result[3]
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

@app.route('/BecomeATutor', methods=['GET', 'POST'])
def becomeATutorPage(): 
    pageType = backend.userClass
    if request.method == 'POST':
        tuID = request.form['tuID']
        first_name = request.form['name'].split(' ')[0]
        last_name = request.form['name'].split(' ')[-1]
        email = request.form['email']
        subject = request.form['subject']
        location = request.form['location']
        with sqlite3.connect('System_Data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Tutor_Application values(?, ?, ?, ?, ?)",
                           (tuID, first_name, last_name, email, subject))
            cursor.execute("INSERT INTO Tutor_Account values(?, ?, ?)",
                           (tuID, subject, location))
            cursor.execute("INSERT INTO Tutor_Account values(?)", (tuID,))
            conn.commit()
    return render_template('becomeATutor.html', pageType=pageType)

@app.route('/TutoringApplications',  methods=['GET', 'POST'])
def viewTutAppsPage():
    pageType = backend.userClass
    with sqlite3.connect('System_Data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, tuID, email FROM Tutor_Application")
        result = cursor.fetchall()

    return render_template('viewTutApps.html', pageType=pageType, options=result)

@app.route('/ApplicationDetail/<TUid>', methods=['GET', 'POST'])
def viewAppDetailsPage(TUid):
    pageType = backend.userClass
    # tuid = request.args.get('TUid')

    with sqlite3.connect('System_Data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT first_name,last_name,email,tuID FROM Tutor_Application
                        WHERE tuID = ?""", (TUid,))
        result = cursor.fetchall()[0]
        fullname = [result[0], result[1]]
        email = result[2]
        tuID = result[3]
        name = " ".join(fullname)

    return render_template('tutAppDetail.html', pageType=pageType, applicantName=name,
                           applicantID=tuID, applicantRecLetter='applicantRecLetter',
                           applicantEmail=email)

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

@app.route('/SystemInfo')
def viewSystemInfoPage(): 
    pageType = backend.userClass
    return render_template('systemInfo.html', pageType=pageType)

@app.route('/AdminManagement', methods=['GET', 'POST'])
def adminMmgtPage():
    pageType = backend.userClass
    if request.method == 'POST':
        id = request.form['id']
        with sqlite3.connect('System_Data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT tuID, email FROM User_Account where tuID = ?", (id))
            result = cursor.fetchall()
            try:
                result = result[0]
                email = result[1]
                flash(f'User found: {email}')
            except:
                flash('User not found')

    return render_template('adminMmgt.html', pageType=pageType)

@app.route('/ManageTutors')
def tutMmgtPage():
    pageType = backend.userClass
    with sqlite3.connect('System_Data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT first_name,last_name,email,tuID FROM Tutor_Application")
        result = cursor.fetchall()[0]
        fullname = [result[0], result[1]]
        email = result[2]
        name = " ".join(fullname)

    return render_template('tutMmgt.html', name=name, email=email, pageType=pageType)

@app.route('/WeeklyView')
def weeklyApptViewPage(): 
    pageType = backend.userClass
    calMonth = backend.month
    return render_template('/weeklyView.html', pageType=pageType, calMonth=calMonth)
   
@app.route('/FindATutor', methods=['GET', 'POST'])
def tutorSelctPage(): 
    pageType = backend.userClass
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        first_name = name.split[' '][0]
        last_name = name.split[' '][1]
        with sqlite3.connect('System_Data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT first_name,last_name,email,tuID,subject FROM Tutor_Application
                            where first_name=? and last_name and subject=?""", (first_name,last_name,subject))
            result = cursor.fetchall()[0]
            fullname = [result[0], result[1]]
            name = " ".join(fullname)
            email = result[2]
            tuID = result[3]
            subject = result[4]


    
    return render_template('/tutorSelect.html', name=name, email=email, tuID=tuID, subject=subject, pageType=pageType)

@app.route('/ScheduleAppointment')
def schedApptPage(): 
    pageType = backend.userClass
    calMonth=backend.month
    
    return render_template('/schedAppt.html', calMonth=calMonth, pageType=pageType)

@app.route('/TutorLocationAssignment/<name>')
def tutLocationAssignmetPage(name):
    pageType = backend.userClass
    return render_template('/tutAssignment.html', pageType=pageType, name=name)

@app.route('/MyTutoringAvailability')
def tutAvailabilityPage(): 
    pageType = backend.userClass
    
    return render_template('/tutAvailability.html', pageType=pageType)

@app.route('/EditDaily', methods=['GET', 'POST'])
def editDailyAvailabilityPage(): 
    pageType = backend.userClass
    if request.method == "POST":
        day = request.form['day']
        start_time = request.form['starttime']
        end_time = request.form['endtime']
        with sqlite3.connect('System_Data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Daily_Availability values(?, ?, ?)",
                           (day,start_time,end_time))
            conn.commit()
            cursor.execute("""SELECT day_tutor_avail, avail_from, avail_to FROM Daily_Availability""")
            result = cursor.fetchall()
        return render_template('/dailyAvail.html', pageType=pageType, options=result)
    return render_template('/dailyAvail.html', pageType=pageType)

@app.route('/EditBlackoutDates', methods=['GET', 'POST'])
def editBlackoutDatesPage(): 
    pageType = backend.userClass
    if request.method == "POST":
        date = request.form['date']
        with sqlite3.connect('System_Data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Blackout_Dates values(?)",
                           (date,))
            conn.commit()
            cursor.execute("""SELECT blackout_date FROM Blackout_Dates""")
            result = cursor.fetchall()
        return render_template('/blackoutAvail.html', pageType=pageType, options=result)
    
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
    app.run(debug=True, port=8000)
