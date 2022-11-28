from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_check(number):
    return 'yes' if number % 2 == 0 else 'no'


def generate_round_qa():
    number = randint(0, 100)
    question = f'Question: {number}'
    answer = parity_check(number)
    return question, answer
