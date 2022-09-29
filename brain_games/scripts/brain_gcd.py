#!/usr/bin/env python3
from brain_games.games.gcd import calculates_gcd
from brain_games.engine import engine


def main():
    engine(calculates_gcd)


if __name__ == '__main__':
    main()
