"""EXO1 - Chardle - Walmart Wordle"""
__author__ = "730606845"
word: str = (input("Enter a five character word:  "))
if (len(word) !=5):
    print("Error: Word must contain five characters")
    exit()
letter: str = (input("Enter a single charachter: "))
if (len(letter) != 1):
    print("Error: Character must be a single character")
    exit()


count: int = 0
print("searching for " + letter + " in " + word)

if (letter == word [0]):
    print(letter + " found at index 0 ")
    count = count + 1
if (letter == word [1]):
    print(letter + " found at index 1 ")
    count = count + 1
if (letter == word [2]):
    print(letter + " found at index 2 ")
    count = count + 1
if (letter == word [3]):
    print(letter + " found at index 3 ")
    count = count + 1
if (letter == word [4]):
    print(letter + " found at index 4 ")
    count = count + 1


if (count == 1):
    print("1 instance of " + letter + " found in " + word)
if (count == 0):
    print("No instances of " + letter + " found in " + word)
if (count >= 2):
    print(str(count) + " instances of " + letter + " found in " + word)