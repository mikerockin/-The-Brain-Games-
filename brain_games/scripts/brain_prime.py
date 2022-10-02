#!/usr/bin/env python3
from brain_games.games.is_prime import prime
from brain_games.engine import engine


def main():
    engine(prime,
           'Answer "yes" if given number is prime.'' Otherwise answer "no"')


if __name__ == '__main__':
    main()
