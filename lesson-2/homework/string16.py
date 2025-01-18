#Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.
a = input("Write a string: ")
b = input("Write a character for removing: ")
result = a.replace(b, "")
print(result)
