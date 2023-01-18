str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
isSuffix = False
if str1.endswith(str2) or str2.endswith(str1):
    isSuffix = True
print(isSuffix)