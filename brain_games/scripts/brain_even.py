#!/usr/bin/env python3
from brain_games.games.is_even import is_even
from brain_games.engine import engine
NAME_OF_GAME = 'is_even'


def main():
    engine(is_even, NAME_OF_GAME)


if __name__ == '__main__':
    main()
