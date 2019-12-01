def send_msg(msg, socket):
    response = ""
    while len(response) <= 2:
        socket.send(bytes(msg + '\n\r', 'ASCII'))
        response = socket.recv(1024)
    return response