#!/usr/bin/python3
import os
path = "/opt/python/pyscripts"
if os.path.exists(path):
    print("Script(s) directory exists")
elif os.path.isfile(path):
    print("Script(s) dir does not exist")