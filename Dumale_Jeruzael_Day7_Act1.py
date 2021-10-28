#Random name generatorr
import random

fn = ["Goku","Naruto","ichigo","luffy","Tempest","rudeus","eris","Dalgona","Baby","Happy","yagba","etits","Roa","sandro","king e","sabado","sabog","kartite","hotdog","rastaman","Mar Roxas","Anton","Totoy","Jeje","Adik"]
mn = ["may","sanguin","rosian","Saber","Alucard","Hayabusa","leni","Jimbo","Salisal","Kamui","Ai","Sy","Momi","Rodrigo","Robredo","Kalabasa","Talong","Lawlaw","Sibuyas","Mane","Na","Oy","Bebe","Kulangot","Laplap"]
ln = ["simsimi","kaloy","randy","light","thunder","borduza","zamshi","Alibaso","Quinti","Rabutsi","Bulbol","Bantot","Baho","Supot","Kulubot","Tarantado","Baduy","Laspag","Bading","Burnik","Ulol","Putok","Kulot","Pepe","Shabu"]
gn = []

start = 0
i = 0

while start == 0:
	print("-"*5+"Welcome to random name generator"+"-"*5+"\nPlease Hit [1] to start!")
	hit = int(input("==> "))
	if hit == 1:
		frd = random.randrange(0,25)
		mrd = random.randrange(0,25)
		lrd = random.randrange(0,25)
		gn.append(fn[frd]+" "+mn[mrd]+" "+ln[lrd])
		print(f"Random Num: {frd}, {mrd}, {lrd}")
		txt = f"""CONGRATULATIONS! YOUR NEW NAME IS {gn[i]}.

Do you wish to try again? hit [1]yes or [2]no"""

		print(txt)
	hit = int(input("==> "))
	if hit==1:
		start = 0
		i = i + 1
	else:
		print("THANK YOU!\nGenerated Names:")
		for x in gn:
			print(x)
		start = 1	
	