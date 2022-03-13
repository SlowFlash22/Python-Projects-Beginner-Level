from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo,bye


def quiz_start():
    print(logo)
    category_choice = input(
        "Which category quiz do you want to play? \nYou can choose from: Either Computers or Anime or "
        "Video Game: ").lower()
    if category_choice == "computers":
        print("Got it! Computers Quiz coming up....\n")
        question_bank = [Question(question["question"], question["correct_answer"]) for question in
                         question_data["computers"]]
    elif category_choice == "anime":
        print("Got it! Anime Quiz coming up....\n")
        question_bank = [Question(question["question"], question["correct_answer"]) for question in
                         question_data["anime"]]
    else:
        print("Got it! Video Games Quiz coming up....\n")
        question_bank = [Question(question["question"], question["correct_answer"]) for question in
                         question_data["videogame"]]
    quiz = QuizBrain(question_bank)

    quiz.next_question()

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz!")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


quiz_start()
while input("\nDo you want to play Quiz again? type \"yes\" / \"no\": ") == "yes":
    quiz_start()

print("")
print("Thanks for playing this game...Come Back Soon ")
print(bye)