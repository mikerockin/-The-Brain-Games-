#!/usr/bin/env python3
import prompt
import random
from brain_games.games.is_even import START_OF_RANGE_RAND_NUMBER,\
    END_OF_RANGE_RAND_NUMBER
from brain_games.games.calc import START_OF_RANGE_RAND_NUMBER_1,\
    START_OF_RANGE_RAND_NUMBER_2
from brain_games.games.calc import END_OF_RANGE_RAND_NUMBER_1,\
    END_OF_RANGE_RAND_NUMBER_2
from brain_games.games.gcd import GCD_START_OF_RANGE_RAND_NUMBER_1,\
    GCD_END_OF_RANGE_RAND_NUMBER_1
from brain_games.games.gcd import GCD_START_OF_RANGE_RAND_NUMBER_2,\
    GCD_END_OF_RANGE_RAND_NUMBER_2
from brain_games.games.is_prime import\
    PRIME_START_OF_RANGE_RAND_NUMBER, PRIME_END_OF_RANGE_RAND_NUMBER
from brain_games.games.arithm_progression import\
    END_OF_RANGE_STEP_PROGRESSION, END_OF_RANGE_ELEMENTS,\
    END_OF_RANGE_AMOUNT_OF_ELEMENTS
from brain_games.games.arithm_progression import\
    START_OF_RANGE_STEP_PROGRESSION,\
    START_OF_RANGE_ELEMENTS, START_OF_RANGE_AMOUNT_OF_ELEMENTS
AMOUNT_OF_STEPS = 3


def compares_answers(user_answer, answer, name, count):
    if user_answer == answer:
        print(f'Your answer: {user_answer}')
        print('Correct!')
        count += 1
        print(count)
        if count == AMOUNT_OF_STEPS:
            print(f'Congratulations, {name}!')
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f" "f"Correct answer was '{answer}'. Let's try again, {name}!")
    return count


def engine(Funcarg, param):
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    if param == 'is_even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
        while count != AMOUNT_OF_STEPS:
            rand_number = random.randint(START_OF_RANGE_RAND_NUMBER,
                                         END_OF_RANGE_RAND_NUMBER)
            answer = Funcarg(rand_number)
            print(answer)
            user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
            while user_answer != 'yes' or user_answer != 'no':
                break
            count = compares_answers(user_answer, answer, name, count)
    elif param == 'calc':
        print('What is the result of the expression?')
        while count != AMOUNT_OF_STEPS:
            rand_number_1 = random.randint(START_OF_RANGE_RAND_NUMBER_1,
                                           END_OF_RANGE_RAND_NUMBER_1)
            rand_number_2 = random.randint(START_OF_RANGE_RAND_NUMBER_2,
                                           END_OF_RANGE_RAND_NUMBER_2)
            operators = ['+', '-', '*']
            operator = random.choice(operators)
            answer = Funcarg(rand_number_1, rand_number_2, operator)
            print(answer)
            user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                            f'{operator} {rand_number_2} '))
            count = compares_answers(user_answer, answer, name, count)
    elif param == 'gcd':
        print('Find the greatest common divisor of given numbers.')
        while count != AMOUNT_OF_STEPS:
            rand_number_1 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_1,
                                           GCD_END_OF_RANGE_RAND_NUMBER_1)
            rand_number_2 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_2,
                                           GCD_END_OF_RANGE_RAND_NUMBER_2)
            answer = Funcarg(rand_number_1, rand_number_2)
            print(answer)
            user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                            f'{rand_number_2} '))
            count = compares_answers(user_answer, answer, name, count)
    elif param == 'is_prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no"')
        while count != AMOUNT_OF_STEPS:
            rand_number = random.randint(PRIME_START_OF_RANGE_RAND_NUMBER,
                                         PRIME_END_OF_RANGE_RAND_NUMBER)
            if Funcarg(rand_number) is True:
                answer = 'yes'
            else:
                answer = 'no'
                print(Funcarg(rand_number))
            user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
            while user_answer != 'yes' or user_answer != 'no':
                break
            count = compares_answers(user_answer, answer, name, count)
    elif param == 'prog':
        print('What number is missing in the progression?')
        while count != AMOUNT_OF_STEPS:
            progression = []
            amount_of_elements = \
                random.randint(START_OF_RANGE_AMOUNT_OF_ELEMENTS,
                               END_OF_RANGE_AMOUNT_OF_ELEMENTS)
            element = random.randint(START_OF_RANGE_ELEMENTS,
                                     END_OF_RANGE_ELEMENTS)
            step_of_progression =\
                random.randint(START_OF_RANGE_STEP_PROGRESSION,
                               END_OF_RANGE_STEP_PROGRESSION)
            answer, my_string = Funcarg(amount_of_elements, element,
                                        step_of_progression, progression)
            user_answer = int(prompt.string(f'Question: {my_string} '))
            count = compares_answers(user_answer, answer, name, count)
