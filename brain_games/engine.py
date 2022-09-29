import prompt


AMOUNT_OF_STEPS = 3


def engine(returns_answer):
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    while count != AMOUNT_OF_STEPS:
        answer, user_answer = returns_answer(count)
        if user_answer == answer:
            print(f'Your answer: {user_answer}')
            print('Correct!')
            count += 1
            if count == AMOUNT_OF_STEPS:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" "f"Correct answer was '{answer}'."
                  f" Let's try again, {name}!")
            break
