import subprocess

# List of users to add
userlist = ["nkumar", "pkumar", "rkumar"]
print("Adding users to System")

# Loop to add user from userlist
for user in userlist:
    # Check if the user exists using net user command
    try:
        # Run the command to check if user exists
        exitcode = subprocess.call(f"net user {user}", shell=True)
        if exitcode != 0:
            print(f"User {user} does not exist. Adding it.")
            # Adding the user
            subprocess.call(f"net user {user} /add", shell=True)
        else:
            print(f"User {user} already exists, checking next user.")
    except Exception as e:
        print(f"An error occurred: {e}")
