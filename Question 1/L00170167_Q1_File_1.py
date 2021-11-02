"""
#
# File          :   L00170167_Q1_File_1.py
# Created       :    
# Author        :   Derek Troy
# Version       :   1.0.0
# Licensing     :   (C) 2021 Derek Troy LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Question 1 - Create an SSH Connection to a VM
#
"""
# import paramiko module
import paramiko

# configure the login details
hostname = "192.168.1.60"
username = "test"
password = "letterkenny"

# initialize the SSH client
client = paramiko.SSHClient()

# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the server, if connected print, if fails print other statement
try:
    client.connect(hostname=hostname, username=username, password=password)
    print("Connected to: ", hostname)

except:
    print("[!] Cannot connect to", hostname)
    exit()
