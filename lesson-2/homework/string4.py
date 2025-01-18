#Write a Python program to check if a given string is palindrome or not.
#What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
text = input ("Try to write someething that is palindrome " )
if (text == text[::-1]):
    print("Aha, this is palindrome")
else:
    print("O no, this is not a palindrome")