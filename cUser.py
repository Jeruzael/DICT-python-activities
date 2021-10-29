from customer import *
from gui import *
import os

class User(Person, Panel):
	name = ""
	adult = 0
	child = 0
	date = ""
	time = ""

	slot = []
	ph = 1

	def __init__(self):
		Person.__init__(self)
		Panel.__init__(self)
				

	def startApp(self):
		self.showMenu()

	def getInfo(self):
		self.setName(str(input("Name: "))) 
		self.adult = int(input("Adult: "))
		self.child = int(input("Children: "))
		self.date = str(input("Date: "))
		self.time = str(input("Time: "))

		self.slot.append(f"{self.ph}  {self.date}   {self.time}      {self.getName()}            {self.adult}       {self.child}")
		self.ph = self.ph + 1

	def printReport(self):
		self.viewRes()	
		for x in self.slot:	
			print(x)

	def delRes(self):
		self.printReport()
		q = int(input("\nType the number of reservation that u want to delete: "))
		del self.slot[q]
		print("Deleted")
		os.system('cls')
		self.printReport()




