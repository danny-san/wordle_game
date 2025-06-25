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
    unguessed_letters = []

    # Проверяем буквы на точное совпадение по их месту в слове.
    for idx, letter in enumerate(secret_letters):
        if secret_letters[idx] == player_letters[idx]:
            letters_on_screen.append(letter.upper())
            guessed_idx.append(idx)
        else:
            letters_on_screen.append('_')
            unguessed_letters.append(letter)

    # Проверяем оставшиеся буквы из догадки на их наличие в слове.
    for idx, letter in enumerate(player_letters):
        if idx in guessed_idx:
            continue

        # Если буква игрока есть в списке неугаданных букв, то вставляем
        # ее в нижнем регистре в список букв, которые появятся на экране.
        # Удаялем эту букву из списка неугаданных.
        if letter in unguessed_letters:
            letters_on_screen[idx] = letter
            unguessed_letters.pop(unguessed_letters.index(letter))

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
            attempts += 1
            print(
                f"It's not the right word. Attempts left: {TRIES - attempts}."
            )

        if attempts == TRIES:
            print(
                "Sorry, you lost this time. Please try again!\n"
                f"The word was {secret_word.upper()}."
            )
            break


if __name__ == "__main__":
    game()
