#!/usr/bin/env python3
import numpy as np


SWAP, KEEP = range(2)


def open_door(doors: list, your_choice: int) -> int:
    if doors[your_choice] == 1: return 1
    else: return 0


def gameshow_host(doors: list, your_choice: int) -> list:
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


def next_available_door_index(doors: list, your_choice: int) -> int:
    door_you_can_change_to = None
    for i, door in enumerate(doors):
        if i == your_choice: continue
        if door == -1: continue
        door_you_can_change_to = i
    return door_you_can_change_to


def run_single_game(strategy: int) -> int:
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


def run_games(num_games: int, strategy: int) -> float:
    score = 0
    for game in range(num_games):
        score += run_single_game(strategy)
    pct_score = 100 * score / num_games

    if strategy is SWAP: text = 'swapping'
    else: text = 'keeping'

    print(f'Success rate by {text} door: {pct_score}%')
    return pct_score


def main():

    num_games = 100000
    aggregate = 0.

    print('')
    aggregate += run_games(num_games, strategy=SWAP)
    aggregate += run_games(num_games, strategy=KEEP)

    print(f'Error: {round(abs(100 - aggregate), 3)}%')


if __name__ == '__main__':
    main()
