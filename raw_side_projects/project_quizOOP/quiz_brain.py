class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question_number = self.question_number
        current_question = self.questions_list[self.question_number]
        # needed to put this into a variable so we can call the .text attribute

        user_answer = input(f"Q.{question_number + 1}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is: {self.score}/{question_number + 1}\n")

    def still_has_questions(self):
        # need length of question list
        question_length = len(self.questions_list)
        return self.question_number < question_length

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was {correct_answer}")
