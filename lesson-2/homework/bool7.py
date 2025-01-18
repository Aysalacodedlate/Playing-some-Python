#Write a program that checks if the sum of two numbers is greater than 50.8. 
#Create a program that checks if a given number is between 10 and 20 (inclusive)
mynum = int(input("Write a number: "))
if mynum > 50.8:
    print ("Voy tovba")
else:
    print ("Come on")

#I don't know why, but it's giving the opposite answers. 
#Should I have to convert the num to boolean?
#let's this out:

mynum = bool(input("Write a number: "))
if mynum > 50.8:
    print ("Voy tovba")
else:
    print ("Come on")

#ou yes, it is working correctly now. so the problem was the number types. i see