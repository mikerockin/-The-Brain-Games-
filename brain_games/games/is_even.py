import random
import prompt
START_OF_RANGE_RAND_NUMBER = 1
END_OF_RANGE_RAND_NUMBER = 841


def is_even(count):
    if count == 0:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    rand_number = random.randint(START_OF_RANGE_RAND_NUMBER,
                                 END_OF_RANGE_RAND_NUMBER)
    if rand_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
    return answer, user_answer
