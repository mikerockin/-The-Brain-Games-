#!/usr/bin/env python3
import random
import prompt


def brain_calc():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print('What is the result of the expression?')
    while count != 3:
        answer = ''
        rand_number_1 = random.randint(1, 5)
        rand_number_2 = random.randint(1, 5)
        operators = ('+', '-', '*')
        operator = random.choice(operators)
        if operator == '+':
            answer = rand_number_1 + rand_number_2
        elif operator == '-':
            answer = rand_number_1 - rand_number_2
        elif operator == '*':
            answer = rand_number_1 * rand_number_2
        user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                        f'{operator} {rand_number_2} '))
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
