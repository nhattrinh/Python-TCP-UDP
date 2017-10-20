import socket

def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count


#create a socket for the server
server_socket = socket.socket()
#set the address of that socket to be localhost port 10000
server_address = ('',10000)
#the socket will be binded with the address
server_socket.bind(server_address)
#once the socket listens it turns into a server socket
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    client_message = client_socket.recvfrom(2048)
    print('Server got message: ' + client_message[0].decode())
    print('Server count: ' + count_characters(client_message[0].decode()))
    client_socket.send(str(count_characters(client_message[0])).encode())

server_socket.close()