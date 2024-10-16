"""This code will add users from userslist to server, automatically.
    if user is already available then it will print user already exist
    otherwise it will add users from the list one by one."""

"""I am using os.system(id) function to check if that user is present in the server or not,
    if it is present return code will be 0 other wise it will be a random number
    so we are checking only for returncode (exit code) from os.system(id) is a non zero"""

#!/usr/bin/python3

import os
import time

userslist = ["nkumar","rgvarma","vsharma","msingh"] #Variable declaring list of users

print("Adding users from the list to server")
print("*************************************")

#Loop to add users one by one to server

for user in userslist: #for loop to add users one by one
    returncode = os.system("id {}".format(user))
    #Assigning a variable to os.system(id) shell code, and for loop sends each user to .format(user)
    # and that will send to id (user) to check if user exists or not

    if returncode != 0: #If user is available return code will be 0, and it will skip adding users
        print(f'User {user} does not exist, Adding Now')
        os.system("useradd {}".format(user))
        #Above line will add users which are not available, i.e. if return code is non 0.
        time.sleep(1)  # Wait for 1 second between users to add.
        print(f'User {user} has been added successfully')
    else:
        print(f'User {user} already exist')