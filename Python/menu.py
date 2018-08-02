#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
haiku5 = ["Haikus are easy.","Refrigerator.","You never feed me","Shoe laces.","You think you're big."]
haiku6 = ["But sometimes they don't make sense.","Must attack at once.","And your house is a big mess?","IPods, mobiles, cameras.","Has to be five seven five."]
haiku7 = ["OMG KITTENS.","By a fierce dragon.","Yes! Afghanistan.","Life is so extreme.","He is now homeless."]
#Generates a random integer.
aRandomIndex = randint(0, len()-1)
print(haiku5[aRandomIndex],haiku6[aRandomIndex],haiku7[aRandomIndex])
