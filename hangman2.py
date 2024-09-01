import random


def secret_word():
    word_list = []
    with open('christmas_theme_words.txt') as f:
        file_data = f.read()
        for word in file_data:
            word_list.append(word.upper())
        word_list = "".join(word_list).split()
    return random.choice(word_list)


def start_hidden_answer(answer):
    hidden_answer_blanks = []
    for i in range(len(answer)):
        hidden_answer_blanks.append("_")
    return (hidden_answer_blanks)

# After create function to store all used letters: validate by checking if user has used the letter already


def user_input():
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("You can only guess one letter - Try again!")
        # elif guess in letters_used:
            # print("You\'ve already guessed that letter - try again!")
            continue
        else:
            return guess


def main():
    # initial set-up
    answer = secret_word()
    starting_blanks = start_hidden_answer(answer)
    letters_used = set()
    print(f"Welcome to a game of hangman! \nGuess this word: {
          starting_blanks} \n")

    # main
    lives = 3
    while lives > 0:
        guess = user_input()
        letters_used.add(guess)

        if guess not in answer:
            lives -= 1
            print(f"Wrong letter try again! You have {lives} lives left")
        else:
            for i, letter in enumerate(answer):
                if letter == guess:
                    starting_blanks[i] = answer[i]
            print(f"You\'ve got a letter! You still have {lives} lives left")
        print(f"Letters used: {letters_used} \nStarting blanks: {
              starting_blanks} \n")

        if starting_blanks == list(answer):
            print(f"You won! The word was {answer}")
            break

    # End game
    if starting_blanks != list(answer):
        print(f"Game over - The word was {answer}")


main()
