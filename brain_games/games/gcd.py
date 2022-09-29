GCD_START_OF_RANGE_RAND_NUMBER_1 = 1
GCD_END_OF_RANGE_RAND_NUMBER_1 = 20
GCD_START_OF_RANGE_RAND_NUMBER_2 = 20
GCD_END_OF_RANGE_RAND_NUMBER_2 = 50


def calculates_gcd(rand_number_1, rand_number_2, count):
    if count == 0:
        print('Find the greatest common divisor of given numbers.')
    while rand_number_1 != 0 and rand_number_2 != 0:
        if rand_number_1 > rand_number_2:
            rand_number_1 = rand_number_1 % rand_number_2
        else:
            rand_number_2 = rand_number_2 % rand_number_1
    return rand_number_1 + rand_number_2
