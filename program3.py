
# Program to Print the all recursive letters in the given word or sentence with their times of repetition.
# The program will not print the letters that are present only one time in a sentence or word
# For Example "shq love pig"
# The program must repeat "No letters are repeated in the given input"
# For example "He must have been tired working all day"
# Output :  h -> repeated 2 times e -> repeated 5 times t -> repeated 2 times and so on .


myInput = input("Enter any Sentence ")

def changeIntoWord(myInput):
    myWord = ""

    for l in myInput.lower():
        if l == " ":
            continue
        else:
            myWord+=l
    return myWord


def check_repetitive_letters(myInput):
    myWord = changeIntoWord(myInput)
    myLetterList = []
    myRepLetterList = {}
    myRepLetterTime = []


    for l in myWord:
        myLetterList.append(l)

    for i in myWord:
        count = 0
        for l in myLetterList:
            # count = 0
            if i == l:
                count += 1
                continue
            if count > 1:
                myRepLetterList[i] = count

    # print(len(myRepLetterList))
    if len(myRepLetterList) > 0:

        for key in myRepLetterList:
            if myRepLetterList[key] > 1:
                print(f"The letter {key} is repeated -> {myRepLetterList[key]} times")
    else:
        print("No Letters are Repeated")




check_repetitive_letters(myInput)