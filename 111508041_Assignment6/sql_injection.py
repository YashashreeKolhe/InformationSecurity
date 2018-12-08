#!/usr/bin/python3

import sys
import mysql.connector

def connectToDb():
	mysqlconn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "sql_injection_db")
	return mysqlconn

def main():
	mysqlconn = connectToDb()
	cursor = mysqlconn.cursor()
	
	print("**** WELCOME TO LOGIN SYSTEM ****")
	print('\n')
	
	while 1:
		print("Username : ")
		username = input()
		print("Password : ")
		password = input()

		sql_str = "SELECT username, password FROM user_details where username = '"
		
		print("Query Used: " + sql_str + username + "'" + ";")
		
		try:
			cursor.execute(sql_str + username + "'" + ";")
			print("\nExtracted Output: ")
			result = cursor.fetchall()
			for x in result:
				print(x)
			print("\nSuccessfully logged in!")

		except:
			print("\nError while logging! Invalid username ...")
			
		print('\nDo you want to continue? (y/n): ')
		choice = input()
		if choice == 'y' or choice == 'Y':
			continue
		else:
			break

if __name__ == "__main__":
	main()
