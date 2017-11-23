# README

## Project 8: A Meeting Time App
## Authors:
#### Michal Young
#### Revised by: Keir Armstrong

#### About:
- A web app that calculates the free times in a time block in a day, or multiple days.
- Uses Oauth2 for authentication and access to the user's Google Calendar calendars and events.

#### Activation:
- In /memos create a credentials.ini file, and fill in the following variables:
    1. SECRET_KEY
    2. PORT
    3. GOOGLE_KEY_FILE
- GOOGLE_KEY_FILE is your Google Developer key file.
- After credentials.ini has been created,
enter 'make install' under the main directory to install virtual environment.
- Enter 'make start' to start the server.
- Enter 'make stop' to stop the server from running.
- Enter 'make test' to run test cases.