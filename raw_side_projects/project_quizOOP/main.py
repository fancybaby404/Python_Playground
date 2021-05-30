from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # List of question objects
quiz_brain = QuizBrain(question_bank)  # Initializes the QuizBrain class

for question in range(0, len(question_data)):
    question_text = question_data[question]["question"]
    question_answer = question_data[question]["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

while quiz_brain.still_has_questions():
    user_answer = quiz_brain.next_question()  # Initialize the question_list to an input
    quiz_brain.question_number += 1

print(f"You've completed the quiz\nYour final score was: {quiz_brain.score}/{len(question_bank)}")
