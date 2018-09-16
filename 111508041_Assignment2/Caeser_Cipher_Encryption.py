#!/usr/bin/python3
import sys

def main():
    if len(sys.argv) < 3:
        print('Usage: python3 Caeser_Cipher_Encryption.py <inputfile> shift')
        exit()

    inputFile = sys.argv[1]
    shift = int(sys.argv[2])


    fr = open(inputFile, 'r')
    fw = open('encrypted.txt', 'w')

    for line in fr:
        for char in line:
            if ord(char) >= 97 and ord(char) <= 122:
                char = chr(((ord(char) - 97 + shift) % 26) + 97)
            elif ord(char) >= 65 and ord(char) <= 90:
                char = chr(((ord(char) - 65 + shift) % 26) + 65)
            fw.write(char)
            fw.flush()

    fw.close()

if __name__ == '__main__':
    main()
