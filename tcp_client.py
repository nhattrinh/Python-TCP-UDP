import socket

def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count

#create a socket for client
socket = socket.socket()
#set arbitrary name for server we are requesting from
server_name = "localhost"
#set the server port for the packet to travel through
server_port = 10000

#connect the socket with the server's address
socket.connect((server_name,server_port))

#create data to send to server
sentence = input('Enter a sentence to send: ')
character_count = count_characters(sentence)
#send the sentence(data) to the server
socket.send(sentence.encode())
#wait for server to acknowledge and receive server's count of characters
server_character_count = socket.recv(1024)
server_character_count = server_character_count.decode()

print("Sentence: " + sentence)
print("Client\'s count: " + str(character_count))
print("Server\'s count: " + str(server_character_count))
socket.close()

