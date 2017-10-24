import socket

def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count

#create a socket for client, no need to set arguments, default is set for tcp socket
client_socket = socket.socket()
#set arbitrary ip for server we are requesting/sending from/to
server_name = "127.0.01"
#set the server port for the packet to travel through
server_port = 10000

#connect the socket with the server's address
socket.connect((server_name,server_port))

#create data to send to server
sentence = input("Enter a sentence to send: ")
client_count = count_characters(sentence)
#send the sentence(data) to the server
client_socket.send(sentence.encode())
#wait for server to acknowledge and receive server's count of characters
data = socket.recv(1024)
server_count = data.decode()

print("Sentence: " + sentence)
print("Client's count: " + str(client_count))
print("Server's count: " + str(server_count))
socket.close()

