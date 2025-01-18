#Write a program to check if a string contains any digits.
my_str = input("Write something here: ")
#find stings length
str_length = len(my_str) #2
#2: 0,1
my_str[0]
for index in range(str_length):
    if my_str[index].isdigit() == True:
        print('My str contains a digit')