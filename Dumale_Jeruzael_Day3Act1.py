#Day 3 act 1
#Jeruzael R. Dumale

name = input("Enter your name: ")
mg = float(input("Enter your math grade: "))
sg = float(input("Enter your science grade: "))
eg = float(input("Enter your English grade: "))
sub = ""

avg = (mg+sg+eg)/3

print("\nAverage: "+str(avg))

if avg < 75:
	print(f"\nCongratulations {name}, you failed!. See you again.")
else:
	print(f"\nCongratulations {name}, You passed! I will miss you!")
	if mg < 75 or sg < 75 or eg < 75:
		if mg < 75:
			sub = sub+"\nMath"

		if sg < 75:
			sub = sub+"\nScience"

		if eg < 75:
			sub = sub+"\nEnglish"

		failedSub = sub;

		txt = f"""You passed the semester, but you need to retake this subject(s): {failedSub}"""

		print(txt)




