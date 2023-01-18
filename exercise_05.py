num1 = (int)(input("Enter a number for the first list: "))
num2 = (int)(input("Enter a number for the first list: "))
num3 = (int)(input("Enter a number for the first list: "))
num4 = (int)(input("Enter a number for the first list: "))
num5 = (int)(input("Enter a number for the first list: "))
list1 = [num1, num2, num3, num4, num5]
num6 = (int)(input("Enter a number for the second list: "))
num7 = (int)(input("Enter a number for the second list: "))
num8 = (int)(input("Enter a number for the second list: "))
num9 = (int)(input("Enter a number for the second list: "))
num10 = (int)(input("Enter a number for the second list: "))
list2 = [num6, num7, num8, num9, num10]
commonList = []
for i in range(0, len(list1)):
    for j in range(0, len(list2)):
        if list1[i] == list2[j]:
            alreadyInList = False
            for k in range(0, len(commonList)):
                if list1[i] == commonList[k]:
                    alreadyInList = True
            if alreadyInList == False:
                commonList.append(list1[i])
print(list1)
print(list2)
print(commonList)