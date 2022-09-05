#!/usr/bin/env python3
import random
import prompt
from brain_games.Engine import engine, AMOUNT_OF_STEPS
START_OF_RANGE_RAND_NUMBER = 1
END_OF_RANGE_RAND_NUMBER = 200
DEVIDER = 2


def is_prime(n):
    DEVIDER = 2
    while DEVIDER * DEVIDER <= n and n % DEVIDER != 0:
        DEVIDER += 1
    return DEVIDER * DEVIDER > n


def ask_user_is_prime():
    count = 0
    name = engine()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != AMOUNT_OF_STEPS:
        rand_number = random.randint(START_OF_RANGE_RAND_NUMBER,
                                     END_OF_RANGE_RAND_NUMBER)
        if is_prime(rand_number) is True:
            answer = 'yes'
        else:
            answer = 'no'
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
