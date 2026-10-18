import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


# TODO-1: - Use a while loop to let the user guess again.
correct_words= []
display = placeholder

while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        correct_words.append(guess)
    display= ""
    for letter in chosen_word:
        if letter in correct_words:
            display += letter
        else:
            display += "_"

    print(display)

