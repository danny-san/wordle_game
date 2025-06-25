import random

from words import WORDS_5


WORD_LENGTH = 5
TRIES = 6


def generate_word() -> str:
    return random.choice(WORDS_5)


def check_guess(player_word, secret_word) -> int:
    player_letters = [letter.lower() for letter in player_word]
    secret_letters = [letter.lower() for letter in secret_word]
    letters_on_screen = []
    guessed_idx = []

    for idx, letter in enumerate(secret_letters):
        if secret_letters[idx] == player_letters[idx]:
            letters_on_screen.append(letter.upper())
            guessed_idx.append(idx)
        else:
            letters_on_screen.append('_')

    print(' '.join(letters_on_screen), "\n")

    return len(guessed_idx)


def game():
    attempts = 0
    secret_word = generate_word()

    while True:
        player_word = input(f"Please enter a {WORD_LENGTH} letter word: ")
        number_of_guessed = check_guess(player_word, secret_word)
        if number_of_guessed == WORD_LENGTH:
            print("You are right!")
            break
        else:
            print("It's not the right word.\n")
            attempts += 1

        if attempts == TRIES:
            print("Sorry, you lost this time. Please try again!")
            break


if __name__ == "__main__":
    game()
