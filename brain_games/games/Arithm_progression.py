#!/usr/bin/env python3
import random
import prompt


def arithm_progression():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print('What number is missing in the progression?')
    while count != 3:
        progression = []
        amount_of_elements = random.randint(5, 10)
        element = random.randint(1, 34)
        step_of_progression = random.randint(2, 8)
        for i in range(amount_of_elements):
            element += step_of_progression
            progression.append(element)
        random_number = random.choice(progression)
        index_of_random_number = progression.index(random_number)
        progression[index_of_random_number] = '...'
        answer = random_number
        user_answer = int(prompt.string(f'Question: {progression} '))
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
