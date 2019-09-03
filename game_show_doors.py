#!/usr/bin/env python3
import numpy as np


SWAP, KEEP = range(2)


def open_door(doors, your_choice):
    if doors[your_choice] is 1:
        return 1
    else:
        return 0


def gameshow_host(doors, your_choice):

    # Chooses only between 2
    drop_a_or_b = np.random.randint(2, size=1)[0]

    door_a, door_b = None, None
    for door in doors:
        if door is your_choice:
            continue
        else:
            continue

    return doors


def run_game(score, strategy=SWAP):
    doors = [0, 0, 0]

    prize_pocket = np.random.choice(range(len(doors)))

    doors[prize_pocket] = 1

    chosen_pocket = np.random.choice(range(len(doors)))

    doors = gameshow_host(doors, chosen_pocket)

    if strategy is SWAP:
        doors[chosen_pocket] = 0
        score += open_door(doors, chosen_pocket)
    else:
        score += open_door(doors, chosen_pocket)


def main(*args, **kwargs):

    games = 10

    score = 0
    for game in range(games):
        run_game(score, strategy=SWAP)
    print(f'Final score by swapping door: {100 * score / games}')

    score = 0
    for game in range(games):
        run_game(score, strategy=KEEP)
    print(f'Final score by keeping door: {100 * score / games}')


if __name__ == '__main__':
    main()
