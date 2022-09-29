import prompt
import random
from brain_games.games.is_even import START_OF_RANGE_RAND_NUMBER,\
    END_OF_RANGE_RAND_NUMBER, is_even
from brain_games.games.calc import START_OF_RANGE_RAND_NUMBER_1,\
    START_OF_RANGE_RAND_NUMBER_2, performing_operations_on_numbers
from brain_games.games.calc import END_OF_RANGE_RAND_NUMBER_1,\
    END_OF_RANGE_RAND_NUMBER_2
from brain_games.games.gcd import GCD_START_OF_RANGE_RAND_NUMBER_1,\
    GCD_END_OF_RANGE_RAND_NUMBER_1
from brain_games.games.gcd import GCD_START_OF_RANGE_RAND_NUMBER_2,\
    GCD_END_OF_RANGE_RAND_NUMBER_2, calculates_gcd
from brain_games.games.is_prime import\
    PRIME_START_OF_RANGE_RAND_NUMBER, PRIME_END_OF_RANGE_RAND_NUMBER, is_prime
from brain_games.games.arithm_progression import\
    END_OF_RANGE_STEP_PROGRESSION, END_OF_RANGE_ELEMENTS,\
    END_OF_RANGE_AMOUNT_OF_ELEMENTS, calculates_arithm_progression
from brain_games.games.arithm_progression import\
    START_OF_RANGE_STEP_PROGRESSION,\
    START_OF_RANGE_ELEMENTS, START_OF_RANGE_AMOUNT_OF_ELEMENTS
AMOUNT_OF_STEPS = 3


def engine(returns_answer):
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    while count != AMOUNT_OF_STEPS:
        if returns_answer == is_even:
            rand_number = random.randint(START_OF_RANGE_RAND_NUMBER,
                                         END_OF_RANGE_RAND_NUMBER)
            answer = returns_answer(rand_number, count)
            user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
        elif returns_answer == performing_operations_on_numbers:
            rand_number_1 = random.randint(START_OF_RANGE_RAND_NUMBER_1,
                                           END_OF_RANGE_RAND_NUMBER_1)
            rand_number_2 = random.randint(START_OF_RANGE_RAND_NUMBER_2,
                                           END_OF_RANGE_RAND_NUMBER_2)
            operators = ['+', '-', '*']
            operator = random.choice(operators)
            answer = returns_answer(rand_number_1, rand_number_2,
                                    operator, count)
            user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                            f''f'{operator} {rand_number_2} '))
        elif returns_answer == calculates_gcd:
            rand_number_1 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_1,
                                           GCD_END_OF_RANGE_RAND_NUMBER_1)
            rand_number_2 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_2,
                                           GCD_END_OF_RANGE_RAND_NUMBER_2)
            answer = returns_answer(rand_number_1, rand_number_2, count)
            user_answer = int(prompt.string(f'Question: {rand_number_1}'
                                            f' 'f'{rand_number_2} '))
        elif returns_answer == is_prime:
            rand_number = random.randint(PRIME_START_OF_RANGE_RAND_NUMBER,
                                         PRIME_END_OF_RANGE_RAND_NUMBER)
            if returns_answer(rand_number, count) is True:
                answer = 'yes'
            else:
                answer = 'no'
            user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
        elif returns_answer == calculates_arithm_progression:
            progression = []
            amount_of_elements = \
                random.randint(START_OF_RANGE_AMOUNT_OF_ELEMENTS,
                               END_OF_RANGE_AMOUNT_OF_ELEMENTS)
            element = random.randint(START_OF_RANGE_ELEMENTS,
                                     END_OF_RANGE_ELEMENTS)
            step_of_progression = \
                random.randint(START_OF_RANGE_STEP_PROGRESSION,
                               END_OF_RANGE_STEP_PROGRESSION)
            answer, my_string = returns_answer(amount_of_elements,
                                               element, step_of_progression,
                                               progression, count)
            user_answer = int(prompt.string(f'Question: {my_string} '))
        if user_answer == answer:
            print(f'Your answer: {user_answer}')
            print('Correct!')
            count += 1
            if count == AMOUNT_OF_STEPS:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" "f"Correct answer was '{answer}'."
                  f" Let's try again, {name}!")
            break
