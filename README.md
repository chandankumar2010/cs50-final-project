# Pomodoro technqiue

    #### Video Demo:  <URL HERE>

    #### Description:

        Pomodoro technique: The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s.[1] It uses a kitchen timer to break work into intervals, typically 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato, after the tomato-shaped kitchen timer Cirillo used as a university student.
        
        https://en.wikipedia.org/wiki/Pomodoro_Technique

        This project implements the Pomodoro technique using python. The program asks user for following:
        a. Duration of pomodoro(interval of work time)
        b. Number of pomodoro
        c. Duration of break

        After getting the desired inputs from the user, program starts the timer with a "Message" printed on the terminal. After work time expires, program prints again prints a message on the terminal and generates a notification sound; alerting user for the timer expiry and start of the break tiner.

        Once break timner expires, again a message and a sound notification is generated to alert the user.

        After all pomodori are complete, program generates a CSV report of the pomodori completed.

    ### Design Choice:
        SQLite + CSV vs Only CSV
            Initially program was exporting the report only in CSV.
            Later on SQLite was added to account for scalability and strucute to the data
    
    ### How to use the program
