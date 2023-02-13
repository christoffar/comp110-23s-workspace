"""EX02 - one shot wordle"""
__author__ = "730606845"

secret_word: str = "python"
word_length: int = len(secret_word)
guess: str = input(f"what is your {word_length} letter guess")

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

word_index: int = 0
emoji: str = ("")
alternate_index: int = 0
variable: bool = False

while len(guess) != word_length:
    print(f"That was not {word_length} letter! Try again: ")
    guess = input(f"what is your {word_length} letter guess: ")


    while word_index < int(len(secret_word)):
        if guess[word_index] == secret_word[word_index]:
            emoji = emoji + green_box
        elif guess[word_index] != secret_word[alternate_index]:
                alternate_index = 0
                variable = False
                while alternate_index < word_length:
                    if guess[word_index] == secret_word[alternate_index]:
                        variable = True
                    alternate_index += 1
                if variable is True:
                    emoji = emoji + yellow_box
                else:
                    emoji = emoji + white_box
word_index = word_index + 1

print (emoji)

if guess != secret_word:
    print("Not quite. Play again soon! ")
if guess == secret_word:
    print("Woo You got it! ")
                