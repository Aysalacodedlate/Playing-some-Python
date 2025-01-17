#Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter your username ")
password = input("Enter your password ")
print(bool(username.strip()))
print(bool(password.strip()))
