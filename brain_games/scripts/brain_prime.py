#!/usr/bin/env python3
from brain_games.games.is_prime import is_prime
from brain_games.engine import engine
NAME_OF_GAME = 'is_prime'


def main():
    engine(is_prime, NAME_OF_GAME)


if __name__ == '__main__':
    main()
