#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["Jake Peralta","Billy","Joe","Pammy","Patty","Sally","Honey"]
names = ["Jim","Jill","Beau","Amy","Sam","Alex","Sugar"]
#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
print(names[aRandomIndex],aList[aRandomIndex])
