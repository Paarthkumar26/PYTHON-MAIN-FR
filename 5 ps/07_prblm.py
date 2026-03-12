#If the names of 2 friends are same; what will happen to the program in problem
#6?


d  = {} 
name = input("enter freinds name1: ")
lang = input("enter language name: ")

d.update({name:lang})
name = input("enter freinds name2: ")
lang = input("enter language name: ")

d.update({name:lang})
name = input("enter freinds name3: ")
lang = input("enter language name: ")

d.update({name:lang})
name = input("enter freinds name4: ")
lang = input("enter language name: ")

d.update({name:lang})
 
print(d)
