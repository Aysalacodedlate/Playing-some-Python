#Write a program that asks the user for a sentence and prints the number of words in it.
my_str = input("Write a sentence ")

# my_str = my_str.strip()

a = my_str.split(" ") 
print(a)
result = ""
for a in my_str:
   