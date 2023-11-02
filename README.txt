### BIGNOTE ###
You might need to make an exception to this folder for your security software. The lower level python
scripts contain key words which are likely to be picked up by their filters.

This explains how to use the chatroom and extension keylogger implementations

### CHATROOM ###
This is the implementation of a keylogger within my COMP3331 project. It's
essentially a chatroom application where the client-side of the application
is being logged by the server-side.

HOW TO RUN

You need to start an instance of the server and a client (or two for maximum immersion)
cd into the chatroom folder first and start the instances.
Server
python3 server.py 12000 30 900

Client 
python3 client.py 12000

Once the client is logged on, you can try sending a message via "broadcast {message}"
Anything that the client types including outside of terminal will be logged in keylog.txt which is
written serverside.

HOW IT WORKS
There is a local keylogger on the client application. Since the client is connected to the server
through a forwarded socket, we can also send this logged data through the socket alongside any messages.

Note: It's not quite real time logging. The log gets updated whenever the client transmits to the server.
This includes broadcasting or even sending the close connection signal, so the window for keylog collection
is as long as the client is up.

### Extension ###
This is a new implementation of a keylogger hidden within an extension. The extension is built using
Javascript (and a bit of html). I also used Python Flask for a server that can record the logs
from the extension.

HOW TO RUN
Open google chrome and go onto chrome://extensions/
Click the developer mode switch on the top right and click 'load unpacked' on the top left corner.
Select the extension folder in this repo to unpack.
Run the flask server using: python3 extensiontracker.py
Go onto a few sites and start typing, you can see the flask server log your inputs.

If you want to use the easy button, it's best to pin the extension. When you click it, click the
button image to announce "that was easy"

HOW IT WORKS
The keylogger is contained in the extension itself (content.js). When the extension logs this data, 
it needs to then pass this data to the browser (background.js) which then sends a POST request to 
my flask server (extensiontracker.py). At the same time, I also have popup.js as an obfuscation 
file which provides some basic functionality to my feature, making it look like a simple "easy"
button. Both this front facing and key logging script are able to run at the same time.