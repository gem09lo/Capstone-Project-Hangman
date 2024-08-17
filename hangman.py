#python hangman.py



def secret_word():
    word = "HANGMAN"
    return word

def user_guess():
    return (input("Enter your guess: ")).upper()

def check_guess(current_guess, word):
    correct_letters = []
    for i in current_guess:
        for j in word:
            if i == j and i not in correct_letters:
                correct_letters.append(i)
    return (correct_letters)



def game():
    word = secret_word()
    guessed_letters = set()
    total_correct_letters = []

    for guess_num in range(1,4):
        guess = user_guess()
        print("Current guess: {}".format(guess))

        if guess == word:
            print("You win! The word was {}".format(word))
            break
        else:
            correct_letters = check_guess(guess, word)
            total_correct_letters.extend(correct_letters)
            print("Correct letters: {}".format(total_correct_letters))

            guessed_letters.update(list(guess))
            print("Guessed letters: {}".format(guessed_letters))
            print("Guess again \n")
    if guess != word:
        print("Game Over - You lose. The word was {}".format(word))



game()
