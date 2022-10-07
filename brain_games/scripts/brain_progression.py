#!/usr/bin/env python3
from brain_games.games.arithm_progression import calculates_arithm_progression,\
    RULES_OF_GAME
from brain_games.engine import engine


def main():
    engine(calculates_arithm_progression, RULES_OF_GAME)


if __name__ == '__main__':
    main()
