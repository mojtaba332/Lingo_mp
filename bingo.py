# bingo.py
import random

def create_bingo_card(team):
    return [[(i * 4 + j + (2 if team == 1 else 1)) for j in range(4)] for i in range(4)]

def print_bingo_card(card):
    for row in card:
        print(" | ".join(str(cell).rjust(2) if isinstance(cell, int) else cell for cell in row))
    print()

def mark_card(card, number):
    for i in range(4):
        for j in range(4):
            if card[i][j] == number:
                card[i][j] = "X"

def check_bingo(card):
    for row in card:
        if all(cell == "X" for cell in row):
            return True
    for col in range(4):
        if all(row[col] == "X" for row in card):
            return True
    if all(card[i][i] == "X" for i in range(4)) or all(card[i][3 - i] == "X" for i in range(4)):
        return True
    return False

def grab_balls(team, card, green_balls, red_balls):
    balls = (
        [i for i in range(1, 33) if i % 2 == (1 if team == 2 else 0)] +
        ["green"] * (3 - green_balls) +
        ["red"] * (3 - red_balls)
    )
    random.shuffle(balls)

    first = balls.pop()
    print(f"🎱 First ball: {first}")
    if first == "red":
        print("❌ Red ball! No second draw.")
        return 0, 1
    if first != "green":
        mark_card(card, first)

    second = balls.pop()
    print(f"🎱 Second ball: {second}")
    if second == "red":
        return (1 if first == "green" else 0), 1
    elif second == "green":
        return (1 if first == "green" else 0) + 1, 0
    else:
        mark_card(card, second)
        return (1 if first == "green" else 0), 0
