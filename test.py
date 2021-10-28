	#activity1
name = str("Jeruzael")
mg = float(99.9)
sg = float(99.9)
eg = int(100)
status = str("Single")

print("Name: "+name)
print("Math Grade: "+str(mg))
print("Science Grade: "+str(sg))
print("English Grade: "+str(eg))
print("Status: "+ status)

#Activity2
name = input("Name: ")
pasw = input("Password: ")

print("Name: "+name, "Password: "+pasw)

#Lesson 2: strings
#Place Holders
# {}
# %
# F

name = input("Name: ");
food = input("Favorite Food: ")
game = input("Favorite sport: ")


txt = "my name is {}. I love {}, and playing {}, "
op = txt.format(name, food, game);

print("\n"+op)

""""
String format functions
upper() - Convert string into upper case
lower() - Convert string into lower case
capitalize() - Converts the first characters in upper case.
title() - Converts the first character of each word to up-case
split() - Splits the strings 
replace() - replace words
len() - Check the length

Number formative functions
round()
ceil()
floor()
pow()
"""

import math
grade1 = 95.50
grade = 95.20

print(round(grade,1))
print(math.ceil(grade1))
print(math.ceil(grade2))
print(math.floor(grade1))
print(math.floor(grade1))
print(pow(2,3))
print(2**3)

""" 
Types of control structure
Sequence
selection (or decision control) structure
iteration(or repetition) structure

isupper() - all string are up
islower() - all string are low
isdigit() - all string are num
isalpha() - all string are in alphabet

List
appent() - 
account() - 
extend() - 
index() - 
insert() - 
pop()-
remove() - 
reverse() - 
sort() -

tuple
- unchangable
- can be used in database

useful tuple function
- len(t) => get the tuple length
- max(t) => get the maximum element
- min(t) => get the minimum element
- tuple(l) => convert list into tuple
- del t => delete tuple
- + => concatenate tuple
- in => check tuple chemistry

dictionary
- Store data in key value pairs
- in 3.7, dic is ordered, but in 3.6 earlier, its unodered
- writen in curly brackets
- ordered, in can be changed, does not allow duplicates
- presented in key: value pairs, can be referred using the key name.

"""

person = {
	'Name' = 'Jeruzael',
	'age' = 7,
	'class' = 'first'

}

#How to access dictionary?
print("Name: ", person['Name'])

#How to update dictionary?
person['age'] = 20

#how to check the dictionary?
person

#how to delete?
""" 
del person['Name'] => del specific element
person.clear() => remove all elements but person dictionary still remains
del person => delete all, also the dictionary in memory

SETS
- Store multiple items in a single variable
- inordered, unindexed
- written with curly brackets

set1.add("mango")
set1.update([1, 200])
set1.remove("cherry")
set1.disregard()


MODULE
- Code library
- file containing functions you want to include
ADVANTAGE
- Logically organize your python code
- code is easier to understand and use

CREATE A MODULE
~ how to call module
- import moduleName as alias
- from modulename import functionName
- from operation import *
 to view all built-in module
 - help('module')

 RANDOM
 - import random
 - implements pseudo-random number generator
 build-in function
 - random.randrange(1, 69)
 - random.choice('a','b','c','d')

 DATE & TIME
 from datetime import *
 
 EXCEPTIONS
 - events or errors that disrupts the normal flow of execution a program
 - prevents program from reaching the normal end.
 - example:
    1. Division by zero
    2. Invalid input
    3. File Not found

KIND OF EXCEPTIONS
- runtime exceptions
    - all exceptions except for runtime ex, are checked exception
- Erros
    - Unreadable file
    - Hardware malfunction

HANDLING EXCEPTIONS
try:
    if condition:
        raise exception
except EXCEPTIONNAME:
    pass
else:
    pass
finally: 
    pass


Class 3 types access modifier


file = open("file.txt", [r,a,w,x])

#how to read file
file = open("Operation.py", "r")
print(file.readline())
file.close()

#How to write a file
file = open("file.txt", "w")
file.write("\nThis is a new line")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()

#How to remove file
import os

os.remove("file.txt")


"""
