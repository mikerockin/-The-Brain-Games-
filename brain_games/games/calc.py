import random
import prompt


START_OF_RANGE_RAND_NUMBER_1 = 1
END_OF_RANGE_RAND_NUMBER_1 = 10
START_OF_RANGE_RAND_NUMBER_2 = 1
END_OF_RANGE_RAND_NUMBER_2 = 10


def performing_operations_on_numbers(count):
    if count == 0:
        print('What is the result of the expression?')
    rand_number_1 = random.randint(START_OF_RANGE_RAND_NUMBER_1,
                                   END_OF_RANGE_RAND_NUMBER_1)
    rand_number_2 = random.randint(START_OF_RANGE_RAND_NUMBER_2,
                                   END_OF_RANGE_RAND_NUMBER_2)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    user_answer = int(prompt.string(f'Question: {rand_number_1} '
                                    f''f'{operator} {rand_number_2} '))
    answer = eval(str(rand_number_1) + operator + str(rand_number_2))
    return answer, user_answer
