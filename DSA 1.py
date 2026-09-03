Prob 1 : Write a program that takes an integer, then a string, then a char from the user and prints them in the screen.

a = int(input("enter the number : "))
b = input("enter the name : ")
c = input("enter tha character : ")
print(a)
print(b)
print(c)


Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.

a=int(input("enter a = "))
b=int(input("enter b = "))
c=int(input("enter c = "))
triangle = a+b+c
if triangle==180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")


Prob 3: 

Given mark of student, Print the Grade
Grade A if mark is greater than or equal to 90
Grade B if mark is greater than or equal to 80
Grade C if mark if greater than or equal to 60
Grade D if mark if greater than or equal to 35
Fail if mark is lesser than 35

mark = int(input("enter the mark = "))
if mark>=90:
    print("Grade A")
elif mark>=80:
    print("Grade B")
elif mark>=60:
    print("Grade C")
elif mark>=35:
    print("Grade B")
elif mark<35:
    print("Fail")


Prob 4: Write a program using switch case which takes a value and prints the respective Size.
If size is 29 then its small
If size is 30 then its Medium
If size is 38 then its Large
If size is 42 then its XLarge
If size is not any of the above then Invalid.

size = int(input())

match size:
    case 29:
        print("Small")
    case 30:
        print("Medium")
    case 38:
        print("Large")
    case 42:
        print("XLarge")
    case _:
        print("Invalid")




