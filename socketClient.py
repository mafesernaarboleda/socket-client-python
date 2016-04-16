import socket


def receive(socket):
    total_data = []
    data = ''
    while True:
        data = socket.recv(8192)
        if "[END]" in data:
            total_data.append(data[:data.find("[END]")])
            break
        total_data.append(data)
        if len(total_data) > 1:
            # check if end_of_data was split
            last_pair = total_data[-2] + total_data[-1]
            if "[END]" in last_pair:
                total_data[-2] = last_pair[:last_pair.find("[END]")]
                total_data.pop()
                break
    return ''.join(total_data)


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "127.0.0.1"

port = 10009

clientId = "6"

# connection to hostname on the port.
s.connect((host, port))

print "connected with server "
# infinite loop to keep client alive
var = 1
while var == 1:
    msg = receive(s)
    if msg == "-s":
        print "Subscribed as " + clientId
        s.sendall(clientId)
    else:
        print "Receiving data from server : " + msg
