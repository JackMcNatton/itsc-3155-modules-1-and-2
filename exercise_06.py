row = int(input("Enter a row number from 1 to 5: "))
column = int(input("Enter a column number from 1 to 5: "))
rowCounter = 1
while rowCounter <= 5:
    if rowCounter == row:
        rowString = ""
        columnCounter = 1
        while columnCounter <= 5:
            if columnCounter == column:
                rowString += "1 "
            else: 
                rowString += "0 "
            columnCounter += 1
        print(rowString)
    else: 
        print("0 0 0 0 0")
    rowCounter += 1
