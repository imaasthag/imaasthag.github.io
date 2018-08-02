#answer = input("Who inspires you? ")
#print(answer, "inspires you!")
#i = -1
#while True:
    #i += 1

    #if (i > 20):
        #break

    #if (i %2 != 0):
        #continue

    #print(i)
#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")

while True:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    guess = int(guess) # converts a string to an integer
#if wrong tell whether to go up or down

    if (guess == aRandomNumber):
        print("Yay, you got it right!")
        break

    if (guess != aRandomNumber):

        if (guess < aRandomNumber):
             print('Your guess is too low.')
             continue

        elif (guess > aRandomNumber):
            print('Your guess is too high.')
            continue
