#!/usr/bin/env python3
import random
import prompt
from brain_games.Engine import engine, AMOUNT_OF_STEPS


def arithm_progression():
    count = 0
    name = engine()
    print('What number is missing in the progression?')
    while count != AMOUNT_OF_STEPS:
        progression = []
        amount_of_elements = random.randint(5, 10)
        element = random.randint(1, 34)
        step_of_progression = random.randint(2, 8)
        for i in range(amount_of_elements):
            element += step_of_progression
            progression.append(element)
        random_number = random.choice(progression)
        index_of_random_number = progression.index(random_number)
        progression[index_of_random_number] = '..'
        answer = random_number
        my_string = " ".join(map(str, progression))
        user_answer = int(prompt.string(f'Question: {my_string} '))
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
