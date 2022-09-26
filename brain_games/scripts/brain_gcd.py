#!/usr/bin/env python3
from brain_games.games.gcd import calculates_gcd
from brain_games.Engine import engine
NAME_OF_GAME = 'gcd'


def main():
    engine(calculates_gcd, NAME_OF_GAME)


if __name__ == '__main__':
    main()
