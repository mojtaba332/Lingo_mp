import random

def create_bingo_card(team):
    card = []
    start_number = 2 if team == 1 else 1

    for i in range(4):  # rows
        row = []
        for j in range(4):  # columns
            number = i * 4 + j + start_number
            row.append(number)
        card.append(row)

    return card

def print_bingo_card(card):
    for row in card:
        new_row = []  # will store the formatted values
        for cell in row:
            if isinstance(cell, int):  # check if number
                formatted = str(cell).rjust(2)
            else:
                formatted = cell  # if it's already a string, leave it as is
            new_row.append(formatted)
        
        # Join the row with " | " separator and print it
        print(" | ".join(new_row))
    print()
  
# mark it with (X)
def mark_card(card, number):
    for i in range(4):
        for j in range(4):
            if card[i][j] == number:
                card[i][j] = "X"


def check_bingo(card):
    # Check rows
    for row in card:
        count = 0
        for cell in row:
            if cell == "X":
                count += 1
        if count == 4:
            return True

    # Check columns
    for col in range(4):
        count = 0
        for row in card:
            if row[col] == "X":
                count += 1
        if count == 4:
            return True

    # Check main diagonal
    count = 0
    for i in range(4):
        if card[i][i] == "X":
            count += 1
    if count == 4:
        return True

    # Check anti-diagonal
    count = 0
    for i in range(4):
        if card[i][3 - i] == "X":
            count += 1
    if count == 4:
        return True

    return False

def grab_balls(team, card, green_balls, red_balls):
    if team == 1:
        number_balls = [i for i in range(2, 33, 2)]  # Even numbers for Team 1
    else:
        number_balls = [i for i in range(1, 33, 2)]  # Odd numbers for Team 2

    # Add green and red balls
    green_list = ["green"] * (3 - green_balls)
    red_list = ["red"] * (3 - red_balls)

    # Combine all balls and shuffle
    balls = number_balls + green_list + red_list
    random.shuffle(balls)

    first = balls.pop()
    print(f" First ball: {first}")
    if first == "red":
        print("Red ball! No second draw.")
        return 0, 1
    if first != "green":
        mark_card(card, first)

    second = balls.pop()
    print(f" Second ball: {second}")
    if second == "red":
        return (1 if first == "green" else 0), 1
    elif second == "green":
        return (1 if first == "green" else 0) + 1, 0
    else:
        mark_card(card, second)
        return (1 if first == "green" else 0), 0
