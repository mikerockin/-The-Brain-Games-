#!/usr/bin/env python3
from brain_games.games.calc import performing_operations_on_numbers
from brain_games.engine import engine


def main():
    engine(performing_operations_on_numbers,
           'What is the result of the expression?')


if __name__ == '__main__':
    main()
