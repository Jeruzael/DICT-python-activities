class Panel:
	def __init__(self):
		self.menu = f""" 
{"-"*20}RESTAURAN RESERVATION SYSTEM{"-"*20}
System Menu
[a] View all reservation
[b] Make reservation
[c] Delete reservation
[d] Generate report
[e] Exit

testing
"""
		self.view = f""" 
{"-"*20}Reservations{"-"*20}
#  Date			Time		Name		Adults	Children
"""


	def showMenu(self):
		print(self.menu)

	def viewRes(self):
		print(self.view)


