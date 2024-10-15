import csv
from datetime import datetime
import sqlite3
import time
import pyfiglet
import chime

def main():

    # Render welcome message using Figlet
    welcome_msg = pyfiglet.figlet_format("Pomodoro App!", font="slant")
    print(welcome_msg)

    # Get the user input for duration of breaks and pomodoro and no of sessions
    duration_of_pomodoro, pomodoro_tag, duration_of_break, no_of_sessions = get_user_input()

    # Initilize the SQLite db
    conn = db_initialization()

    #Start the pomodoro sessions
    pomodoro(conn, duration_of_pomodoro, duration_of_break, no_of_sessions, pomodoro_tag)

    # Close the DB connection
    conn.close()

##########################################    
 ###### Database related functions ######
##########################################

def db_initialization():
    '''
    Initialize the SQLite database

    Args: none

    Returns:
        sqlite3.Connection : Returns the connection object to the database
    '''
    conn = sqlite3.connect("pomodoro_sessions.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions  (
                   id INTEGER PRIMARY KEY,
                   session_date TEXT,
                   session_number INTEGER,
                   tag TEXT
                   )
                   ''')
    conn.commit()
    return conn

def update_session(conn, session_number, pomodoro_tag):
    '''
    Save the session data into the SQLite db.

    Args:
        sqlite.connection, int: take 2 arguments, sqlite connection object to the sql db and current session number
    
    Returns:
        none
    '''
    
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sessions (session_date, session_number, tag)
        VALUES (?, ?, ?)
        ''', (datetime.now().strftime("%Y-%m-%d"), session_number, pomodoro_tag))
    conn.commit()


def export_csv(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM sessions WHERE session_date = ?
    ''', (datetime.now().strftime("%Y-%m-%d"),))

    rows = cursor.fetchall()

    with open(f'pomodoro_report_{datetime.now().strftime("%Y-%m-%d")}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Date', 'Session Number', 'Tag'])
        writer.writerows(rows)



################################################
###### User operations related functions ######
################################################


def get_user_input():
    '''
    Get the following input from users in integers:
        - Work session duration in minutes
        - Break session duration in minuttes
        - No of pomodoro sessions.

    Args: none

    Returns:
        Integers: duration_of_pomodoro, duration_of_break, no_of_sessions

    '''
        
    duration_of_pomodoro = input_validation("Enter work session duration in Minutes: ")
    pomodoro_tag = input("Tag your pomodoro session(Optional): ")
    duration_of_break = input_validation("Enter break session duration in Minutes: ")
    no_of_sessions = input_validation("Enter the number of Pomodoro sessions: ")

    return duration_of_pomodoro, pomodoro_tag, duration_of_break, no_of_sessions



def input_validation(prompt):
    '''
    Checks if user input is integer and greater than 0

    Args:
        string: user_input prompt
    
    Returns:
        Integer: If user input is valid then true else false
    '''

    while True:
        try:
            user_input = int(input(prompt))

            if user_input > 0:
                return user_input
            
            raise ValueError
        except ValueError:
            print("//Invalid input. Value should be positive integer.")

def countdown(minutes):
    '''
    Displays a timer on the terminal with user input minutes

    Args:
        int: minutes in integers
    
    Returns:
        none
    '''

    # Change minutes into seconds
    seconds = minutes * 10

    # Display the timer till the seconds turns to 0
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        
        print(timer, end="\r")

        time.sleep(1)
        seconds -= 1

def notify(message, chime_sound="info"):
    '''
    Prints the message on the screen with a chime sound 
    '''
    chime.theme = 'material'
    print(message)

    if chime_sound == 'success':
        chime.success()
    else:
        chime.info()
    print()
    

def pomodoro(conn, duration_of_pomodoro, duration_of_break, no_of_sessions, pomodoro_tag=""):
    '''
    Calls the countdown function for work durations and break duration for number of sessions

    Args:
       sqlite.connection, str, int, int, int
    
    Returns:
        none
    '''

    for session in range(1, no_of_sessions + 1):
        print(f"Pomodoro session: [{pomodoro_tag}-{session}] ")

        # Work session
        notify("##### Work sessions starts! ⏰ #####", "success")
        time.sleep(1)
        countdown(duration_of_pomodoro)

        # Notify user for break with sound
        notify("##### Work session ends! 🛑 #####", "success")

        # Save the session in the SQLite Database
        update_session(conn, session, pomodoro_tag)
        time.sleep(1)

        # Break session
        notify("##### Break session starts! 🧁 #####")
        time.sleep(1)
        countdown(duration_of_break)
        notify("##### Break session ends! 🛑 #####")
        time.sleep(1)
    
    # Export to CSV
    export_csv(conn)
    notify("Congratulations!🎉  All Pomodoro sessions completed!⭐️")
        

if __name__ == "__main__":
    main()