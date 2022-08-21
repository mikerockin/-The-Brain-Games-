#!/usr/bin/env python3
import random
import prompt
from brain_games.Engine import engine, AMOUNT_OF_STEPS
START_OF_RANGE_AMOUNT_OF_ELEMENTS = 5
END_OF_RANGE_AMOUNT_OF_ELEMENTS = 10
START_OF_RANGE_ELEMENTS = 1
END_OF_RANGE_ELEMENTS = 34
START_OF_RANGE_STEP_PROGRESSION = 2
END_OF_RANGE_STEP_PROGRESSION = 2

def calculates_arithm_progression():
    count = 0
    name = engine()
    print('What number is missing in the progression?')
    while count != AMOUNT_OF_STEPS:
        progression = []
        amount_of_elements = random.randint(START_OF_RANGE_AMOUNT_OF_ELEMENTS, END_OF_RANGE_AMOUNT_OF_ELEMENTS)
        element = random.randint(START_OF_RANGE_ELEMENTS, END_OF_RANGE_ELEMENTS)
        step_of_progression = random.randint(START_OF_RANGE_STEP_PROGRESSION, END_OF_RANGE_STEP_PROGRESSION)
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
