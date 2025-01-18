#Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
sentc = input("Write a sentence: ")
sentc2 = input("Remove the word: ")
sentc3 = input("Replace with: ")
a = sentc.replace(f"{sentc2}", f"{sentc3}")
print(a)

#I could not understand the logic of this problem so it might look meaningless. 
#How do I know which word should I replace from the input?
#Ya'ni won't the grammar go wrong instantly?
