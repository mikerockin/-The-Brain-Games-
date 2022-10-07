import random

START_OF_RANGE_RAND_NUMBER = 1
END_OF_RANGE_RAND_NUMBER = 841
RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    rand_number = random.randint(START_OF_RANGE_RAND_NUMBER,
                                 END_OF_RANGE_RAND_NUMBER)
    if rand_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return rand_number, answer
