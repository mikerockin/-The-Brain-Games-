import random


PRIME_START_OF_RANGE_RAND_NUMBER = 1
PRIME_END_OF_RANGE_RAND_NUMBER = 200
DEVIDER = 2
RULES_OF_GAME = 'Answer "yes" if given number'' is prime.' \
                ' Otherwise answer "no".'


def is_prime(rand_number):
    DEVIDER = 2
    while DEVIDER * DEVIDER <= rand_number and rand_number % DEVIDER != 0:
        DEVIDER += 1
    return DEVIDER * DEVIDER > rand_number


def prime():
    rand_number = random.randint(PRIME_START_OF_RANGE_RAND_NUMBER,
                                 PRIME_END_OF_RANGE_RAND_NUMBER)
    if is_prime(rand_number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return rand_number, answer
