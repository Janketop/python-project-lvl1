#!/usr/bin/env python3
import prompt
import random


ROUND = 3


def even_or_odd(number):
    return number % 2 == 0


def opposite_answer(answer):
    if answer == "yes":
        return "no"
    else:
        return "yes"


def wrong_answer(answer):
    is_wrong = ", is wrong answer ;(. Correct answer was "
    return "\"{}\"{}\"{}\"".format(answer, is_wrong, opposite_answer(answer))


def try_again(name):
    return "Let's try again, {}!".format(name)


def play_game():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    a = 0
    while a < ROUND:
        number = random.randint(0, 99)
        print("Question: {}".format(number))
        answer = input("Your answer: ")
        if answer == "yes" and even_or_odd(number):
            print("Correct!")
            a += 1
        elif answer == "no" and not even_or_odd(number):
            print("Correct!")
            a += 1
        else:
            return wrong_answer(answer) + '\n' + try_again(name)
            break
    if a == 3:
        return 'Congratulation, {}!'.format(name)


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(play_game())


if __name__ == '__main__':
    main()
