import os

class Fh:

	txt = f"""
{"-"*10}Record keeping app{"-"*10} 
[A] Add record
[B] View record
[C] Clear all records
[D] Exit

"""
	aRec = f"""
{"-"*10}Add record{"-"*10} 

testing
"""
	rRec = f"""
{"-"*10}Clear all record{"-"*10} 

testing
"""
	vRec = f"""
{"-"*10}View record{"-"*10} 

""" 
	def __init__(self):
		os.system('cls')
		print(self.txt)		

	def addRec(self):
		os.system('cls')
		print(self.aRec)

	def revRec(self):
		os.system('cls')
		print(self.rRec)	
		self.removeData()

	def viewRec(self):
		os.system('cls')
		print(self.vRec)
		self.viewData()

	def exit(self):
		print("THANK YOU!")

	def storeData(self, n, e, a):
		try:
			file = open("sample.txt", "a")
			file.write(f"\nName: {n}\nEmail: {e}\nAddres: {a}.\n")
			file.close()
		except:
			print("File not found!")
		else:
			pass
		finally:
			pass

	def viewData(self):
		try:
			file = open("sample.txt", "r")
			print(file.read())
			file.close()
		except:
			print("File not found!")
		else:
			print("success")
		finally:
			pass

	def removeData(self):
		try:
			os.remove("sample.txt")
		except:
			print("File not found")
		else:
			print("File successfully deleted")
			print("NO RECORDS FOUND!")
		finally:
			pass

