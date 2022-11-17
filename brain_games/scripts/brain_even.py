from brain_games.cli import welcome_user
from random import randint


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        flag = 'yes'
        number = randint(0, 100)
        if number % 2:
            flag = 'no'
        print('Question:', number)
        answr = input('Your answer: ')
        if answr == flag:
            correct_answers += 1
            print('Correct!')
        else:
            print(f"'{answr}' is wrong answer ;(. Correct answer was '{flag}'.")
            print(f"Let's try again, {name}!")
            correct_answers = 0
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
