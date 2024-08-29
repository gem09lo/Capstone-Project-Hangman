

def secret_word():
    return "HANGMAN"


answer = secret_word()


def start_hidden_answer():
    hidden_answer_blanks = []
    for i in range(len(answer)):
        hidden_answer_blanks.append("_")
    return (hidden_answer_blanks)


starting_blanks = start_hidden_answer()

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


guess = user_input()
#

letters_used = []


def store_guesses():
    letter_used = letters_used.append(guess)
    return (letters_used)


letters_used = store_guesses()
print(letters_used)
# Now find a way to loop if the letter occurs twice in the answer


def replace_blank():
    answer_letter_index = answer.find(guess)
    starting_blanks[answer_letter_index] = guess
    return (starting_blanks)


correct_letter = replace_blank()
print(correct_letter)


# FUNCTION FOR LIMITED ATTEMPTS AND TRY AGAIN IF ANSWER NOT CORRECT AND GAME OVER
