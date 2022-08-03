#!/usr/bin/env python3
import random
import prompt


def main():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 3:
        rand_number = random.randint(1, 841)
        answer = ''
        user_answer = ''
        if rand_number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        user_answer = (prompt.string(f'Question: {rand_number} ')).lower()
        while user_answer != 'yes' or user_answer != 'no':
            break
        if answer == user_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
