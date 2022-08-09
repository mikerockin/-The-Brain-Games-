#!/usr/bin/env python3
import random
import prompt

list_of_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                 89, 97, 101, 103, 107, 109, 113, 127, 131,
                 137, 139, 149, 151, 157, 163, 167,
                 173, 179, 181, 191, 193, 197, 199]


def is_prime():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != 3:
        rand_number = random.randint(1, 200)
        for x in [list_of_prime]:
            if rand_number in x:
                answer = 'yes'
            else:
                answer = 'no'
        user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
        while user_answer != 'yes' or user_answer != 'no':
            break
        if user_answer == answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. Let's try again, {name}!")
            break
