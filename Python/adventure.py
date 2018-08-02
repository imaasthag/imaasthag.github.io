# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

done = False

while (done != True):

    print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
    user_input = input()
    if user_input == "left":
        done = True
        print("You decide to go left and a pool of lava swallows you and takes you to your doom.") # Update to match your story.
        break
        # Continue code to finish story.

    elif user_input == "right":
        done = True
        print("You choose to go right and you find a yellow brick road with a sign that says, 'This way to Oz!' Move forward type yes, if not type no") # Update to match your story.
        user_input = input()
        if user_input == "yes":
            done = True
            print("You meet the Scarecrow! Do you want to speak with him? Type yes or no.")
            user_input = input()
            if user_input == "yes":
                done = True
                print("The Scarecrow says,'Do you want to be my friend?'")
                user_input = input()
                if user_input == "yes":
                    done = True
                    print("You have made a friend and get home safe!")
                    break

                if user_input == "no":
                    done = True
                    print("You haven't made a friend. The mad scarecrow sends his birds to kill you! GAME OVER") # Update to match your story.
                    break

            elif user_input == "no":
                done = True
                print("You go back home.")
                break

        elif user_input == "no":
            done = True
            print("You hesitate for too long and The Wicked Witch of Oz sends her monkeys and YOU DIE!")
            break


    else:
        print("I'm sorry, that was not an option.")
        continue
        # Continue code to finish story.
