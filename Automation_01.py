"""This automation adds list of mentioned users to server and creates
    a group add users to that new group, also a new directory will be
    created and give user ownership to that directory"""

#!/usr/bin/python3

import os
import time

userslist = ["nkumar", "rgvarma", "vsharma", "msingh"]  # List of users

print("Adding users from the list to the server")
print("*************************************")
print()
# Function to check if the devops group exists and create it if not
def check_and_create_group(groupname):
    # Check if the group exists by running 'getent group'
    group_check_cmd = f"getent group {groupname}"
    retcode = os.system(group_check_cmd)

    if retcode != 0:
        # If the return code is non-zero, the group does not exist, so we create it
        print(f"Group {groupname} does not exist. Creating the group.")
        print()
        os.system(f"groupadd {groupname}")
        print(f"Group {groupname} has been created successfully.")
        print()
    else:
        print(f"Group {groupname} already exists.")


# Function to check if a user is in a specified group and add them if not
def check_user_in_group(user, groupname):
    # Command to check if the user is in the specified group
    cmd = f"id {user} | grep -w {groupname}"
    retcode = os.system(cmd)

    if retcode == 0:
        # If the retcode is 0, the user is already in the group
        print(f"User {user} is already in group {groupname}")
    else:
        # If the retcode is non-zero, the user is not in the group
        print(f"Adding {user} to group {groupname}")
        print()
        os.system(f"usermod -aG {groupname} {user}")
        print(f"User {user} has been added to group {groupname}")


# Check if the 'devops' group exists, and create it if not
    check_and_create_group('devops')

# Loop through the list of users
for user in userslist:
    # Check if the user exists by using the `id` command
    returncode = os.system("id {}".format(user))

    if returncode != 0:  # If the user does not exist (non-zero return code)
        print(f'User {user} does not exist, Adding Now')
        os.system("useradd {}".format(user))  # Add the user
        time.sleep(1)  # Wait for 1 second
        print(f'User {user} has been added successfully')
    else:
        print(f'User {user} already exists')

    check_user_in_group(user, 'devops')

# Now check if the "devops_projects" directory exists, if not exist then create
    if os.path.isdir("/opt/devops_projects"):
        print("devops_projects directory already exists")
        print()
    else:
        os.mkdir("/opt/devops_projects")
        print("devops_project directory has been created")
        print()

#Give permission to devops group and give 770 permission
    #Chmod 770(chmod a + rwx, o - rwx) sets permissions so that,
    #(U)ser/owner can read, write & execute.
    #(G)roup can read, write & execute.
    #(O)thers can't read, write and execute.

    print("Assigning group permission and ownership to the directory")
    print()
    os.system("chown :devops /opt/devops_projects")
    os.system("chmod 770 /opt/devops_projects")
    print("Necessary permission and ownership has been set to the directory")