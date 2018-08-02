import json
responses= []

file = open("survey.json")
mydict= {}
numTimesLoggedin = 0
# counter = 0

def intro():
    welcome = ("Hi! This is a survey! Please answer as truthfully as possible!")
    print(welcome)

def process_input():
    # global counter
    # counter += 1
    question = ("What is your name?")
    print(question)
    user_input = input()

    if user_input in mydict.keys():
        mydict[user_input] += 1
        print('Welcome back', user_input)
    else:
        mydict[user_input] = 1
        print('Welcome', user_input)
    print(mydict)

    mydict["What month were you born?"] = input("How old are you?")
    mydict["Do you own any pets?"] = input("What city were you born in?")
    mydict["What did you have for dinner last night?"] = input("What did you have for dinner last night?")
    responses.append(mydict)

    if input("Are you done?") == ("yes"):
        print(responses)

    file = open("survey.json", "w")
    file.write("responses")
    #json.load(file)
    json.dump(responses, file)
    file.close()
        #
    # if counter == 3:
    #     level = 1
    #     print("Would you like to answer another question?")
    #     if user_input == "Yes":
    #         age()
    #             break
    #
    #     if user_input != "Yes":
    #         process_input()
# myDict = {}
# myDict["Emma"] = 18
# myDict["Nathalie"] = 18
# myDict["Lucy"] = 17
# myDict["Polina"] = 17
# print(myDict)


# --- Put your main program below! ---
def main():
    intro()
    while True:
        process_input()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
