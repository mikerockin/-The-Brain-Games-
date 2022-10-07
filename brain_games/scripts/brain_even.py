#!/usr/bin/env python3
from brain_games.games.is_even import even, RULES_OF_GAME
from brain_games.engine import engine


def main():
    engine(even, RULES_OF_GAME)


if __name__ == '__main__':
    main()
