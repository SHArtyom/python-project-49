from brain_games.cli import welcome_user
from random import randint
from random import choice
import operator


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers < 3:
        number1 = randint(0, 20)
        number2 = randint(0, 20)
        char, action = choice([('+', operator.add),
                               ('*', operator.mul), ('-', operator.sub)])
        answer = action(number1, number2)
        print('Question:', number1, char, number2)
        your_answer = int(input('Your answer: '))
        if your_answer == answer:
            correct_answers += 1
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
