#!/usr/bin/python3

import sys 

def generateKeyMatrix(key, flag):
	keyMatrix = [[0 for i in range(0, 3)] for j in range(0, 3)]
	k = 0
	
	for i in range(0, 3):
		for j in range(0, 3):
			if flag == 1:
				keyMatrix[i][j] = (ord(key[k]) % 65)
			else:
				keyMatrix[i][j] = (ord(key[k]) % 97)
			k += 1
	return keyMatrix

def matrixDeterminant(matrix):
	det = matrix[0][0]*(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
	return det

def matrixTranspose(matrix):
	resMatrix = [[0 for i in range(0, 3)] for i in range(0, 3)]
	for i in range(0, 3):
		for j in range(0, 3):
			resMatrix[i][j] = matrix[j][i]
	return resMatrix


def matrixInverse(matrix):
	if matrixDeterminant(matrix) == 0:
		return null
	det = matrixDeterminant(matrix) % 26
	print(det)
	matrix = matrixTranspose(matrix)
	print(matrix)
	resMatrix = [[0 for i in range(0, 3)] for i in range(0, 3)]
	
	resMatrix[0][0] = int(((matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])*det) % 26)
	resMatrix[0][1] = int((-1 * ((matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])*det)) % 26)
	resMatrix[0][2] = int(((matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])*det) % 26)
	resMatrix[1][0] = int((-1 * ((matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1])*det)) % 26)
	resMatrix[1][1] = int(((matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0])*det) % 26)
	resMatrix[1][2] = int((-1 * ((matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])*det)) % 26)
	resMatrix[2][0] = int(((matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1])*det) % 26)
	resMatrix[2][1] = int((-1 * ((matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0])*det)) % 26)
	resMatrix[2][2] = int(((matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])*det) % 26)
	
	return resMatrix



def matrixMultiplication(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2):
		print("Error: Dimensions of Key Matrix (" + str(len(matrix1)) + "*" + str(len(matrix1[0])) + ") is incompatible with dimenstions of input string matrix (" + str(len(matrix2)) + "*" + str(len(matrix2[0])) + ")")
		exit()
	
	resMatrix = [[0 for i in range(0, 1)] for i in range(0, 3)]

	for i in range(0, 3):
		for j in range(0, 1):
			resMatrix[i][j] = 0
			for k in range(0, 3):
				resMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
			resMatrix[i][j] = resMatrix[i][j] % 26
	return resMatrix


def main():
	if len(sys.argv) < 3:
		print("Usage: python3 hill_cipher.py <inputfile> key(9 alphabets)")
		exit()
	inputfile = sys.argv[1]
	key = sys.argv[2]
	
	if len(key) != 9:
		print("Error: Key must contain 9 alphabets")
		exit() 
	
	if key.islower():
		flag = 0
		keyMatrix = generateKeyMatrix(key, 0)
	else:
		flag = 1
		keyMatrix = generateKeyMatrix(key, 1)


	matrix = [[0 for i in range(0, 1)] for i in range(0, 3)]

	fr = open(inputfile, 'r')
	fw = open('decrypted.txt', 'w')

	for line in fr:
		if line.strip().islower():
			matrix[0][0] = ord(line[0]) % 97
			matrix[1][0] = ord(line[1]) % 97
			matrix[2][0] = ord(line[2]) % 97
		else:
			matrix[0][0] = ord(line[0]) % 65
			matrix[1][0] = ord(line[1]) % 65
			matrix[2][0] = ord(line[2]) % 65
		inverseMatrix = matrixInverse(keyMatrix)
		print(inverseMatrix)
		print(matrix)
		matrixMult = matrixMultiplication(inverseMatrix, matrix)
		if flag == 0:
			fw.write(chr(matrixMult[0][0]+97) + chr(matrixMult[1][0]+97) + chr(matrixMult[2][0] + 97) + '\n')
			fw.flush()
		else:
			fw.write(chr(matrixMult[0][0]+65) + chr(matrixMult[1][0]+65) + chr(matrixMult[2][0] + 65) + '\n')
			fw.flush()

	fw.close()
	fr.close()
if __name__ == '__main__':
	main()

