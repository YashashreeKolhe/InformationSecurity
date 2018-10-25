#!/usr/bin/python3

from sys import exit
from time import time
 
KeyLength = 10
SubKeyLength = 8
DataLength = 8
FLength = 4
 
# Tables for initial and final permutations (b1, b2, b3, ... b8)
IPtable = (2, 6, 3, 1, 4, 8, 5, 7)
FPtable = (4, 1, 3, 5, 7, 2, 8, 6)
 
# Tables for subkey generation (k1, k2, k3, ... k10)
P10table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8table = (6, 3, 7, 4, 8, 5, 10, 9)
 
# Tables for the fk function
EPtable = (4, 1, 2, 3, 2, 3, 4, 1)
S0table = (1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 3, 1, 3, 2)
S1table = (0, 1, 2, 3, 2, 0, 1, 3, 3, 0, 1, 0, 2, 1, 0, 3)
P4table = (2, 4, 3, 1)
 
def perm(inputByte, permTable):
    """Permute input byte according to permutation table"""
    outputByte = 0
    for index, elem in enumerate(permTable):
        if index >= elem:
            outputByte |= (inputByte & (128 >> (elem - 1))) >> (index - (elem - 1))
        else:
            outputByte |= (inputByte & (128 >> (elem - 1))) << ((elem - 1) - index)
    return outputByte
 
def ip(inputByte):
    """Perform the initial permutation on data"""
    return perm(inputByte, IPtable)
 
def fp(inputByte):
    """Perform the final permutation on data"""
    return perm(inputByte, FPtable)
 
def swapNibbles(inputByte):
    """Swap the two nibbles of data"""
    #print("input for swap :") 
    #print(bin(inputByte))
    #print("swap :")
    #print(bin((inputByte << 4 | inputByte >> 4) & 0xff))
    return (inputByte << 4 | inputByte >> 4) & 0xff
 
def keyGen(key):
    """Generate the two required subkeys"""
    def leftShift(keyBitList):
        """Perform a circular left shift on the first and second five bits"""
        shiftedKey = [None] * KeyLength
        shiftedKey[0:9] = keyBitList[1:10]
        shiftedKey[4] = keyBitList[0]
        shiftedKey[9] = keyBitList[5]
        #print("keybits :" + str(keyBitList))
        #print("left-shift :" + str(shiftedKey))
        return shiftedKey
 
    # Converts input key (integer) into a list of binary digits
    keyList = [(key & 1 << i) >> i for i in reversed(range(KeyLength))]
    permKeyList = [None] * KeyLength
    for index, elem in enumerate(P10table):
        permKeyList[index] = keyList[elem - 1]
    shiftedOnceKey = leftShift(permKeyList)
    shiftedTwiceKey = leftShift(leftShift(shiftedOnceKey))
    subKey1 = subKey2 = 0
    for index, elem in enumerate(P8table):
        subKey1 += (128 >> index) * shiftedOnceKey[elem - 1]
        subKey2 += (128 >> index) * shiftedTwiceKey[elem - 1]
    return (subKey1, subKey2)
 
def fk(subKey, inputData):
    """Apply Feistel function on data with given subkey"""
    def F(sKey, rightNibble):
        aux = sKey ^ perm(swapNibbles(rightNibble), EPtable)
        #print('aux :')
        #print(bin(aux))
        index1 = ((aux & 0x80) >> 4) + ((aux & 0x40) >> 5) + \
                 ((aux & 0x20) >> 5) + ((aux & 0x10) >> 2)
        index2 = ((aux & 0x08) >> 0) + ((aux & 0x04) >> 1) + \
                 ((aux & 0x02) >> 1) + ((aux & 0x01) << 2)
        #print('index1:')
        #print(bin(index1))
        #print(index1)
        #print(S0table[index1])
        #print('index2:')
        #print(bin(index2))
        #print(index2)
        #print(S1table[index2])
        sboxOutputs = swapNibbles((S0table[index1] << 2) + S1table[index2])
        #print("sbox:")
       	#print(bin(sboxOutputs))
       	#print("perm:")
       	#print(bin(perm(sboxOutputs, P4table)))
        return perm(sboxOutputs, P4table)
 
    leftNibble, rightNibble = inputData & 0xf0, inputData & 0x0f
    return (leftNibble ^ F(subKey, rightNibble)) | rightNibble
 
def encrypt(key, plaintext):
    """Encrypt plaintext with given key"""
    data = fk(keyGen(key)[0], ip(plaintext))
    return fp(fk(keyGen(key)[1], swapNibbles(data)))
 
def decrypt(key, ciphertext):
    """Decrypt ciphertext with given key"""
    data = fk(keyGen(key)[1], ip(ciphertext))
    return fp(fk(keyGen(key)[0], swapNibbles(data)))  
 
if __name__ == '__main__':
    key = 0b1110001110
    print("key : ")
    print(bin(key))
    plaintext = 0b10101010
    print("plaintext : ")
    print(bin(plaintext))
    ciphertext = 0b11001010
    print("ciphertext : ")
    print(bin(ciphertext))
    
    print('\nEncrypting ...\n')
    
    try:
        assert encrypt(key, plaintext) == ciphertext
        print("Correct Ciphertext : ")
        print(bin(encrypt(key, plaintext)))
    except AssertionError:
        print("Error on encrypt:")
        print("Output: ", encrypt(key, plaintext), "Expected: ", ciphertext)
        exit(1)
        
    print('\nDecrypting ...\n')   
        
    try:
        assert decrypt(key, ciphertext) == plaintext
        print("Correct Plaintext on decryption : ")
        print(bin(decrypt(key, ciphertext)))
    except AssertionError:
        print("Error on decrypt:")
        print("Output: ", decrypt(key, ciphertext), "Expected: ", plaintext)
        exit(1)
