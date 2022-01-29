

from statistics import quantiles


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


if __name__ == "__main__":
    q1 = Question("What is your name?", "True")
    print(q1.text, q1.answer)