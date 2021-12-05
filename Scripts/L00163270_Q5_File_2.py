# --------------------
# File      : .py
# Created   : 04-12-2021 {TIME}
# Author    : Sreejith
# Version   : v1.0.0.
# Licensing : (C) 2021  Sreejith , LYIT
#             Available under  GNU Public License (GPL)
# Description :
# --------------------
import time
import re
import paramiko

IP = '192.168.206.128'


def ssh_connection():
    """Function to open SSH connection to the device"""

    try:
        print( "Establishing a connection..." )
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        session.connect(IP, username='l00163270', password='Somno@123' )
        session.exec_command( "sudo -S apt-get install curl" )

        connection = session.invoke_shell()
        connection.send( "mkdir labs\n" )  # unix command to list
        connection.send('mkdir labs/lab1\n')
        connection.send('mkdir labs/lab2\n')
        time.sleep( 1 )
        vm_output = connection.recv( 65535 )
        print( vm_output )
        if re.search( b"% Invalid input", vm_output ):
            print( "There was an error on vm {}".format( IP ) )
        else:
            print( "Commands successfully executed on {}".format( IP ) )
        session.close()
    except paramiko.AuthenticationException:
        print( "Authentication Error" )
        ssh_connection()
    except Exception as err:
        print( err )


if __name__ == '__main__':
    ssh_connection()
