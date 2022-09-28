#!/usr/bin/env python3
from brain_games.games.arithm_progression import calculates_arithm_progression
from brain_games.engine import engine
NAME_OF_GAME = 'prog'


def main():
    engine(calculates_arithm_progression, NAME_OF_GAME)


if __name__ == '__main__':
    main()
