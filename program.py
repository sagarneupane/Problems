
# Program To Print the first repeated letter in python
# For example :: if user enters the word "knowledgel"
# The program will print 'l' as first repeated word
# If the word doesnot have any repeated letters then it will print "No Letters are Recursive In the Word"

myInput = input("Enter a Word Without giving")

def checkRecursion(myInput):
    myInput = myInput.lower()
    list_lett = []
    count = 0
    recurs_lett = ""
    for l in myInput:
        if l not in list_lett:
            list_lett.append(l)
        else:
            count += 1
        if count>0:
            recurs_lett += l
            break
    if count == 0:
        return "No Letters are Recursive in the Given Input"
    else:
        return recurs_lett

a = checkRecursion(myInput)
print(a)


