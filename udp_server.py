import socket

def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count

ip = "127.0.0.1"
port = 5005
address = (ip,port)

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(address)

while True:
    data, address = server_socket.recvfrom(1024)
    server_count = count_characters(data.decode())
    server_socket.sendto(str(server_count).encode(),address)
    
server_socket.close()