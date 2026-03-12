#A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
#to detect these spams.

g1 = "Make a lot of money"
g2 = "buy now"
g3 = "subscribe this"
g4 = "click this"
comment = input("enter your comment: ")

if( (g1 in comment) or (g2 in comment) or (g3 in comment) or (g4 in comment)):
 print("ALERT! THIS IS A SPAM COMMENT IGNORE IT ")

else:
 print("THIS IS NOT A SPAM COMMENT") 
    