#! /usr/bin/python3

def modInverse(a, m) :
	a = a % m;
	for x in range(1, m) :
		if ((a * x) % m == 1) :
			return x
	return 1

def addition(x1, y1, x2, y2, field):
	slope = (y2 - y1) / (x2 - x1)
	slope = slope % field
	xnew = (slope * slope - x1 - x2) % field
	ynew = (-y1 + slope * (x1 - xnew)) % field
	temp = list()
	temp.append(xnew)
	temp.append(ynew)
	return temp
	
def doubling(x, y, field):
	s_num = (3 * x * x + 1)
	s_deno = modInverse(2 * y, field)
	s = (s_num * s_deno) % field
	xnew = (s * s - 2 * x) % field
	ynew = (-y + s *(x - xnew)) % field
	temp = list()
	temp.append(xnew)
	temp.append(ynew)
	return temp
	
print("Enter the parameters for elliptic curve of the form 'y^2 = x^3 + ax + b': ")
a = int(input("a = "))
b = int(input("b = "))

#check validity of the parameters
while(1): 
	if(4*a*a*a + 27*b*b == 0):
		print("Invalid parameters a & b. Choose other values for the parameters")
		a = input("a = ")
		b = input("b = ")
	else:
		break
print("Enter the prime field : ")
field = int(input())

i = "y"
while(i == "y"):
	print("	Menu of operations :")
	print("1 - Negation")
	print("2 - Addition")
	print("3 - Doubling")
	print("4 - Subtraction")
	print("5 - Check if point lies on elliptical curve")
	print("Enter your choice code: ", end = "")
	operation = int(input())
	if operation == 1:
		print("Enter the coordinates of point:")
		x = int(input("x coordinate - "))
		y = int(input("y coordinate - "))
		ynew = (-y) % field
		print("Negation of point is : (" + str(x) + "," + str(ynew) + ")") 
	elif operation == 2:
		print("Enter the coordinates of first point:")
		x1 = int(input("x coordinate : "))
		y1 = int(input("y coordinate : "))
		print("Enter the coordinates of second point:")
		x2 = int(input("x coordinate : "))
		y2 = int(input("y coordinate : "))
		if (x1 == -x2 and y1 == -y2):
			xnew, ynew = 0, 0
		elif (x1 == x2 and y1 == y2):
			xnew, ynew = doubling(x1, y1, field)
		else:
			xnew, ynew = addition(x1, y1, x2, y2, field)
		print("Addition of points is : (" + str(xnew) + "," + str(ynew) + ")")
	elif operation == 3:
		print("Enter the coordinates of point:")
		x = int(input("x coordinate : "))
		y = int(input("y coordinate : "))
		xnew, ynew = doubling(x, y, field)
		print("Doubling of point is : (" + str(xnew) + "," + str(ynew) + ")")
	elif operation == 4:
		print("Enter the coordinates of first point:")
		x1 = int(input("x coordinate : "))
		y1 = int(input("y coordinate : "))
		print("Enter the coordinates of second point:")
		x2 = int(input("x coordinate : "))
		y2 = int(input("y coordinate : "))
		y2 = (-y2) % field #negation of second point is taken and remaining process remains same as addition
		if (x1 == -x2 and y1 == -y2):
			xnew, ynew = 0, 0
		elif (x1 == x2 and y1 == y2):
			xnew, ynew = doubling(x1, y1, field)
		else:
			xnew, ynew = addition(x1, y1, x2, y2, field)
		print("Subtraction of points is : (" + str(xnew) + "," + str(ynew) + ")")
	elif operation == 5:
		print("Enter the coordinates of the point:")
		x = int(input("x coordinate : "))
		y = int(input("y coordinate : "))
		lhs = (y * y) % field
		rhs = (x*x*x + a*x + b) % field
		if lhs == rhs:
			print("Point lies on the curve.")
		else:
			print("Point doesn't lie on the curve.")
	else:
		print("Enter valid number")
		continue
	print("Do you want to continue : Y/N")
	i = input().lower()
