str = input("Enter a string: ")
strList = []
strLength = len(str)
counter = 0
while counter < strLength:
    tempList = []
    for i in range(0, 3):
        if (counter + i) < strLength:
            tempList.append(str[counter + i:counter + i + 1])
    counter += 3
    strList.append(tempList)
print(strList)