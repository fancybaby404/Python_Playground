from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        # Initilization
        self.window = Tk()
        self.window.config(bg=THEME_COLOR)
        self.window.title("QuizGUI")
        
        # QuizBrain
        self.quiz = quiz_brain
        
        # Score
        self.create_score()
        
        # Canvas
        self.create_canvas()
        self.get_next_question()
        
        # Buttons
        self.create_buttons()
        
        # Main Loop
        self.window.mainloop()

    def create_canvas(self):
        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        
        # Canvas Text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text='Question',
            font=FONT
            )

    def create_buttons(self):
        # Right Button
        self.right_button_image = PhotoImage(file='./images/true.png')
        self.right_button = Button(command=self.right_button_pressed, image=self.right_button_image)
        self.right_button.grid(column=0, row=2, padx=20, pady=20)
    
        # Wrong Button
        self.wrong_button_image = PhotoImage(file='./images/false.png')
        self.wrong_button= Button(command=self.wrong_button_pressed, image=self.wrong_button_image)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)
    
    def create_score(self):
        self.score_text = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Arial', 10, "bold"))
        self.score_text.grid(column=1, row=0, padx=20, pady=20)
        
    def update_score(self):
        self.score_text.config(text=f'Score: {self.quiz.score}')

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # Finished Quiz (show final score etc.)
            quit()
    
    def wrong_button_pressed(self):
        self.give_feedback('False')    
        self.update_score()
        self.window.after(1000, self.get_next_question)
    
    def right_button_pressed(self):
        self.give_feedback('True')
        self.update_score()
        self.window.after(1000, self.get_next_question)
        
    def give_feedback(self, user_input):
        if self.quiz.check_answer(user_answer=user_input):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
