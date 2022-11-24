from random import randint


def get_rules():
    return print('Answer "yes" if the number is even, otherwise answer "no".')


def generate():
    number = randint(0, 100)
    question = f'Question: {number}'
    answer = 'yes'
    if number % 2:
        answer = 'no'
    return question, answer
