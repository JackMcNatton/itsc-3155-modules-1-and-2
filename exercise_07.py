userHasQuit = False
allNumsList = []
evenNumsList = []
while userHasQuit == False:
    entry = input("Enter a number or QUIT to quit: ")
    if entry == "QUIT":
        userHasQuit = True
        break
    entry = int(entry)
    allNumsList.append(entry)
    if entry % 2 == 0:
        evenNumsList.append(entry)
print(allNumsList)
print(evenNumsList)