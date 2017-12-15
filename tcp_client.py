import socket

#function to count the characters in any string
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
client_socket.connect((server_name,server_port))

#create data to send to server
sentence = input("Enter a sentence to send: ")
client_count = count_characters(sentence)
#send the sentence(data) to the server
client_socket.send(sentence.encode())
#wait for server to acknowledge and receive server's count of characters
data = client_socket.recv(1024)
server_count = data.decode()

"""client compares the count to server's count then print out both the message
    and the count"""
if (client_count.__str__() == server_count):
    print("Sentence: " + sentence)
    print("Character count: " + str(client_count))
else:
    print("Client and server counts are not equal!")
    
# for every socket initialized there must be a socket close
client_socket.close()

