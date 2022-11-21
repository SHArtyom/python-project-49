from brain_games.cli import welcome_user
from random import randint


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = randint(3, 100)
        answer = 'yes'
        for i in range(2, number // 2):
            if number % i == 0:
                answer = 'no'
            i += 1
        print('Question:', number)
        your_answer = input('Your answer: ')
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
