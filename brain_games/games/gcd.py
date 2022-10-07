import random

GCD_START_OF_RANGE_RAND_NUMBER_1 = 1
GCD_END_OF_RANGE_RAND_NUMBER_1 = 20
GCD_START_OF_RANGE_RAND_NUMBER_2 = 20
GCD_END_OF_RANGE_RAND_NUMBER_2 = 50
RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def calculates_gcd():
    rand_number_1 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_1,
                                   GCD_END_OF_RANGE_RAND_NUMBER_1)
    rand_number_2 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_2,
                                   GCD_END_OF_RANGE_RAND_NUMBER_2)
    question = f' {rand_number_1} {rand_number_2} '
    while rand_number_1 != 0 and rand_number_2 != 0:
        if rand_number_1 > rand_number_2:
            rand_number_1 = rand_number_1 % rand_number_2
        else:
            rand_number_2 = rand_number_2 % rand_number_1
    answer = rand_number_1 + rand_number_2
    return question, str(answer)
