# 🧠 Quiz App with GUI, Scoreboard, and Admin Panel (Python + Tkinter)

A fully functional multiple-choice Quiz Application built using **Python and Tkinter**, with a password-protected **Admin Panel** for managing questions, a scoreboard to track top players, and support for dynamic quiz content using JSON.

---

## 📌 Features

### 🎮 User Side (Player Mode)
- 🧑‍💻 **Name Entry** before quiz begins
- ❓ **Multiple Choice Questions (MCQ)**
- 🔀 **Shuffled Questions** every time
- ✅ **Answer Checking** with score tracking
- 🎯 **Final Score Display**
- 🏆 **Top 5 Scoreboard** after quiz ends
- 📂 Data saved in `scoreboard.json`

---

### 🔐 Admin Panel (Password Protected)
- Requires password (default: `admin123`)
- 🧾 **View All Questions**
- ➕ **Add New Questions** via GUI
- ✏️ **Edit Existing Questions** by question number
- ❌ **Delete Questions** by number
- All updates reflected in real-time in `quiz.json`

---

## 📁 File Structure
📦 Quiz App
├── quiz_gui.py # Main app file with GUI code
├── quiz.json # JSON file with all quiz questions
├── scoreboard.json # JSON file with user scores
└── README.md # This file


---

## 💻 Tech Stack

| Component       | Tool                  |
|----------------|-----------------------|
| GUI Framework   | Python Tkinter        |
| Data Storage    | JSON                  |
| Language        | Python 3.x            |
| Randomization   | random.shuffle        |
| File Handling   | open, json.load/dump  |

---

## 🛡️ Admin Access

- **To access Admin Panel:**
  - Click "Admin Panel" on main menu
  - Enter password → `admin123` *(default, can be changed in code)*

---

## 📝 How to Add/Manage Questions

You can add/edit/delete questions from the Admin Panel. Each question has:
- A **question**
- Four **options**
- One **correct answer**

All questions are stored and updated in `quiz.json`.

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.x

### ▶️ Run the App
```bash
python quiz_gui.py

💡 Future Ideas
⏱️ Add a timer per question

🌐 Build a web version using Flask

📊 Show detailed quiz analytics

🔐 Secure admin passwords using hashing

👤 Add login system with user history

📥 Import/export questions (CSV)

🙌 Credits
Developed by Rashmi kumari
Feel free to fork, improve, or contribute ⭐

📬 Contact
For suggestions or collaborations: [your-email@example.com]


✅ **What to do next:**
1. Create `README.md` file in your project directory
2. Paste the content above
3. Replace `"Your Name"` and `"your-email@example.com"` with your actual name/email
4. You’re ready to push to GitHub!
