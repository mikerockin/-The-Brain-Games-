#!/usr/bin/env python3
from brain_games.games.calc import performing_operations_on_numbers,\
    RULES_OF_GAME
from brain_games.engine import engine


def main():
    engine(performing_operations_on_numbers, RULES_OF_GAME)


if __name__ == '__main__':
    main()
