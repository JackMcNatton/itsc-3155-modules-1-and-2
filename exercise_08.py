list = []
for i in range(0, 10):
    val = (int)(input("Enter number " + str(i + 1) + ": "))
    list.append(val)
uniqueList = []
for i in range(0, 10):
    val = list[i]
    valIsUnique = True
    for j in range(0, 10):
        if val == list[j] and j != i:
            valIsUnique = False
    if valIsUnique == True:
        uniqueList.append(val)
print("Original List: ",list)
print("Numbers That Appear Once: ",uniqueList)