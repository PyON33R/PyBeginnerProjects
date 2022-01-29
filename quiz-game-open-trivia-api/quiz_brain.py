

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1 
        else:
            print("Sorry, Wrong Answer!")
        print(f"The Correct Answer is: {correct_answer}")
        

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)
        print(f"Your Current Score is: {self.score}/{self.question_number}")

