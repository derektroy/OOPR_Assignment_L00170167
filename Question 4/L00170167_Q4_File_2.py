"""
#
# File          :   L00170167_Q4_File_2.py
# Created       :    Saturday 6th Nov
# Author        :   Derek Troy
# Version       :   1.0.0
# Licensing     :   (C) 2021 Derek Troy LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Port Scanning of a remote IP
#
"""
import socket
import threading

target = "192.168.1.60"   # Which Host to Scan
def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        if port == 22:  # Return SSH if Port 22 open
            print(f"SSH is open     ")
        elif port == 25:  # Return SMTP if Port 25 open
            print(f"SMTP is open     ")
        elif port == 80:  # Return HTTP if Port 80 open
            print(f"HTTP is open     ")
        elif port == 3389:  # Return RDP if Port 3389 open
            print(f"RDP is open     ")
        else:
            print(f"{port} is open     ")
    except:
        pass


for port in range(1,5050):
    thread = threading.Thread(target =port_scanner, args=[port])
    thread.start()