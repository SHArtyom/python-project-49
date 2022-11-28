from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def gcd_search(number1, number2):
    gcd = 2
    answer = '1'
    while gcd <= min(number1, number2):
        if number1 % gcd == 0 and number2 % gcd == 0:
            answer = str(gcd)
        gcd += 1
    return answer


def generate_round_qa():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer = gcd_search(number1, number2)
    question = f'Question: {number1} {number2}'
    return question, answer
