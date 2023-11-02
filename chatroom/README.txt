This is the implementation of a keylogger within my COMP3331 project. It's
essentially a chatroom application where the client-side of the application
is being logged by the server-side.

HOW TO RUN

You need to start an instance of the server and a client (or two for maximum immersion)

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