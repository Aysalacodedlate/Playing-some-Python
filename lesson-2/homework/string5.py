#Write a program that counts the number of vowels and consonants in a given string.
word = input("Write smth: ")
unli = "aioueAIOUE"
count = sum(word.count(unli) for unli in unli)
print(count)
