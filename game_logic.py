# game_logic.py
from colorama import Fore, Style

def color_text(letter, color):
    if color == "green":
        return f"{Fore.GREEN}{letter.upper()}{Style.RESET_ALL}"
    elif color == "yellow":
        return f"{Fore.YELLOW}{letter.upper()}{Style.RESET_ALL}"
    else:
        return letter.upper()

def play_round(secret_word):
    attempts = 5
    correct = False
    revealed = [secret_word[0]] + ['_'] * (len(secret_word) - 1)

    for attempt in range(attempts):
        print(f"\nKnown so far: {' '.join(revealed)}")
        guess = input(f"Attempt {attempt + 1} - Word starting with '{secret_word[0]}': ").lower()

        if len(guess) != 5 or guess[0] != secret_word[0]:
            print(" Invalid guess. Must be 5 letters and start with the correct letter.")
            continue

        result = ""
        for i in range(5):
            if guess[i] == secret_word[i]:
                result += color_text(guess[i], "green")
                revealed[i] = guess[i]
            elif guess[i] in secret_word:
                result += color_text(guess[i], "yellow")
            else:
                result += guess[i].upper()

        print("Result:", result)

        if guess == secret_word:
            print("✅ Correct word!")
            correct = True
            break
    return correct
