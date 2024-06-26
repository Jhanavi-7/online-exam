import tkinter as tk
from tkinter import messagebox

class RegisterPage:
    def _init_(self, root):
        self.root = root
        self.root.title("Register")
        
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=20)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=10)
        
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=20)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=10)
        
        self.button_register = tk.Button(root, text="Register", command=self.register)
        self.button_register.pack(pady=20)
    
    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        # Simulated storage of registered users (in-memory dictionary for simplicity)
        if username in registered_users:
            messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
        else:
            registered_users[username] = password
            messagebox.showinfo("Registration Successful", "You have successfully registered!")
            self.root.destroy()  # Close registration window
            open_login()  # Open the login page

class LoginPage:
    def _init_(self, root):
        self.root = root
        self.root.title("Login")
        
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=20)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=10)
        
        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=20)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=10)
        
        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=20)
        
        self.button_register = tk.Button(root, text="Register", command=open_register)
        self.button_register.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username in registered_users and registered_users[username] == password:
            self.root.withdraw()  # Hide login window
            open_exam()  # Open the exam window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class OnlineExam:
    def _init_(self, root):
        self.root = root
        self.questions = [
            "Question 1: What is Python?",
            "Question 2: Which of the following is not a Python data type?",
            "Question 3: What does the len() function do in Python?",
            "Question 4: In Python, which of these is used to create a function?",
            "Question 5: What is the output of print(2 + 3 * 4) in Python?",
            "Question 6: Which statement is used to exit from a loop in Python?",
            "Question 7: Which of the following is true about Python lists?",
            "Question 8: Which of the following data structures is mutable in Python?",
            "Question 9: What does the range() function in Python return?",
            "Question 10: How do you comment out a single line in Python?"
            # Add more questions as needed
        ]
        
        self.answers = [
            ["A high-level programming language", "A type of snake", "A software development tool", "A database management system"],
            ["Integer", "Float", "Double", " String"],
            ["Returns the length of a string or list", "Returns the logarithm of a number", "Returns the maximum value in a list", "Returns the smallest prime number greater than a given number"],
            ["def", "function", "define", "func"],
            ["20", "14", "24", "14.0"],
            ["break", "stop", "exit", "end"],
            ["Lists are mutable", "Lists can contain elements of different data types", "Lists automatically sort elements when appended", "Lists can only store integers"],
            ["Tuple", "List", "String", "Set"],
            ["A list of integers", "A range object", "A string of characters", "A floating-point number"],
            ["// This is a comment", "# This is a comment", "/* This is a comment */", "<!-- This is a comment -->"]
            # Add corresponding answers for each question
        ]
        
        self.correct_answers = ['A', 'C', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'B']  # Correct answers for each question (A for first option)
        self.current_question = 0
        self.user_answers = [None] * len(self.questions)  # Initialize with None for unattempted questions

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.radio_buttons = []
        self.answer_var = tk.StringVar()  # Variable to track selected answer

        for i in range(4):
            radio_button = tk.Radiobutton(root, variable=self.answer_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor=tk.W)  # Align radio buttons to the left
            radio_button.config(wraplength=400, justify=tk.LEFT)  # Wrap text and justify left

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack()

        self.submit_button = tk.Button(root, text="Submit Exam", command=self.submit_exam)
        self.submit_button.pack_forget()  # Initially hidden

        self.display_question(self.current_question)

    def next_question(self):
        if self.current_question < len(self.questions):
            self.user_answers[self.current_question] = self.get_selected_option()
        self.current_question += 1

        if self.current_question == len(self.questions):
            self.next_button.pack_forget()
            self.submit_button.pack(pady=10)  # Show submit button after last question
        else:
            self.display_question(self.current_question)

    def display_question(self, question_number):
        self.question_label.config(text=self.questions[question_number])
        options = self.answers[question_number]
        for i in range(4):
            self.radio_buttons[i].config(text=options[i])

    def get_selected_option(self):
        selected_value = self.answer_var.get()
        if selected_value:
            selected_index = int(selected_value)
            return chr(65 + selected_index) if selected_index >= 0 else None
        else:
            return None

    def calculate_score(self):
        score = 0
        for i in range(len(self.questions)):
            if self.user_answers[i] is not None:  # Check if question was attempted
                if self.user_answers[i] == self.correct_answers[i]:
                    score += 1  # Increase score for correct answer
        return score

    def submit_exam(self):
        self.root.withdraw()  # Hide exam window
        open_result(self.calculate_score(), len(self.questions))  # Show exam result


class ResultPage:
    def _init_(self, root, score, max_score):
        self.root = root
        self.root.title("Exam Result")

        self.score = score
        self.max_score = max_score
        
        completion_label = tk.Label(root, text="Congratulations! You have successfully completed the exam.")
        completion_label.pack(pady=20)
        
        score_label = tk.Label(root, text=f"Your Score: {self.score} out of {self.max_score}")
        score_label.pack(pady=10)

def open_result(score, max_score):
    root_result = tk.Tk()
    ResultPage(root_result, score, max_score)
    center_window(root_result, 400, 300)  # Increase result window size

def open_register():
    root_register = tk.Tk()
    RegisterPage(root_register)
    center_window(root_register, 400, 300)  # Increase register window size

def open_login():
    root_login = tk.Tk()
    LoginPage(root_login)
    center_window(root_login, 400, 300)  # Increase login window size

def open_exam():
    root_exam = tk.Tk()
    OnlineExam(root_exam)
    center_window(root_exam, 800, 600)  # Increase exam window size

def center_window(root, width, height):
    # Center the window on the screen
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry(f"{width}x{height}+{position_right}+{position_down}")

# Simulated storage of registered users (in-memory dictionary for simplicity)
registered_users = {
    "admin": "password"  # Default admin user for testing
}

if _name_ == "_main_":
    open_register()
    tk.mainloop()