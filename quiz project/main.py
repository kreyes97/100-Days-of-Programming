from data import question_data

# Made this my own way and got rid of quizbrain.py. Looks the same functionality-wise as the final product from the course.


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class Score:
    def __init__(self, count, total):
        self.count = count
        self.total = total

    def update_score(self):
        self.count += 1

    def total_score(self):
        self.total += 1


def question_generator(index):
    new_question = Question(
        question_data[index]["text"], question_data[index]["answer"]
    )
    return new_question


def quiz_game(score):
    for i in range(0, len(question_data)):
        new_question = question_generator(i)
        print(f"Q.{i+1}: {new_question.text} (True/False)?\n")
        answer = input("True or False? \n").capitalize()

        if answer not in ("True", "False"):
            print("Invalid answer.")
        elif answer == new_question.answer:
            print("Correct!\n")
            score.update_score()
            score.total_score()
            print(f"Your current score is: {score.count}/{score.total}\n")
        else:
            print(f"Incorrect! The correct answer is {new_question.answer}\n")
            score.total_score()
            print(f"Your current score is: {score.count}/{score.total}\n")


def main():
    score = Score(0, 0)
    quiz_game(score)

    while True:
        user_input = input("Would you like to play again? Yes or No\n").capitalize()

        if user_input not in ("Yes", "No"):
            print("Invalid input.\n")
        elif user_input == "No":
            print(f"Your final score is: {score.count}/{score.total}")
            print("Goodbye!\n")
            break
        else:
            score = Score(score.count, score.total)
            quiz_game(score)


main()
