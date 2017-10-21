import socket

def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count

def terminate_prompt():
    user_input = input("\nTerminate server, y/n? ")
    if (user_input.__eq__("n")):
        return False
    return True


#create a socket for the server
socket = socket.socket()
#set the address of that socket to be localhost port 10000
address = ('',10000)
#the socket will be binded with the address
socket.bind(address)
#once the socket listens it turns into a server socket
socket.listen(1)

stop_loop = False

while stop_loop == False:
    client_socket, client_address = socket.accept()
    client_message = client_socket.recvfrom(1024)
    
    client_socket.send((str(count_characters(str(client_message[0].decode())))).encode())
    stop_loop = terminate_prompt()
    
socket.close()