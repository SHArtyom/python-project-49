from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(number):
    answer = 'yes'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            answer = 'no'
        i += 1
    return answer


def generate_round_qa():
    number = randint(3, 100)
    answer = prime_check(number)
    question = f'Question: {number}'
    return question, answer
