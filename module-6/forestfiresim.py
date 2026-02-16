##Brady Heinz 6.2 Assignment 2/15/2026

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'w'   # <-- Matches your screenshot (blue w's)

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# Lake size (tall rectangle like your example):
LAKE_WIDTH = 6
LAKE_HEIGHT = 12

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue

                # Water never changes (permanent firebreak).
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space (but never on water).
                    nextForest[(x, y)] = TREE

                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Fire spreads to neighboring trees (not water).
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            nx = x + ix
                            ny = y + iy
                            if forest.get((nx, ny)) == TREE:
                                nextForest[(nx, ny)] = FIRE

                    # Burned tree becomes empty:
                    nextForest[(x, y)] = EMPTY

                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    # Create random starting forest:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    # Add a lake
    addLake(forest)
    return forest


def addLake(forest):
    cx = WIDTH // 2
    cy = HEIGHT // 2

    left = max(0, cx - LAKE_WIDTH // 2)
    right = min(WIDTH - 1, left + LAKE_WIDTH - 1)

    top = max(0, cy - LAKE_HEIGHT // 2)
    bottom = min(HEIGHT - 1, top + LAKE_HEIGHT - 1)

    for x in range(left, right + 1):
        for y in range(top, bottom + 1):
            forest[(x, y)] = WATER


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            tile = forest[(x, y)]

            if tile == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif tile == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif tile == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                # Reset so colors don't bleed into empty spaces:
                bext.fg('reset')
                print(EMPTY, end='')
        print()

    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
