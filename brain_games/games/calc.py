#!/usr/bin/env python3
START_OF_RANGE_RAND_NUMBER_1 = 1
END_OF_RANGE_RAND_NUMBER_1 = 10
START_OF_RANGE_RAND_NUMBER_2 = 1
END_OF_RANGE_RAND_NUMBER_2 = 10


def performing_operations_on_numbers(rand_number_1, rand_number_2, operator):
    answer = eval(str(rand_number_1) + operator + str(rand_number_2))
    return answer
