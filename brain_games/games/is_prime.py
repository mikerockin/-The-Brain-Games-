import random
import prompt


PRIME_START_OF_RANGE_RAND_NUMBER = 1
PRIME_END_OF_RANGE_RAND_NUMBER = 200
DEVIDER = 2


def is_prime(count):
    if count == 0:
        print('Answer "yes" if given number is prime.'
              ' Otherwise answer "no"')
    rand_number = random.randint(PRIME_START_OF_RANGE_RAND_NUMBER,
                                 PRIME_END_OF_RANGE_RAND_NUMBER)
    DEVIDER = 2
    while DEVIDER * DEVIDER <= rand_number and rand_number % DEVIDER != 0:
        DEVIDER += 1
    if DEVIDER * DEVIDER > rand_number:
        answer = 'yes'
    else:
        answer = 'no'
    print(answer)
    user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
    return answer, user_answer
