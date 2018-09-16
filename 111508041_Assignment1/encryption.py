import sys

def main():
    fw = open(sys.argv[2], 'w')
    fr = open(sys.argv[1], 'r')
    for line in fr:
        flag = 0
        for char in line:
                if flag == 0:
                    encryption_line = char
                    flag = 1
                    first_char = ord(char)%10
                else:
                    encryption_line = encryption_line + chr(ord(char) - first_char)
                    first_char = ord(char)%10
        fw.write(encryption_line)
        fw.flush()
    fw.close()

if __name__ == '__main__':
    main()
