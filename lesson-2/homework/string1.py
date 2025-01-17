#Create a program to ask name and year of birth from user and tell them their age.
name = input("What is your name?")
year = int(input("Year of birth: "))
year = 2025 - year
print(f"Your name is {name} and you are {year}")