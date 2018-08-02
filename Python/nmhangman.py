word = input("Enter a word: ")


guessed_letters = [] # a list of letters guessed so far
word_guessed = []
for letter in word:
    word_guessed.append("-") # create an unguessed, blank version of the word
joined_word = None # joins the words in the list word_guessed




attempts = 7


while (attempts != 0 and "-" in word_guessed):
    print(("\nYou have {} attempts remaining").format(attempts))
    joined_word = "".join(word_guessed)
    print(joined_word)

    try:
        player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
    except: # check valid input
        print("That is not valid input. Please try again.")
        continue
    else:
        if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
            print("That is not a letter. Please try again.")
            continue

guessed_letters.append(player_guess)

for letter in range(len(chosen_word)):
    if guess == word:
        word[letter] = guess # replace all letters in the chosen word that match the players guess

    if player_guess not in chosen_word:
        attempts = attempts-1
        print(word[(len(word) - 1) - attempts])
