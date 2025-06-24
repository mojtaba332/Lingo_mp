# main.py
import random
from lingowords import words
from game_logic import play_round
from bingo import create_bingo_card, print_bingo_card, check_bingo, grab_balls

def play_game():
    team = 2  # You can later add team switch
    correct_words = 0
    wrong_streak = 0
    green_balls = 0
    red_balls = 0
    card = create_bingo_card(team)

    print("🎮 Welcome to Lingo!\n")

    while True:
        print_bingo_card(card)
        word = random.choice(words)
        print(f"New word! Starts with: {word[0]}")

        if play_round(word):
            correct_words += 1
            wrong_streak = 0
            g, r = grab_balls(team, card, green_balls, red_balls)
            green_balls += g
            red_balls += r
        else:
            wrong_streak += 1

        # Check win/lose
        if green_balls >= 3:
            print("Win: 3 green balls!")
            break
        elif check_bingo(card):
            print("Win: Bingo!")
            break
        elif correct_words >= 10:
            print("Win: 10 correct words!")
            break
        elif red_balls >= 3:
            print("Lose: 3 red balls.")
            break
        elif wrong_streak >= 3:
            print("Lose: 3 wrong guesses.")
            break

    again = input("Play again? (y/n): ").lower()
    if again == 'y':
        play_game()
    else:
        print("👋 Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
