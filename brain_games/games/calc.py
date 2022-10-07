import random


START_OF_RANGE_RAND_NUMBER_1 = 1
END_OF_RANGE_RAND_NUMBER_1 = 10
START_OF_RANGE_RAND_NUMBER_2 = 1
END_OF_RANGE_RAND_NUMBER_2 = 10
RULES_OF_GAME = 'What is the result of the expression?'


def performing_operations_on_numbers():
    rand_number_1 = random.randint(START_OF_RANGE_RAND_NUMBER_1,
                                   END_OF_RANGE_RAND_NUMBER_1)
    rand_number_2 = random.randint(START_OF_RANGE_RAND_NUMBER_2,
                                   END_OF_RANGE_RAND_NUMBER_2)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    if operator == '+':
        answer = rand_number_1 + rand_number_2
    elif operator == '-':
        answer = rand_number_1 - rand_number_2
    else:
        answer = rand_number_1 * rand_number_2
    question = f'{rand_number_1} {operator} {rand_number_2}'
    return question, str(answer)
