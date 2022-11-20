from brain_games.cli import welcome_user
from random import randint


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    correct_answers = 0
    while correct_answers < 3:
        start_number = randint(0, 20)
        inc_number = randint(0, 20)
        progression = []
        for i in range(10):
            progression.append(start_number + i * inc_number)
        hidden = randint(0, 9)
        answer = progression[hidden]
        progression[hidden] = '..'
        print('Question:', *progression)
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
