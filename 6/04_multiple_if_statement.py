a = int(input("enter your age: "))

  #if elif else ladder
#is condition no. 1
if (a%2==0):
    print("a is even")

#if condition no.3
if (a >= 18): #greater than/ equal to.

    print("you are eligible to vote")
    print("you can also drive a car")

elif (a <0): #lessthan
    print("you are entering invalid age")

elif(a==0): #equal to
    print("you are entering 0 which is not a valid age")


else:
    print("you are not eligible to vote")
    

print("end of program")