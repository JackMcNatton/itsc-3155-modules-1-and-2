str = input("Enter a String: ")
newStr = ""
counter = 0
while counter < len(str):
    currentLetter = str[counter:counter + 1]
    if currentLetter.islower():
        newStr += currentLetter
    counter += 1
counter = 0
while counter < len(str):
    currentLetter = str[counter:counter + 1]
    if currentLetter.isupper():
        newStr += currentLetter
    counter += 1
print(newStr)