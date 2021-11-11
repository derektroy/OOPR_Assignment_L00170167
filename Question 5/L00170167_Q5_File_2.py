"""
#
# File          :   L00170167_Q5_File_2.py
# Created       :    
# Author        :   Derek Troy
# Version       :   1.0.2
# Licensing     :   (C) 2021 Derek Troy LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Connect to Remote Host, Create Dirs and Install Curl
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
    connection = client.invoke_shell()
    client.exec_command("mkdir Labs\n")
    client.exec_command("mkdir Labs/lab1\n")
    client.exec_command("mkdir Labs/lab2\n")
    client.exec_command("echo letterkenny | sudo -S apt install -y curl\n")
    stdin, stdout, stderr = client.exec_command("ls -l --time=atime")
    for line in iter(stdout.readline, ""):
        print(line, end="")
    print('finished.')
except:
    print("[!] Cannot connect to", hostname)
    exit()