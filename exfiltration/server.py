import socket

# Create Socket
host = socket.gethostname()
port = 12000
s = socket.socket()
s.bind((host,port))
s.listen(5)

# Accept Client Connection
print("Waiting for client...")
conn,addr = s.accept()	        # Accept connection when client connects
print("Connected by " + addr[0])

# Print Client Data
while True:
	data = conn.recv(1024)	    # Receive client data
	if  data:
		plaintext = data.decode('utf-8')
		print(plaintext)
		if plaintext == 'commit sudoku':
			s.close
			break