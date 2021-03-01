readIP = "127.0.0.1"
readPORT = "8085"
readBUFFER_SIZE = 1024

import socket
from tkinter import *

class interface:
    def __init__(self):
        sock = socket.socket ( socket.SOCK_DGRAM )
        sock.bind ( ('', int ( readPORT )) )
        sock.connect ( (readIP, int ( readPORT )) )

        win = Tk()
        win.title('Receiver')
        win.iconbitmap('imgs/icon_16x16.ico')
        text = Text(win)
        def printToTk (string): text.insert ( END, f'\n{string}' )
        text.pack()
        win.mainloop()
        while True:
            data, addr = sock.recvfrom ( int ( readBUFFER_SIZE ) )  # buffer size is 1024 bytes
            printToTk ( "received message: %s" % data )


try:
    interface()
except TclError:
    print(' A TclError occured. This is most likely because of the GUI being closed whilst checking the ip.')