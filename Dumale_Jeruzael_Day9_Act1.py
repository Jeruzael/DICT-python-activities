from user import *
from fileHandler import *

start = 0
emp = person()

while start == 0:
	app = Fh()
	s = str(input("$ "))
	if s == "a" or s == "A":
		app.addRec()
		n = emp.setName(input("Name: "))
		e = emp.setEmail(input("Email: "))
		a = emp.setAddr(input("Address: "))
		
		app.storeData(n, e, a)
	elif s == "b" or s ==  "B":
		app.viewRec()
		x = input("Press enter:")
	elif s == "c" or s ==  "C":
		app.revRec()
		x = input("Press enter:")
	else:
		app.exit()	
		start = 1	


