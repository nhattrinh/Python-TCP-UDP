import socket
import sys

def count_characters(sentence):
    sentence = str(sentence)
    words = sentence.split(' ')
    char_count = 0
    
    for word in words:
        char_count += len(word)
        
    return char_count

client_socket = socket.socket()
server_name = 'tcp_server'
server_port = 10000

client_socket.connect((server_name,server_port))
sentence = input('Enter a sentence to send: ')
client_socket.send(sentence.encode())

client_socket.close()
