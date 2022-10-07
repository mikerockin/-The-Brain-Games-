#!/usr/bin/env python3
from brain_games.games.is_prime import prime, RULES_OF_GAME
from brain_games.engine import engine


def main():
    engine(prime, RULES_OF_GAME)


if __name__ == '__main__':
    main()
