from cUser import *
import os

start = 0 
u = User()

while start == 0:	
	u.startApp()
	s = str(input("=> "))
	if s == 'a':
		os.system('cls')
		u.printReport()
	elif s == 'b':
		os.system('cls')
		u.getInfo()
	elif s == 'c':
		os.system('cls')
		u.delRes()
	elif s == 'd':
		os.system('cls')
		u.printReport()
	else:
		print("THANK YOU")
		start = 1

	x = int(input("Try again? "))
	if x == 1:
		start = 0
	else:
		start = 1
		