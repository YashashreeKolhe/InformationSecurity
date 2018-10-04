import numpy as np
import math

def generateKeyMatrix(key):
	if(math.sqrt(len(key)) - int(math.sqrt(len(key)))):
		print("Error: Key must have length equal to perfect square!")
		exit(1)
	dimension = int(math.sqrt(len(key)))
	matrix = [[0 for i in range(0, dimension)] for j in range(0, dimension)]
	k = 0
	if key.isupper():
		for i in range(0, dimension):
			for j in range(0, dimension):
				matrix[i][j] = ord(key[k]) % 65
				k += 1
	else:
		for i in range(0, dimension):
			for j in range(0, dimension):
				matrix[i][j] = ord(key[k]) % 97
				k += 1

	return matrix

def encrypt(key, plainText):
	keyMatrix = generateKeyMatrix(key)
	dimension = len(keyMatrix[0])
	ciphertext = ""
	sub_text = list()
	
	for char in plainText:
		if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
			if (char.isupper()):
				sub_text.append(ord(char) % 65)
			elif (char.islower()):
				sub_text.append(ord(char) % 97)
			if len(sub_text) == dimension:
				matrix = np.array(sub_text).reshape(-1, 1)
				multMatrix = np.matmul(keyMatrix, matrix)
				for i in range(0, dimension):
					for j in range(0, 1):
						ciphertext = ciphertext + chr((multMatrix[i][j] % 26) + 97)
				sub_text.clear()
			else:
				continue
				
		else:
			continue
	if len(sub_text) != 0:
		for i in range(0, len(sub_text)):
			ciphertext = ciphertext + chr(sub_text[i] + 97) 
	return ciphertext	
	
def decrypt(key, cipherText):
	keyMatrix = generateKeyMatrix(key)
	dimension = len(keyMatrix[0])
	plaintext = ""
	sub_text = list()

	determinant = int(np.linalg.det(keyMatrix))
	print(determinant)
	if determinant == 0:
		print("Error: Inverse of key matrix does not exist")
		exit(1)
	inverse = np.linalg.inv(keyMatrix)
	modulo_inverse_det = 0

	for i in range(1, 9999):
		if ((determinant * i)%26) == 1:
			modulo_inverse_det = i
			break
	print(modulo_inverse_det)
	if modulo_inverse_det == 0:
		print("Error: Cannot compute modulo inverse of determinant")
		exit(1)
			
	for i in range(0, dimension):
		for j in range(0, dimension):
			inverse[i][j]  = (inverse[i][j] * modulo_inverse_det * determinant) % 26
	print(inverse)
	for char in cipherText:
		if char.islower() or char.isupper():
			if(char.isupper()):
				sub_text.append(ord(char) % 65)
			else:
				sub_text.append(ord(char) % 97)	
			if len(sub_text) == dimension:
				matrix = np.array(sub_text).reshape(-1, 1)
				print(matrix)
				multmatrix = np.matmul(inverse, matrix)
				for i in range(0, dimension):
					for j in range(0, 1):
						multmatrix[i][j] = round(multmatrix[i][j]) % 26
						print(multmatrix[i][j])
						plaintext = plaintext + chr(int(multmatrix[i][j]) + 97)
				sub_text.clear()
			else:
				continue
		else:
			continue
	if len(sub_text) != 0:
		for i in range(0, len(sub_text)):
			plaintext = plaintext + chr(sub_text[i] + 97)
	return plaintext
		
