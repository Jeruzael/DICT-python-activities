print("Please input 3 nouns: ")
n1 = input("Noun1(nationality): ")
n2 = input("Noun2(Parts of the body): ")
n3 = input("Noun3(name): ")

print("Now input 3 adjectives:")
ad1 = input("adjective1: ")
ad2 = input("adjective2: ")
ad3 = input("adjective3: ")

origSong = """ 
You're just too good to be true
Can't take my eyes off of you
You'd be like Heaven to touch
I wanna hold you so much
At long last, love has arrived
And I thank God I'm alive
You're just too good to be true
Can't take my eyes off of you
Pardon the way that I stare
There's nothin' else to compare
The sight of you leaves me weak
There are no words left to speak
But if you feel like I feel
Please let me know that it's real
You're just too good to be true
Can't take my eyes off of you
I love you, baby
And if it's quite alright
I need you, baby
To warm the lonely night
I love you, baby
Trust in me when I say
Oh, pretty baby
Don't bring me down, I pray
Oh, pretty baby
Now that I've found you, stay
And let me love you, baby
Let me love you
"""

song = f"""
You're just too {ad1.upper()} to be {n1.upper()}
Can't take my {n2.upper()} off of you
You'd be like {ad2.upper()} to touch
I wanna hold you so much
At long last, love has arrived
And I thank God I'm alive
You're just too {ad1.upper()} to be true
Can't take my {n2.upper()} off of you
Pardon the way that I stare
There's nothin' else to compare
The sight of you leaves me {ad3.upper()}
There are no words left to speak
But if you feel like I feel
Please let me know that it's real
You're just too {ad1.upper()} to be true
Can't take my {ad2.upper()} off of you
I love you, {n3.upper()}
And if it's quite alright
I need you, {n3.upper()}
To warm the lonely night
I love you, {n3.upper()}
Trust in me when I say
Oh, pretty {n3.upper()}
Don't bring me down, I pray
Oh, pretty {n3.upper()}
Now that I've found you, stay
And let me love you, {n3.upper()}
Let me love you
"""

print(origSong)
print(song)

