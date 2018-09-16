#!/usr/bin/python3

import socket

def decrypt(password):
	flag = 0
	for char in password:
		if flag == 0:
			decryption_line = char
			flag = 1
			first_char = ord(char)%10
		else:
			decryption_line = decryption_line + chr(ord(char) + first_char)
			first_char = ord(chr(ord(char) + first_char))%10
	return decryption_line

def main():

	dict_of_login = {'yashashree': 'yvkolhe'}

	host = socket.gethostname()
	port = 5000

	server_socket = socket.socket()
	server_socket.bind((host, port))

	server_socket.listen(2)
	conn, address = server_socket.accept()
	print('Connected to ' + str(address))

	print('Server: Enter the Username')
	conn.send('Server: Enter the Username'.encode())
	
	print('Receiving username from Client ...')
	username = conn.recv(1024).decode()
	print('Client: ' + username)
	
	print('Server: Enter the Password')
	conn.send('Server: Enter the Password'.encode())
	print('Receiving password from Client ...')

	encrypted_password = conn.recv(1024).decode()
	print('Client: ' + encrypted_password)

	print('Decrypting password and verifying ...')
	if decrypt(encrypted_password) == dict_of_login[username]:
		print('Server: The password : ' + decrypt(encrypted_password) + ' has been verified correctly')
		conn.send('Server: The password has been verified correctly'.encode())
	else:
		print('Server: The decrypted password : ' + decrypt(encrypted_password) + ' is invalid')
		conn.send('Server: The decrypted password is invalid'.encode())

if __name__ == '__main__':
	main()


