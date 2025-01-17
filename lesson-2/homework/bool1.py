#Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter your username ")
password = input("Enter your password ")
print(bool(username.strip()))
print(bool(password.strip()))

# Here I just checked whether the input is empty or not
# I could write an if statement as well for printing some comment to the user