import random
from lingowords import words
from game_logic import play_round
from bingo import create_bingo_card, print_bingo_card, check_bingo, grab_balls

def play_game():
    # twee teams
    teams = {
        1: {
            "card": create_bingo_card(1),
            "green_balls": 0,
            "red_balls": 0,
            "correct_words": 0,
            "wrong_streak": 0,
        },
        2: {
            "card": create_bingo_card(2),
            "green_balls": 0,
            "red_balls": 0,
            "correct_words": 0,
            "wrong_streak": 0,
        }
    }

    current_team = 1  
    print("🎮 Welcome to Lingo - Team Edition!\n")

    while True:
        print(f"\n🎯 Team {current_team}'s turn")
        print_bingo_card(teams[current_team]["card"])

        word = random.choice(words)
        print(f"hint---{word} ")
        print(f"New word! Starts with: {word[0]}")

        if play_round(word):
            teams[current_team]["correct_words"] += 1
            teams[current_team]["wrong_streak"] = 0

            g, r = grab_balls(
                current_team,
                teams[current_team]["card"],
                teams[current_team]["green_balls"],
                teams[current_team]["red_balls"]
            )
            teams[current_team]["green_balls"] += g
            teams[current_team]["red_balls"] += r
        else:
            teams[current_team]["wrong_streak"] += 1

        # Win/Lose conditions
        if teams[current_team]["green_balls"] >= 3:
            print(f"🏆 Team {current_team} wins: 3 green balls!")
            break
        elif check_bingo(teams[current_team]["card"]):
            print(f"🏆 Team {current_team} wins: Bingo!")
            break
        elif teams[current_team]["correct_words"] >= 10:
            print(f"🏆 Team {current_team} wins: 10 correct words!")
            break
        elif teams[current_team]["red_balls"] >= 3:
            print(f"💥 Team {current_team} loses: 3 red balls.")
            break
        elif teams[current_team]["wrong_streak"] >= 3:
            print(f"💥 Team {current_team} loses: 3 wrong guesses.")
            break

        # Switch teams
    if current_team == 1:
        current_team = 2
    else:
        current_team = 1

    again = input("Play again? (y/n): ").lower()
    if again == 'y':
        play_game()
    else:
        print("👋 Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
