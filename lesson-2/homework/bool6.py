#Create a program that accepts a number and checks if it’s divisible by both 3 and 5
a = int(input("Write a number: "))
if a%3==0 and a%5==0:
    print("Given number is divisible by 3 and 5")
else:
    print("Not divisible")