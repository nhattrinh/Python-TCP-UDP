import socket

def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count

server_ip = "127.0.0.1"
server_port = 5005
server_address = (server_ip,server_port)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#create data to send to server
sentence = input('Enter a sentence to send: ')
client_count = count_characters(sentence)

client_socket.sendto(sentence.encode(),server_address)

data, address = client_socket.recvfrom(1024)

print("Sentence: " + sentence)
print("Client's count: " + str(client_count))
print("Server's count: " + str(data.decode()))

client_socket.close()