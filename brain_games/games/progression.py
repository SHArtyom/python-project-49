from random import randint


def get_rules():
    return print('What number is missing in the progression?')


def generate():
    start_number = randint(0, 20)
    inc_number = randint(0, 20)
    progression = [(start_number + i * inc_number) for i in range(1, 10)]
    hidden_number = randint(0, 9)
    answer = str(progression[hidden_number])
    progression[hidden_number] = '..'
    question = 'Question: ' + ' '.join(str(i) for i in progression)
    return question, answer
