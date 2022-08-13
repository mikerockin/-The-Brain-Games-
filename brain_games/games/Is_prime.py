#!/usr/bin/env python3
import random
import prompt
from brain_games.Engine import engine, AMOUNT_OF_STEPS


def define_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return 'yes'
    else:
        return 'no'


def is_prime():
    count = 0
    name = engine()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != AMOUNT_OF_STEPS:
        rand_number = random.randint(1, 200)
        answer = define_prime(rand_number)
        user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
        while user_answer != 'yes' or user_answer != 'no':
            break
        if user_answer == answer:
            print('Correct!')
            count += 1
            if count == AMOUNT_OF_STEPS:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. Let's try again, {name}!")
            break
