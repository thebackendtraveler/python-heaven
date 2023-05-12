import schedule
import os
import time
import requests

#the function that displays the welcome text
def display_welcome():
    print(welcome_text)

#The function that opens the browser
def open_browser():
    os.system("open - a firefox http://www.noroff.no")

#Open the welcome.txt and reading its contents
welcome = open("C:\\MyScripts\Module 5\Welcome.txt", "r")
welcome_text = welcome.read()
welcome.close()

#Schedule the tasks
schedule.every().monday.at("08:00").do(display_welcome)
schedule.every().tuesday.at("08.00").do(display_welcome)
schedule.every().wednesday.at("08:00").do(display_welcome)
schedule.every().thursday.at("08:00").do(display_welcome)
schedule.every().friday.at("08:00").do(display_welcome)
schedule.every(1).hour.do(open_browser)

continue_loop = True

try: 
    # Since continue_loop is set to True the loop will
    # continue indefinitely.  If anything goes wrong
    # the except statement sets continue_loop to False to
    # gracefully end the script execution.
    while continue_loop:
        # Tells the scheduler to run any outstanding
        # tasks.
        schedule.run_pending()
        # Makes the current thread sleep (pause) for 1
        # second.  This ensures that the run_pending()
        # method is only called once every second.
        time.sleep(1)
except: 
    continue_loop = False
    print("Scheduler stopped")

