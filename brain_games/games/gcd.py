import random
import prompt


GCD_START_OF_RANGE_RAND_NUMBER_1 = 1
GCD_END_OF_RANGE_RAND_NUMBER_1 = 20
GCD_START_OF_RANGE_RAND_NUMBER_2 = 20
GCD_END_OF_RANGE_RAND_NUMBER_2 = 50


def calculates_gcd(count):
    if count == 0:
        print('Find the greatest common divisor of given numbers.')
    rand_number_1 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_1,
                                   GCD_END_OF_RANGE_RAND_NUMBER_1)
    rand_number_2 = random.randint(GCD_START_OF_RANGE_RAND_NUMBER_2,
                                   GCD_END_OF_RANGE_RAND_NUMBER_2)
    user_answer = int(prompt.string(f'Question: {rand_number_1}'
                                    f' 'f'{rand_number_2} '))
    while rand_number_1 != 0 and rand_number_2 != 0:
        if rand_number_1 > rand_number_2:
            rand_number_1 = rand_number_1 % rand_number_2
        else:
            rand_number_2 = rand_number_2 % rand_number_1
    return rand_number_1 + rand_number_2, user_answer
