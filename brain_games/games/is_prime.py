PRIME_START_OF_RANGE_RAND_NUMBER = 1
PRIME_END_OF_RANGE_RAND_NUMBER = 200
DEVIDER = 2


def is_prime(rand_number):
    DEVIDER = 2
    while DEVIDER * DEVIDER <= rand_number and rand_number % DEVIDER != 0:
        DEVIDER += 1
    return DEVIDER * DEVIDER > rand_number
