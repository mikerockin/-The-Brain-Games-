#!/usr/bin/env python3
START_OF_RANGE_RAND_NUMBER = 1
END_OF_RANGE_RAND_NUMBER = 841


def is_even(param_1):
    rand_number = param_1
    if rand_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer
