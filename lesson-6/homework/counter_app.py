#Ohhh, this is gonna be hard, I guessss


import os
import string
from collections import Counter

def create_sample_file():
    print("'sample.txt' does not exist. Please create it by writing a paragraph:")
    with open("sample.txt", "w") as f:
        text = input("Write text for the file: ")
        f.write(text)
    print("'sample.txt' created successfully.")

def clean_text(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower()

def count_words(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    cleaned_content = clean_text(content)
    words = cleaned_content.split()

    
#need to continue understanding