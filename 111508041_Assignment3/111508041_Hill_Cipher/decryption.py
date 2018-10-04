import sys
from hill_cipher import decrypt

def main():
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print("Usage: python3 decryption.py <encrypted_file> key")
		exit(1)
	fr = open(sys.argv[1], "r")
	fw = open("decrypted.txt", "w")
	key = sys.argv[2]
	for lines in fr:
		plaintext = decrypt(key, lines)
		fw.write(plaintext)
		fw.flush()
	fw.close()

if __name__ == "__main__":
	main()
