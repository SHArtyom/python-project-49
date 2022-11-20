from brain_games.cli import welcome_user
from random import randint


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0
    while correct_answers < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        gcd = 2
        answer = 1
        while gcd <= min(number1, number2):
            if number1 % gcd == 0 and number2 % gcd == 0:
                answer = gcd
            gcd += 1
        print('Question:', number1, number2)
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
