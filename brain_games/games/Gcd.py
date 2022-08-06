#!/usr/bin/env python3
import prompt
import random


def gcd():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print('Find the greatest common divisor of given numbers.')
    while count != 3:
        answer = ''
        rand_number_1 = random.randint(1, 20)
        rand_number_2 = random.randint(20, 60)
        user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                        f'{rand_number_2} '))
        while rand_number_1 != 0 and rand_number_2 != 0:
            if rand_number_1 > rand_number_2:
                rand_number_1 = rand_number_1 % rand_number_2
            else:
                rand_number_2 = rand_number_2 % rand_number_1
        answer = rand_number_1 + rand_number_2
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
