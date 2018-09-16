#!/usr/bin/python3

import socket

def encrypt(password):
	flag = 0
	for char in password:
		if flag == 0:
			encryption_line = char
			flag = 1
			first_char = ord(char)%10
		else:
			encryption_line = encryption_line + chr(ord(char) - first_char)
			first_char = ord(char)%10
	return encryption_line

def main():
	host = socket.gethostname()  # as both code is running on same pc
	port = 5000  # socket server port number

	client_socket = socket.socket()  # instantiate
	client_socket.connect((host, port))  # connect to the server

	data = client_socket.recv(1024).decode()
	print(data)

	username = input('Client: ')
	client_socket.send(username.encode())
	print('Sending Username : ' + username + ' to Server ...')

	data = client_socket.recv(1024).decode()
	print(data)

	password = input('Client: ')
	client_socket.send(encrypt(password).encode())
	print('Sending encrypted password : ' + encrypt(password) + ' to Server...')

	data = client_socket.recv(1024).decode()
	print(data)
	
	client_socket.close()  # close the connection


if __name__ == '__main__':
	main()
