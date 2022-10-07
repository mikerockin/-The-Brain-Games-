#!/usr/bin/env python3
from brain_games.games.gcd import calculates_gcd, RULES_OF_GAME
from brain_games.engine import engine


def main():
    engine(calculates_gcd, RULES_OF_GAME)


if __name__ == '__main__':
    main()
