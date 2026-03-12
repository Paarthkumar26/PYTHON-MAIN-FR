# Write a program to find the greatest of four numbers entered by the user.

a = int(input("enter number1 : "))
b = int(input("enter number2 : "))
c = int(input("enter number3 : "))
d = int(input("enter number4 : "))

if (a > b and a > c and a > d):
    print("a is greatest")

elif (b > a and b > c and b > d):
    print("b is greatest")

elif (c> a and c > b and c >d ):
    print("c is greatest")

else:
    print("d is greatest")