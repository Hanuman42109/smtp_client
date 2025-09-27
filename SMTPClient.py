from socket import *
import ssl
import base64

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 587)

# Sender and receiver details
sender = "chanukyasrinivas99@gmail.com"
password = "iwtzbrkuxuzrxhhl"  # Use an App Password, not your actual password
recipient = "chanukyachilamkuri@gmail.com"
subject = "SMTP Client Test Email"
msg = "\r\nTest Email:\r\n\r\nI love computer networks! It is so cool!"
endmsg = "\r\n.\r\n"

# Create socket called clientSocket and establish a connection with mailserver
# #Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# #Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO example.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send STARTTLS command
starttlsCommand = "STARTTLS\r\n"
clientSocket.send(starttlsCommand.encode())
recv_tls = clientSocket.recv(1024).decode()
print(recv_tls)
if recv_tls[:3] != '220':
    print("220 reply not received from server (TLS).")

# Wrap socket with SSL
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname='smtp.gmail.com')

# Send HELO again after TLS handshake
clientSocket.send(heloCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# AUTH LOGIN
authCommand = "AUTH LOGIN\r\n"
clientSocket.send(authCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send username (Base64 encoded)
clientSocket.send(base64.b64encode(sender.encode()) + b'\r\n')
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send password (Base64 encoded)
clientSocket.send(base64.b64encode(password.encode()) + b'\r\n')
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = f"MAIL FROM:<{sender}>\r\n"
clientSocket.send(mailFrom.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = f"RCPT TO:<{recipient}>\r\n"
clientSocket.send(rcptTo.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
# Fill in end

# Send message data.
# Fill in start
message = f"Subject: {subject}\r\n\r\n{msg}\r\n.\r\n"
clientSocket.send(message.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv10 = clientSocket.recv(1024).decode()
print(recv10)
# Fill in end

clientSocket.close()
print("\n✅ Email sent successfully!")