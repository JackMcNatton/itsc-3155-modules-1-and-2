list = []
numsNeeded = int(input("Enter a number: "))
i = 1
sum = 0
while i <= numsNeeded:
    entry = input("Enter number " + str(i) + ": ")
    list.append(entry)
    sum = sum  + int(entry)
    i += 1
average = sum/numsNeeded
print(list)
print(average)