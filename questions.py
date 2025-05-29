class Question:
    def __init__(self, text, choice_a, choice_b, choice_c, choice_d, correct_answer):
        self.text = text
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d
        self.correct_answer = correct_answer.lower()
    
    def __str__(self):
        return (
            f"Question: {self.text}\n"
            f"a: {self.choice_a}\n"
            f"b: {self.choice_b}\n"
            f"c: {self.choice_c}\n"
            f"d: {self.choice_d}\n"
            f"Correct Answer: {self.correct_answer}\n"
        )