#!/usr/bin/env python3
import prompt
import random
from brain_games.Engine import engine, AMOUNT_OF_STEPS
START_OF_RANGE_RAND_NUMBER_1 = 1
END_OF_RANGE_RAND_NUMBER_1 = 20
START_OF_RANGE_RAND_NUMBER_2 = 20
END_OF_RANGE_RAND_NUMBER_2 = 50


def calculates_gcd(rand_number_1, rand_number_2):
    while rand_number_1 != 0 and rand_number_2 != 0:
        if rand_number_1 > rand_number_2:
            rand_number_1 = rand_number_1 % rand_number_2
        else:
            rand_number_2 = rand_number_2 % rand_number_1
    return rand_number_1 + rand_number_2


def ask_user_gcd():
    count = 0
    name = engine()
    print('Find the greatest common divisor of given numbers.')
    while count != AMOUNT_OF_STEPS:
        rand_number_1 = random.randint(START_OF_RANGE_RAND_NUMBER_1,
                                       END_OF_RANGE_RAND_NUMBER_1)
        rand_number_2 = random.randint(START_OF_RANGE_RAND_NUMBER_2,
                                       END_OF_RANGE_RAND_NUMBER_2)
        user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                        f'{rand_number_2} '))
        answer = calculates_gcd(rand_number_1, rand_number_2)
        if user_answer == answer:
            print(f'Your answer: {user_answer}')
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'Your answer: {user_answer}')
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. Let's try again, {name}!")
            break
