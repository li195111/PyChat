import socket

HOST = "localhost"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
print (f"Start Connect ... {HOST}:{PORT}")

done = False

msg = ''
msg_send = ''

while not done:
    try:
        msg_send = input("Message: ")
        client.send(msg_send.encode('utf-8'))
        if msg_send == 'quit':
            done = True
            
        msg = client.recv(1024).decode('utf-8')
        if msg and msg != 'quit':
            print (f"Received: {msg}")
        else:
            client.send('quit'.encode('utf-8'))
            done = True

    except KeyboardInterrupt:
        done = True
client.close()