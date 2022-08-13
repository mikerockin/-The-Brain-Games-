#!/usr/bin/env python3
import random
import prompt
from brain_games.Engine import engine, AMOUNT_OF_STEPS


def is_even():
    count = 0
    name = engine()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != AMOUNT_OF_STEPS:
        rand_number = random.randint(1, 841)
        answer = ''
        if rand_number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
        while user_answer != 'yes' or user_answer != 'no':
            break
        if answer == user_answer:
            print('Correct!')
            count += 1
            if count == AMOUNT_OF_STEPS:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. Let's try again, {name}!")
            break
