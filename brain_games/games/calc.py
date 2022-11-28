from random import randint
from random import choice
import operator


RULES = 'What is the result of the expression?'


def generate_round_qa():
    number1 = randint(0, 20)
    number2 = randint(0, 20)
    char, action = choice([('+', operator.add),
                           ('*', operator.mul), ('-', operator.sub)])
    question = f'Question: {number1} {char} {number2}'
    answer = str(action(number1, number2))
    return question, answer
