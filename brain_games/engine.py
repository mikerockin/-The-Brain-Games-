import prompt

AMOUNT_OF_STEPS = 3


def engine(generate_round, rules_of_game):
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules_of_game)
    while count != AMOUNT_OF_STEPS:
        question, answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" "f"Correct answer was '{answer}'."
                  f" Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
