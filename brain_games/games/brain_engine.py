from brain_games.cli import welcome_user
import prompt


def start_game(game):
    correct_answers = 0
    ROUNDS = 3
    name = welcome_user()
    game.get_rules()
    while correct_answers < ROUNDS:
        question, answer = game.generate()
        print(question)
        user_answer = prompt.string('Your answer: ', question)
        if user_answer == answer:
            correct_answers += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer}'.")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")
