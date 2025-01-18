#Ask the user for a string and replace all the vowels with a symbol (e.g., *).
my_str = str(input('Enter a string: '))
new_str = ''
length = len(my_str)
vowels = ['a','o','u','i','e']
#2
for index in range(length):
    if my_str[index] in vowels:
        new_str = new_str + '*'
    else:
        new_str = new_str + my_str[index]
    
print(new_str)

