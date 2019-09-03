#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

SWAP, KEEP = range(2)


def open_door(doors, your_choice):
    if doors[your_choice] == 1:
        return 1
    else:
        return 0


def gameshow_host(doors, your_choice):
    # Chooses only between 2
    a_or_b = np.random.randint(2, size=1)[0]

    doors_you_can_close = []

    for i, door in enumerate(doors):
        if i == your_choice: continue
        if door == 1: continue
        doors_you_can_close.append(i)

    if len(doors_you_can_close) is 1:
        doors[doors_you_can_close[0]] = -1
    else:
        doors[doors_you_can_close[a_or_b]] = -1
    return doors


def next_available_door_index(doors, your_choice):

    door_you_can_change_to = None

    for i, door in enumerate(doors):
        if i == your_choice: continue
        if door == -1: continue
        door_you_can_change_to = i

    return door_you_can_change_to


def run_game(strategy=SWAP):

    # We set the game
    doors = [0, 0, 0]
    prize_pocket = np.random.choice(range(len(doors)))
    doors[prize_pocket] = 1

    # Now you chose which door you would like
    chosen_pocket = np.random.choice(range(len(doors)))

    # Now the gameshow host opens an empty door
    doors = gameshow_host(doors, chosen_pocket)

    score = 0
    if strategy is SWAP:
        new_door = next_available_door_index(doors, chosen_pocket)
        doors[chosen_pocket] = 0
        chosen_pocket = new_door
        score += open_door(doors, chosen_pocket)
    else:
        score += open_door(doors, chosen_pocket)
    return score


def main(*args, **kwargs):

    games = 10000

    score = 0
    pct_score = []
    for game in range(games):
        score += run_game(strategy=SWAP)
        pct_score.append(100 * score / games)
    print(f'\nSuccess rate by swapping door: {100 * score / games}%')

    score = 0
    pct_score = []
    for game in range(games):
        score += run_game(strategy=KEEP)
        pct_score.append(100 * score / games)
    print(f'Success rate by keeping door: {100 * score / games}%')

    # Plot results
    # plt.plot( range(games), pct_score, 'go--', linewidth=2, markersize=12)
    # plt.show()


if __name__ == '__main__':
    main()
