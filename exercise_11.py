str = input("Enter a String: ")
counter = len(str)
reverseStr = ""
while counter > -1:
    reverseStr += str[counter - 1:counter]
    counter -= 1
print(reverseStr)