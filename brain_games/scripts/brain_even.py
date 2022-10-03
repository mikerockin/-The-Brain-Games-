#!/usr/bin/env python3
from brain_games.games.is_even import even
from brain_games.engine import engine


def main():
    engine(even, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
