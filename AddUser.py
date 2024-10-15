#!/usr/bin/python3

import os
import time
userslist = ["nkumar","rgvarma","vsharma","msingh"] #Variable declaring list of users

print("Adding users from the list to server")
print("*************************************")

#Loop to add users one by one to server

for user in userslist:
    returncode = os.system("id {}".format(user))
    if returncode != 0:
        print(f'User {user} does not exist, Adding Now')
        os.system("useradd {}".format(user))
        time.sleep(1)  # Wait for 1 second between users
        print(f'User {user} has been added successfully')
    else:
        print(f'User {user} already exist')