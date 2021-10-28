def test():
	print("working")

def add(n1, n2):
	try:
		print(f"Sum: {n1 + n2}")
		return n1 + n2
	except TypeError:
		print("invalid input") 
	else:
		pass
	finally:
		pass

def subtract(n1, n2):
	try:
		print(f"Difference: {n1 - n2}")
		return n1 - n2
	except:
		print("invalid input")
	else:
		pass
	finally:
		pass	

def multiply(n1, n2):
	try:
		print(f"Product: {n1 * n2}")
		return n1*n2
	except:
		print("invalid input")
	else:
		pass
	finally:
		pass	

def divide(n1, n2):
	try:
		n1/n2
	except ZeroDivisionError:
		print("The divisor is Zero")
	else:
		print(f"Quotient: {n1 / n2}")
		return n1/n2
	finally:
		pass