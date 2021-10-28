class Student:

	__name = ""
	__math = 0
	__science = 0
	__english = 0

	def __init__(self, name, math, science, english):
		self.__name = name
		self.__math = math
		self.__science = science
		self.__english = english

	def getMath(self):
		return self.__math

	def getScience(self):
		return self.__science

	def getEnglish(self):
		return self.__english

	def getName(self):
		return self.__name

	def getAvg(self, m, s, e):
		avg = (m + s + e) / 3
		return avg

	def result(self, n, avg):
		if avg <= 74:
			print(f"Sorry {n}, Your average is {avg}. you failed.")
		else:
			print(f"Congratulations! {n}, Your average is {avg}. you passed.")

	def test(self):
		print("working")