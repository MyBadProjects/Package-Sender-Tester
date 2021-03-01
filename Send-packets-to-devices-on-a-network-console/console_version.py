"""
Please use the GUI interface version.
It is better and easier to use.

Please do not use this tool for malicious purposes.
This is designed for debugging and testing.

This was made by MyBadProjects
"""

import os
import socket
import secrets
import string


def getrandomstring(amount):
    return ''.join (
        secrets.choice (
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits
        ) for _ in range (
            amount
        )
    )


def ip4addresses():
    # get ips
    base = [
        i[4][0]
        for i in socket.getaddrinfo (
            socket.gethostname (),
            None
        )]
    return base[len ( base ) // 2:]


def q1():
    # get ip
    print ( 'Detected IP Addresses: ' )
    for i in ip4addresses ():
        print ( i )
    ip = input ( '\nType in the IP Address you want to send packets to.\nIf it is not there still type it in. ' )

    # ping ip
    print ( 'Attempting to ping ip...\n' )
    if os.system ( f"ping {ip}" ) == f'Ping request could not find host {ip}. Please check the name and try again.':
        print ( 'Failed to ping ip' )
    else:
        print ( 'Successfully pinged ip.' )

    # get packets to send
    packets = q2 ()

    # get packet contents
    amountofjunk = q3 ()

    print ( f'Sample of packet: {getrandomstring ( amountofjunk )}' )

    # get port
    port = q4 ()

    # get mode
    mode = q5 ()

    # ask if sure
    answers_sure = ['yes', 'y', 'true']
    sure = input ( 'Do you want to continue? [Yes or No] ' ).lower ()

    valid = False
    for i in answers_sure:
        if i == sure:
            valid = True

    if valid:
        if mode == 'internet':
            for i in range ( packets ):
                sock = socket.socket ( socket.AF_INET )
                sock.bind ( ('', port) )
                sock.connect ( (ip, port) )
                sock.sendto ( getrandomstring ( amountofjunk ).encode ( 'utf-8' ), (ip, port) )
                sock.close ()
                print ( f'Sent {i}th packet.' )
        else:
            for i in range ( packets ):
                sock = socket.socket ( socket.SOCK_DGRAM )
                sock.bind ( ('', port) )
                sock.connect ( (ip, port) )
                sock.sendto ( getrandomstring ( amountofjunk ).encode ( 'utf-8' ), (ip, port) )
                sock.close ()
                print ( f'Sent {i}th packet.' )
    else:
        print('Canceled.')


def q2():
    return int ( input ( 'How many packets do you want to send? ' ).lower () )


def q3():
    return int ( input ( 'How much random string do you want to send in the packet?' ) )


def q4():
    return int ( input ( 'What port do you want to send the packets to?' ) )


def q5():
    answers = ['udp', 'internet']
    output = input ( 'Do you want to use UDP or Internet?' ).lower ()
    valid = False
    for i in answers:
        if output == i:
            valid = True

    if valid:
        return valid
    else:
        return q5 ()

q1()