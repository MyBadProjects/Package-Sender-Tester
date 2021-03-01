"""
Please do not use this tool for malicious purposes.
This is designed for debugging and testing.

This was made by MyBadProjects
"""

import json
import secrets
import socket
import string
import sys
from datetime import datetime

"""
Load logger
"""
sys.stdout = open (
    f"log-{str ( datetime.now () ).split ( '.' )[0].replace ( '-', '_' ).replace ( ':', '-' )}.txt",
    'w'
)
print ( 'Loaded logger' )

"""
Add debug_write and toggle debug
"""
debug = True

if debug:
    print ( '\nDebug is on.\n' )
else:
    print ( '\nDebug is off.\n' )


def debug_write(debug_string_input):
    if debug:
        print ( f'INFO: {debug_string_input}' )
    else:
        return None


"""
Console Toggle
"""
console_toggle = True

"""
GUI Stuff
"""
from tkinter import *
from tkinter.ttk import *


class interface:
    def __init__(self):
        # log load
        debug_write ( 'Loading GUI from class' )

        # log version
        debug_write ( f'Tkinter Version: {TkVersion}' )

        # create the window
        win = Tk ()

        # change window settings
        win.title ( "Packet Tester" )
        win.maxsize ( 250, 650 )
        win.minsize ( 250, 560 )
        win.resizable ( False, False )
        win.iconbitmap ( 'imgs/icon_16x16.ico' )

        # attach on_close event
        def on_closing():
            debug_write ( 'Closing GUI from class' )
            win.destroy ()

        win.protocol ( "WM_DELETE_WINDOW", on_closing )

        # method
        methodFrame = Frame ()
        methodFrame.pack ()

        lMethod = Label (
            methodFrame,
            text=f'Method',
            font=("Arial", 16)
        )
        lMethod.pack ()

        OPTIONS = [
            "UDP",
            "Internet"
        ]

        variable = StringVar (
            methodFrame
        )
        variable.set (
            OPTIONS[0]
        )

        methodOptions = Combobox (
            methodFrame,
            values=OPTIONS,
            state='readonly'
        )

        methodOptions.pack ()

        # details
        detailsFrame = Frame ()
        detailsFrame.pack ()

        lDetails = Label (
            detailsFrame,
            text="\nDetails",
            font=(
                "Arial",
                16
            )
        )
        lDetails.pack ()

        lIP = Label (
            detailsFrame,
            text="IP",
            font=(
                "Arial",
                10
            )
        )

        lIP.pack ()

        inputIP = Entry (
            detailsFrame
        )

        inputIP.pack ()

        lPort = Label (
            detailsFrame,
            text="\nPort",
            font=(
                "Arial",
                10
            )
        )

        lPort.pack ()

        inputPort = Entry (
            detailsFrame
        )

        inputPort.pack ()

        # packets

        packetsFrame = Frame ()
        packetsFrame.pack ()

        lPackets = Label (
            packetsFrame,
            text="\nPackets",
            font=(
                "Arial",
                16
            )
        )

        lPackets.pack ()

        lAmoutPackets = Label (
            packetsFrame,
            text="Amount of Packets to send",
            font=(
                "Arial",
                10
            )
        )

        lAmoutPackets.pack ()

        inputPackets = Entry (
            packetsFrame
        )

        inputPackets.pack ()

        lLength = Label (
            packetsFrame,
            text="\nLength of string to send",
            font=(
                "Arial",
                10
            )
        )

        lLength.pack ()

        inputLength = Entry (
            packetsFrame
        )

        inputLength.pack ()

        # start

        startFrame = Frame ()
        startFrame.pack ()

        lStart = Label (
            startFrame,
            text="\nStart",
            font=(
                "Arial",
                16
            )
        )

        lStart.pack ()

        lStartDesc = Label (
            startFrame,
            text="\nBy click this button you accept that you are responsiable for any damages.\nMyBadProjects takes 0 "
                 "responsibility for your actions.\n",
            font=(
                "Arial",
                10
            ),
            wraplength=225,
            justify="center"
        )

        lStartDesc.pack ()

        def sendPackets():
            def getRandomString(length):
                return ''.join (
                    secrets.choice (
                        string.ascii_uppercase +
                        string.ascii_lowercase +
                        string.digits
                    ) for _ in range (
                        length
                    )
                )

            # set variables
            method = methodOptions.get ()
            ip = inputIP.get ()
            port = inputPort.get ()
            amountofpackets = int ( inputPackets.get () )
            lengthofpackets = int ( inputLength.get () )

            # format log
            settings_log = json.dumps ( {"method": method, "ip": ip, "port": port, "amountofpackets": amountofpackets,
                                         "lengthofpackets": lengthofpackets} )
            print ( settings_log )

            # start
            if method.lower () == 'internet':
                print('Sending through internet (TCP).')
                for i in range ( amountofpackets ):
                    sock = socket.socket ( socket.AF_INET )  # load socket
                    sock.bind ( ('', int ( port )) )
                    sock.connect ( (ip, int ( port )) )
                    sock.sendto ( getRandomString ( lengthofpackets ).encode ( 'utf-8' ), (ip, int ( port )) )
                    sock.close ()
                    print ( f'Sent {i}th packet.' )

            else:
                print('Sending through UDP.')
                for i in range ( amountofpackets ):
                    sock = socket.socket ( socket.SOCK_DGRAM )
                    sock.bind ( ('', int ( port )) )
                    sock.connect ( (ip, int ( port )) )
                    sock.sendto ( getRandomString ( lengthofpackets ).encode ( 'utf-8' ), (ip, int ( port )) )
                    sock.close ()
                    print ( f'Sent {i}th packet.' )

        inputStart = Button (
            startFrame,
            text="Start!",
            command=sendPackets
        )

        inputStart.pack ()

        # show the window
        debug_write ( 'Showing GUI from class' )
        win.mainloop ()

        debug_write ( 'Closed GUI from class' )


"""
Load interface
"""
debug_write ( 'Loading GUI Class' )
interface ()  # Load interface
debug_write ( 'GUI Class Closed\nClosing logger' )
sys.stdout.close ()  # Close logger, this will not stop until the interface is closed due to win.mainloop