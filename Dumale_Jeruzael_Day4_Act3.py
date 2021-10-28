#DAY4:ACT3
#WORD BANK

i = 0
b = 0
words = []

while b == 0:
	w = str(input("Input word: "))
	words.append(w)
	q = input("Try again? [Y]yes or [N]: ")
	if q == "y":	
		continue
	else:
		print(f"Number of word(s): {len(words)}")
		for word in words:						
			print(word)
		break

