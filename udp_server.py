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


#ip of server(localhost)
ip = "127.0.0.1"
#port of server
port = 5005
#address is the ip and port
address = (ip,port)

#server socket is the socket object with SOCK_DGRAM as second argument
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#server sockets always need to bind to the address that it is listening to
server_socket.bind(address)

#variable to stop server loop
stop_loop = False

#while server is online, the socket receives data through UDP protocol
while stop_loop == False:
    data, address = server_socket.recvfrom(1024)
    #decode the data and count number of characters to store in server_count
    server_count = count_characters(data.decode())
    #server socket send data back to client using UDP protocol
    server_socket.sendto(str(server_count).encode(),address)
    #terminate server if user wants
    stop_loop = terminate_prompt()
    
#finally close the socket
#for every socket created there must be a socket.close()
server_socket.close()
