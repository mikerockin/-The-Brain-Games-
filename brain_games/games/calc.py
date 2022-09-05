#!/usr/bin/env python3
import random
import prompt
from brain_games.Engine import engine, AMOUNT_OF_STEPS
START_OF_RANGE_RAND_NUMBER_1 = 1
END_OF_RANGE_RAND_NUMBER_1 = 5
START_OF_RANGE_RAND_NUMBER_2 = 1
END_OF_RANGE_RAND_NUMBER_2 = 5


def performing_operations_on_numbers():
    count = 0
    name = engine()
    print('What is the result of the expression?')
    while count != AMOUNT_OF_STEPS:
        answer = ''
        rand_number_1 = random.randint(START_OF_RANGE_RAND_NUMBER_1,
                                       END_OF_RANGE_RAND_NUMBER_1)
        rand_number_2 = random.randint(START_OF_RANGE_RAND_NUMBER_2,
                                       START_OF_RANGE_RAND_NUMBER_2)
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        answer = eval(str(rand_number_1) + operator + str(rand_number_2))
        user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                        f'{operator} {rand_number_2} '))
        if user_answer == answer:
            print(f'Your answer: {user_answer}')
            print('Correct!')
            count += 1
            if count == AMOUNT_OF_STEPS:
                print(f'Congratulations, {name}!')
        else:
            print(f'Your answer: {user_answer}')
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. Let's try again, {name}!")
            break
