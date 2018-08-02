    #people = ["Meredith","Eva","Nidhi"]
    #print(len(people))
    #print(people["Susie"])
    #people[1]="Megan"
    #print(people[1])

    #for p in people:
    #    print(p)
    #for i in range(len(people)):
        #print(people[i])

#    word = input("Enter a word: ")
#    print(word)
#    numofa = 0
#    for letters in word:
#        if letters == "a":
#            numofa += 1
#    print(numofa)

isPal= True
noPal= False
word = input("Enter a word: ")
print(word)

for x in range(len(word)):
    if word(x) == word(len(word)-1-x):
        isPal= True
