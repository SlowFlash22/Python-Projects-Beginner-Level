class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True"
                            f"/False)?: ")
        self.check_answer(user_answer)

    def check_answer(self, usr_answer):
        if self.question_list[self.question_number].answer.lower() == usr_answer.lower():
            self.score += 1
            print("Yes! You got it right!")
        else:
            print("That's incorrect :(")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}")
        self.question_number += 1
        print(f"Your current score: {self.score}/{self.question_number}\n")