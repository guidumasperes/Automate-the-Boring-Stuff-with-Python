#This program searches for a specific word typed by the user in .txt files
#in a folder, and then returns the name of these files where the word was
#founded.

import os

print("Write your word: ")
desired_word = input()

path = "C:\\Users\\Gui\\Desktop\\MyPythonScripts\\Lessons recaps"
files = os.listdir(path)

founded_files = []

for file in files:
    complete_path = path + "\\" + file
    with open(complete_path, "r") as txt_file:
        for line in txt_file:
            for word in line.split():
                if word == desired_word and file not in founded_files:
                    founded_files.append(file)

if len(founded_files) == 1:
    print("Your word is in this file:")
elif len(founded_files) > 1:
    print("Your word are in these files:")
else:
    print("Your word isn't in any file.")

for file in founded_files:
    print(file)
    
    
