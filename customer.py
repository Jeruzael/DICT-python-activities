class Person:
	def __init__(self):
		self.__name = "No name"

	def setName(self, name):
		self.__name = name

	def getName(self):
		return self.__name