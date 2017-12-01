# README

## Project 10: Event Scheduler Web App
## Authors:
#### Michal Young
#### Revised by: Keir Armstrong

#### About:
- Ever wished you had an easier time to find the perfect time slot for your gathering between friends?
Wish no more, with this web app you won't headache over all the complicated calculation anymore,
 the app will do all the work for you!
- How does it work, exactly?
- Event Scheduler uses Google Calendar API to simulate a time table, which means it pulls calendar events 
from your friends' Google calendars, to estimate the availability times. Once everyone you want has participated and 
the calculations are done, you will be give a list of 
choices to decide the perfect time, or not, for the meeting.

#### Activation:
- In /letsmeet create a credentials.ini file, and fill in the following variables:
    1. SECRET_KEY
    2. PORT
    3. GOOGLE_KEY_FILE  (name of the JSON file)
    4. DB_USER  (You should use MongoDB for maximum compatibility)
    5. DB_USER_PW
    6. DB_HOST
    7. DB_PORT
    8. DB 
    DB_USER = karmstr7
- Then, enter 'make install' under the main directory to install virtual environment
- Enter 'make start' to start the server
- Enter 'make stop' to stop the server from running
- Enter 'make test' to run test cases
