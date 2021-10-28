
start = 0
person = {}

while start == 0:
	print("-"*5+"Welcome to Record keeping app"+"-"*5)
	selector = int(input("[1]Add data\n[2]Delete Data\n[3]End\n=> "))

	if selector == 1:
		print("-"*5 + "Adding Data to Dictionary" + "-"*5)
		key = input("Enter key: ")
		val = input("Enter value: ")

		person[key] = val

		print("Dictionary: ", person)
	elif selector == 2:
		print("-"*5 + "Deleting data from Dictionary" + "-"*5)
		key = input("Enter Key: ")
		del person[key]

		print("Element deleted: ", person)
	elif selector == 3:
		print("*"*5 + "Session ended" + "*"*5)
		print("THANK YOU!")
		start = 1
	else:
		print("Select [1], [2], or [3] only")
	