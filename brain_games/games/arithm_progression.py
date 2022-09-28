import random

START_OF_RANGE_AMOUNT_OF_ELEMENTS = 5
END_OF_RANGE_AMOUNT_OF_ELEMENTS = 10
START_OF_RANGE_ELEMENTS = 1
END_OF_RANGE_ELEMENTS = 34
START_OF_RANGE_STEP_PROGRESSION = 2
END_OF_RANGE_STEP_PROGRESSION = 9


def calculates_arithm_progression(amount_of_elements, element,
                                  step_of_progression, progression):
    for i in range(amount_of_elements):
        element += step_of_progression
        progression.append(element)
    random_number = random.choice(progression)
    index_of_random_number = progression.index(random_number)
    progression[index_of_random_number] = '..'
    my_string = " ".join(map(str, progression))
    return random_number, my_string
