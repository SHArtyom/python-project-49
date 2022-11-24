from random import randint


def get_rules():
    print('Answer "yes" if given number is prime.', end=' ')
    print('Otherwise answer "no".')
    return


def generate():
    number = randint(3, 100)
    answer = 'yes'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            answer = 'no'
        i += 1
    question = f'Question: {number}'
    return question, answer
