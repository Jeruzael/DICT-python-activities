#Day 3 act 2
#Jeruzael R. Dumale

name = input("Enter your name: ")
office = input("Office: ")
yrs = int(input("No. of yrs of service: "))
bonus = 0

if office == "IT" or office == "it" or office == "It":
	if yrs >= 10:
		bonus = 10000
	else:
		bonus = 5000
elif office == "ACCT" or office == "Acct" or office == "acct":
	if yrs >= 10:
		bonus = 12000
	else:
		bonus = 6000
if office == "HR" or office == "hr" or office == "Hr" and yrs >= 10:
	if yrs >= 10:
		bonus = 15000
	else:
		bonus = 7500

op = f"""
Bonus:
Name: {name}
Office: {office}
Bonus: {bonus}

 """

print(op)



