# --------------------
# File      : .py
# Created   : 17-11-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------

import paramiko
import time
import re


# Open SSH connection to the device
def ssh_connection(ip):
    try:
        username = "l00163270"  # In an automation script read data from file
        password = "Somno@123"  # never hard code
        print("Establishing a connection."
              "..")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, port=22, username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n")  # unix command to list
        time.sleep(1)
        vm_output = connection.recv(65535)
        print(vm_output)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")
        ssh_connection("192.168.206.128")
    except Exception as err:
        print(err)


ssh_connection('192.168.206.128')












