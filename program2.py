
# Program To Check Recursive Letters In A sentence
# If We input "Here We Go Again"
# The program must output "e"
# If We Input "Have your dronk"
# The program must output "No Recursive Letters in the Sentence"

mySentence = input("Enter any Sentence ")
def changeWord(mySentence):

    myWord = ""
    for i in mySentence:
        if i == " ":
            continue
        else:
            myWord += i
    return myWord

def checkRecursiveLetter(mySentence):
    myWord = changeWord(mySentence)
    # print(myWord)
    myWordList = []
    recursiveLetter = ""
    count = 0
    for l in myWord.lower():
        if l not in myWordList:
            myWordList.append(l)
        else:
            count += 1
            recursiveLetter += l
            break
    if count == 0:
        return "No any recursive letters in the Sentence"
    else:
        return recursiveLetter


a = checkRecursiveLetter(mySentence)
print(a)
