import random
from questions import Question

class QuizTaker:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []
        self.score = 0

    def load_questions_from_file(self):
        with open(self.filename, "r") as file:
            content = file.read().strip()

        blocks = content.split("Question")[1:]

        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                continue  

            question_text = lines[0].split(": ", 1)[1].strip()
            choice_a = lines[1][3:].strip()
            choice_b = lines[2][3:].strip()
            choice_c = lines[3][3:].strip()
            choice_d = lines[4][3:].strip()
            correct = lines[5].split(":")[1].strip().lower()

            question = Question(
                question_text, choice_a, choice_b, choice_c, choice_d, correct
            )
            self.questions.append(question)

        random.shuffle(self.questions)

    def ask_questions(self):
        for index, q in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {q.text}")
            print("a:", q.choice_a)
            print("b:", q.choice_b)
            print("c:", q.choice_c)
            print("d:", q.choice_d)

            user_answer = input("Your answer (a/b/c/d): ").lower()
            while user_answer not in ["a", "b", "c", "d"]:
                user_answer = input("Invalid. Please enter a/b/c/d: ").lower()

            if user_answer == q.correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. Correct answer is {q.correct_answer}")

    def show_results(self):
        total = len(self.questions)
        print(f"\nYour final score: {self.score}/{total}")
        percent = (self.score / total) * 100
        print(f"That's {percent:.2f}% correct!")
