#Ask the user for a string and replace all the vowels with a symbol (e.g., *).
abc = input("Write a string pls: ")
abc1 = abc.strip("a, i, o, u, e")
abc3 = ("*")
abc2 = abc.replace(f"{abc1}", f"{abc3}")
print(abc)
