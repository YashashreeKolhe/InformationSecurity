import sys
from hill_cipher import encrypt

def main():
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print("Usage: python3 encryption.py <inputfile> key")
		exit(1)
	fr = open(sys.argv[1], 'r')
	fw = open("encrypted.txt", 'w')
	key = sys.argv[2]
	for lines in fr:
		ciphertext = encrypt(key, lines)
		fw.write(ciphertext)
		fw.write("\n")
		fw.flush()
		
	fw.close()

if __name__ == "__main__":
	main()
