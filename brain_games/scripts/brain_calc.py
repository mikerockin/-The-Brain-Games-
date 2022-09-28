#!/usr/bin/env python3
from brain_games.games.calc import performing_operations_on_numbers
from brain_games.engine import engine
NAME_OF_GAME = 'calc'


def main():
    engine(performing_operations_on_numbers, NAME_OF_GAME)


if __name__ == '__main__':
    main()
