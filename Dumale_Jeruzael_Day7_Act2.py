from calculations import *
import os

menu = f"""
{"-"*15}Calculator{"-"*15}
SELECT OPERATION: 
[1] Multiply
[2] Divide
[3] Add
[4] Subtract

 """

adds = f"""
{"-"*15}Addition{"-"*15}	
ENTER Num1 & num2
"""

mul = f"""
{"-"*15}Multiplication{"-"*15}	
ENTER Num1 & num2
"""

div = f"""
{"-"*15}Division{"-"*15}	
ENTER Num1 & num2
"""

Sub = f"""
{"-"*15}Subtract{"-"*15}	
ENTER Num1 & num2
"""

start = 0


while start == 0:
	print(menu)
	op = input("$ ")
	try:
		if op == '3':
			os.system('cls')			
			print(adds)
			add1 = float(input("Num1: "))
			add2 = float(input("Num2: "))
			add(add1,add2)		
		elif op == '1':
			os.system('cls')
			print(mul)
			m1 = float(input("Num1: "))
			m2 = float(input("Num2: "))
			multiply(m1, m2)	
		elif op == '2':
			os.system('cls')
			print(div)
			div1 = float(input("Num1: "))
			div2 = float(input("Num2: "))
			divide(div1, div2)	
		elif op == '4':
			os.system('cls')
			print(Sub)
			Sub1 = float(input("Num1: "))
			Sub2 = float(input("Num2: "))
			subtract(Sub1, Sub2)	
		else:
			raise ValueError
	except ValueError as e:
		print("Use numbers only")
		start = 0
	else:
		pass
	finally:
		pass

	print("Try again? hit[1]yes or [2]no")
	hit = input("$ ")
	if hit == '1':
		start = 0
		os.system('cls')
	else:
		start = 1
	
