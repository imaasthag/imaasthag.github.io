if(word.isalpha() == False):
	print("That's not a word!")

# Some useful variables
guesses = []
current = ["_"] * len(word)
lives = 7

while(True):

    # Ask user for a letter
    print("Lives Left: ", lives)
    print("Guesses So Far: ", guesses)
    print("Current Word: ", current)

    guess = input("Guess a letter: ")
    print('''\n----------------------------------------------''')

    # Put into guesses
    guesses.append(guess)

    # If letter is in the word
    if (guess in word):
        print("You got a letter!")
        # ENTER YOUR CODE HERE: Update the current word

        # ENTER YOUR CODE HERE: Check if user has won the game or not

    # If letter is not in the word
    else:
        print("Wrong guess!")
        lives = lives - 1
        if (lives <= 0):
            print("No lives left. You lose!")
            break
