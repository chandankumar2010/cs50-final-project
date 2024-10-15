import time

def countdown(minutes):
    '''
    Displays a timer on the terminal with user input minutes

    Args:
        int: minutes in integers
    
    Returns:
        none
    '''

    # Change minutes into seconds
    seconds = minutes * 60

    # Display the timer till the seconds turns to 0
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
    
        print(timer, end="\r")

        time.sleep(1)
        seconds -= 1

countdown(1)