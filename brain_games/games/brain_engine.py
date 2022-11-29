from brain_games.cli import welcome_user
import prompt


def start_game(game):
    correct_answers = 0
    ROUNDS = 3
    name = welcome_user()
    print(game.RULES)
    while correct_answers < ROUNDS:
        question, answer = game.generate_round_qa()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            correct_answers += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    return
