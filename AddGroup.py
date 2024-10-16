#!/usr/bin/python3

import os

check = os.system("grep devops /etc/group")
if check !=0:
    print("group devops does not exist, Adding it")
    os.system("groupadd devops")
else:
    print("devops group already exist, Skipping it")
