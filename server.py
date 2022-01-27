import socket

HOST = "localhost"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)
print (f"Start Listing ... {HOST}:{PORT}")
client, addr = server.accept()

done = False
msg = ''
msg_send = ''

while not done:
    try:
        msg = client.recv(1024).decode('utf-8')
        if msg and msg != 'quit':
            print (f"Received: {msg}")
        else:
            client.send('quit'.encode('utf-8'))
            done = True
        msg_send = input("Message: ")
        client.send(msg_send.encode('utf-8'))
        if msg_send == 'quit':
            done = True
    except KeyboardInterrupt:
        done = True

client.close()
server.close()       