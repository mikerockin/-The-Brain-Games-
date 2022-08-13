#!/usr/bin/env python3
import prompt
AMOUNT_OF_STEPS = 3


def engine():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name
