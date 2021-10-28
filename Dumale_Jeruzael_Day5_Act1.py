
def avg(name,m,e,s):
	avg = (m+e+s)/3
	print(f"\n{name}\'s grade (Math = {m}, Science = {e}, Enlish = {s}) and the average is {avg} ")
	

names = ["Jhon", "Ana", "Frank"]
math = [90, 98, 77]
eng = [94, 92, 75]
scie = [99, 78, 79]



for x in range(3):
	avg(names[x], int(math[x]), int(eng[x]), int(scie[x]))
	