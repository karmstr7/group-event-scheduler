# Group Event Scheduler Web App
Make planning and scheduling the next get-together with a group of people a more seamless experience.

## Project repository:
https://github.com/keirarmstrong/group-event-scheduler

## Description:
By leveraging the ubiquitous use of Google Calendar, scheduling group hangouts has never been easier. The idea is to use Google Calendar API to import events and busy times of individuals who already use Google Calendar.

#### How to use
Begin by clicking the "Schedule a Meeting" button to provide either - the username and password of your Google account
       - or the username of another Google user 
to allow the app's access to Google Calendar contents. The app only stores the begin and end times of a user's events in their calendar, it does not store anything else beyond the time intervals. Then, a pop-up will appear to ask you to confirm granting permission, or signal to wait for permission to be granted. Multiple calendars from any number of Google accounts can be added, at anytime. Once a schedule has been created, it is stored in the database and it is linked to a session ID. Others may access the unique schedule by using its session ID.       

#### Technical stack
- Languages: Python, MongoDB, JavaScript, HTML, CSS, make
- Base Dependencies/Libraries: arrow, Flask, google-api-python-client, oauth2client, httplib2, urllib3, pymongo
- Additional technologies: Microsoft Azure

#### Required custom values:
- In /letsmeet create a credentials.ini file, and fill in the following variables:
    1. SECRET_KEY
    2. PORT
    3. GOOGLE_KEY_FILE  (name of the JSON file to access Google Calendar API)
    4. DB_USER  (You should use MongoDB for maximum compatibility)
    5. DB_USER_PW
    6. DB_HOST
    7. DB_PORT
    8. DB
  
 #### For Unix, Linux
- Then, enter 'make install' under the main directory to install virtual environment
- Enter 'make start' to start the server
- Enter 'make stop' to stop the server from running
- Enter 'make test' to run test cases
