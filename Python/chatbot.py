# --- Define your functions below! ---
def intro():
    welcome = ("Hi! I'm Chatty bot!")
    print(welcome)

def process_input(text):
    if (text == "Hi!"):
        print("Hello There!")
        is_valid_input(text, valid_responses)
    elif(text == "Square up!"):
        print("Be there or be square :D")
    elif (text == "Yo!"):
        print("YOLO!")
    elif(text == "Tell me a joke!"):
        joke(text)
    else:
        print("You're lame.")

def is_valid_input(user_input, valid_responses):
    if(user_input in valid_responses):
        return(True)
    else:
        return(False)

def joke(text):
    print("Knock Knock")
    text = input("(What will you say?) ")
    if (text == "Who's there?"):
        print("Etch.")
        text = input("(What will you say?) ")
        if (text == ("Etch who?")):
            print("Bless you!")

valid_responses = ["Hi!"]



# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
