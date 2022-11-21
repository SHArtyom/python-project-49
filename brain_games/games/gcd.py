from random import randint


def rules():
    return print('Find the greatest common divisor of given numbers.')


def generate():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    gcd = 2
    answer = '1'
    question = f'Question: {number1} {number2}'
    while gcd <= min(number1, number2):
        if number1 % gcd == 0 and number2 % gcd == 0:
            answer = str(gcd)
        gcd += 1
    return question, answer
