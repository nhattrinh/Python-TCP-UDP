"""
Nhat Trinh
011227645
Python 3.6
CMPE 148 Fall 2017 10:30am
"""

import socket

#function to count the characters in any string
def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count

#function to terminate the loop to end the server
def terminate_prompt():
    user_input = input("Terminate server, y/n? ")
    if (user_input.__eq__("n")):
        return False
    return True

#create a socket for the server
server_socket = socket.socket()
#set the address of that socket to be localhost port 10000
ip = "127.0.0.1"
port = 10000
address = (ip,port)
#the socket will be binded with the address
server_socket.bind(address)
#once the socket listens it turns into a server socket
server_socket.listen(1)

stop_loop = False

while stop_loop == False:
    # accept incoming connection from client
    client_socket, client_address = server_socket.accept()
    # receive data from the socket tcp style
    client_message = client_socket.recv(1024)
    
    # decode, count number of characters from client's data, encode, and send
    client_message = client_message.decode()
    server_count = count_characters(client_message)
    client_socket.send((str(server_count)).encode())
    # ask user if they want to terminate loop
    stop_loop = terminate_prompt()
    
# for every socket open there must be a socket close
server_socket.close()