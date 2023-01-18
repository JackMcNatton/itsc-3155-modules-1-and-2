grade = input("Enter a grade from 0 to 100: ")
grade = int(grade)
if grade >= 90:
    print("Your grade is an A")
elif grade < 90 and grade >= 80:
    print("Your grade is a B")
elif grade < 80 and grade >= 70:
    print("Your grade is a C")
elif grade < 70 and grade >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F")
