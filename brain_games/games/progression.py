from random import randint


def rules():
    return print('What number is missing in the progression?')


def generate():
    start_number = randint(0, 20)
    inc_number = randint(0, 20)
    progression = []
    for i in range(10):
        progression.append(start_number + i * inc_number)
    hidden = randint(0, 9)
    answer = str(progression[hidden])
    progression[hidden] = '..'
    question = 'Question: ' + ' '.join(str(i) for i in progression)
    return question, answer
