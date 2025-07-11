import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random
import os

ADMIN_PASSWORD = "admin123"

# Load questions from JSON
def load_questions(filename='quiz.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return []

# Save score to scoreboard.json
def save_score(name, score, filename='scoreboard.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                scores = json.load(f)
            except:
                scores = []
    else:
        scores = []

    scores.append({"name": name, "score": score})
    with open(filename, 'w') as f:
        json.dump(scores, f, indent=2)

# View scoreboard (Top 5)
def view_scoreboard(filename='scoreboard.json'):
    try:
        with open(filename, 'r') as f:
            scores = json.load(f)
            sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
            top_scores = sorted_scores[:5]
            result = "\n".join([f"{entry['name']} - {entry['score']}" for entry in top_scores])
            return result
    except:
        return "No scores yet."

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App - GUI Version")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.name = ""
        self.questions = []
        self.current_q = 0
        self.score = 0

        self.main_menu_screen()

    def main_menu_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🎓 Welcome to the Quiz App", font=("Arial", 16), bg="#f0f0f0").pack(pady=30)
        tk.Button(self.root, text="Take Quiz", font=("Arial", 12), command=self.name_screen).pack(pady=10)
        tk.Button(self.root, text="Admin Panel", font=("Arial", 12), command=self.open_admin_panel).pack(pady=10)
        tk.Button(self.root, text="Exit", font=("Arial", 12), command=self.root.quit).pack(pady=10)

    def open_admin_panel(self):
      password = tk.simpledialog.askstring("Admin Login", "Enter Admin Password:", show="*")
      if password == ADMIN_PASSWORD:
        AdminPanel(tk.Toplevel(self.root))
      else:
        messagebox.showerror("Access Denied", "Incorrect password!")


    def name_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Enter Your Name", font=("Arial", 16), bg="#f0f0f0").pack(pady=30)
        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=10)
        tk.Button(self.root, text="Start Quiz", font=("Arial", 12), command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        name = self.name_entry.get().strip()
        if name == "":
            messagebox.showwarning("Input Required", "Please enter your name.")
            return

        self.name = name
        self.questions = load_questions()
        random.shuffle(self.questions)
        self.current_q = 0
        self.score = 0
        self.quiz_screen()

    def quiz_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_q < len(self.questions):
            q = self.questions[self.current_q]
            self.var = tk.IntVar()
            self.var.set(-1)

            tk.Label(self.root, text=f"Q{self.current_q + 1}: {q['question']}", font=("Arial", 14), wraplength=550, bg="#f0f0f0").pack(pady=20)

            for i, opt in enumerate(q['options']):
                tk.Radiobutton(self.root, text=opt, variable=self.var, value=i, font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", padx=50, pady=5)

            tk.Button(self.root, text="Submit", command=self.check_answer, font=("Arial", 12, "bold")).pack(pady=20)
        else:
            self.show_result()

    def check_answer(self):
        selected = self.var.get()
        if selected == -1:
            messagebox.showwarning("No Selection", "Please select an answer.")
            return

        correct = self.questions[self.current_q]['answer']
        if self.questions[self.current_q]['options'][selected] == correct:
            self.score += 1

        self.current_q += 1
        self.quiz_screen()

    def show_result(self):
        save_score(self.name, self.score)
        scoreboard = view_scoreboard()

        messagebox.showinfo("Quiz Completed", f"{self.name}, your score is: {self.score}/{len(self.questions)}")

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🏆 Top Scores", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Label(self.root, text=scoreboard, font=("Arial", 14), bg="#f0f0f0", justify="left").pack()

        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12)).pack(pady=30)

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.geometry("600x450")
        self.root.configure(bg="#ffffff")

        self.load_questions()

    def load_questions(self):
        try:
            with open('quiz.json', 'r') as f:
                self.questions = json.load(f)
        except:
            self.questions = []

        self.render_question_list()

    def render_question_list(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🛠️ Admin Panel", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)
        for i, q in enumerate(self.questions):
            tk.Label(self.root, text=f"{i+1}. {q['question']}", font=("Arial", 12), wraplength=500, bg="#ffffff").pack(anchor="w", padx=20)

        tk.Button(self.root, text="Add Question", command=self.add_question_gui, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Edit Question", command=self.edit_question_gui, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Delete Question", command=self.delete_question_gui, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Close", command=self.root.destroy, font=("Arial", 12)).pack(pady=10)

    def add_question_gui(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Question")

        tk.Label(popup, text="Question:").pack()
        entry_q = tk.Entry(popup, width=50); entry_q.pack()

        options = []
        for i in range(4):
            entry = tk.Entry(popup, width=50)
            entry.insert(0, f"Option {i+1}")
            entry.pack()
            options.append(entry)

        tk.Label(popup, text="Correct Answer:").pack()
        entry_ans = tk.Entry(popup, width=50); entry_ans.pack()

        def save_new():
            q_text = entry_q.get()
            opts = [e.get() for e in options]
            ans = entry_ans.get()
            if q_text and all(opts) and ans:
                self.questions.append({"question": q_text, "options": opts, "answer": ans})
                with open('quiz.json', 'w') as f:
                    json.dump(self.questions, f, indent=2)
                popup.destroy()
                self.render_question_list()
            else:
                messagebox.showerror("Error", "Please fill all fields.")

        tk.Button(popup, text="Save", command=save_new).pack(pady=10)

    def edit_question_gui(self):
        idx = simpledialog.askinteger("Edit", "Enter question number to edit:")
        if idx is None or idx < 1 or idx > len(self.questions):
            return

        q = self.questions[idx-1]
        popup = tk.Toplevel(self.root)
        popup.title("Edit Question")

        tk.Label(popup, text="Question:").pack()
        entry_q = tk.Entry(popup, width=50); entry_q.insert(0, q['question']); entry_q.pack()

        entries = []
        for opt in q['options']:
            e = tk.Entry(popup, width=50)
            e.insert(0, opt)
            e.pack()
            entries.append(e)

        tk.Label(popup, text="Correct Answer:").pack()
        entry_ans = tk.Entry(popup, width=50); entry_ans.insert(0, q['answer']); entry_ans.pack()

        def save_edit():
            new_q = entry_q.get()
            new_opts = [e.get() for e in entries]
            new_ans = entry_ans.get()
            if new_q and all(new_opts) and new_ans:
                self.questions[idx-1] = {"question": new_q, "options": new_opts, "answer": new_ans}
                with open('quiz.json', 'w') as f:
                    json.dump(self.questions, f, indent=2)
                popup.destroy()
                self.render_question_list()
            else:
                messagebox.showerror("Error", "Please fill all fields.")

        tk.Button(popup, text="Save Changes", command=save_edit).pack(pady=10)

    def delete_question_gui(self):
        idx = simpledialog.askinteger("Delete", "Enter question number to delete:")
        if idx is None or idx < 1 or idx > len(self.questions):
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this question?")
        if confirm:
            self.questions.pop(idx-1)
            with open('quiz.json', 'w') as f:
                json.dump(self.questions, f, indent=2)
            self.render_question_list()

# Start GUI App
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


