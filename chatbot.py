import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import datetime

# ==========================
# DATA
# ==========================

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did Python go to school? To improve its class!",
    "Why don't programmers like nature? Too many bugs!",
    "Why was the computer cold? It left its Windows open!"
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Consistency beats talent when talent is inconsistent.",
    "Learning never exhausts the mind.",
    "Dream big and dare to fail.",
    "Small progress is still progress."
]

# ==========================
# CHATBOT LOGIC
# ==========================

def get_response(user_input):

    text = user_input.lower().strip()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello! Welcome to Smart AI Assistant Pro."

    elif "how are you" in text:
        return "I am functioning perfectly and ready to help."

    elif "your name" in text:
        return "I am Smart AI Assistant Pro."

    elif "what is ai" in text or text == "ai":
        return """
Artificial Intelligence (AI) enables machines to mimic human intelligence.

Popular Areas:
• Machine Learning
• Deep Learning
• NLP
• Computer Vision
"""

    elif "machine learning" in text:
        return "Machine Learning is a branch of AI that learns from data."

    elif "deep learning" in text:
        return "Deep Learning uses neural networks with many layers."

    elif "python" in text:
        return """
Python Features:

• Easy to Learn
• AI & ML Support
• Automation
• Web Development
"""

    elif "career" in text:
        return """
Career Options:

• AI Engineer
• Data Scientist
• Software Developer
• Cloud Engineer
• Cyber Security Analyst
"""

    elif "resume" in text:
        return """
Resume Tips:

✔ Keep it one page
✔ Add Projects
✔ Add GitHub
✔ Add Skills
✔ Add Internships
"""

    elif "roadmap" in text:
        return """
AI Roadmap

1. Python
2. NumPy
3. Pandas
4. Machine Learning
5. Deep Learning
6. NLP
7. Build Projects
8. Deploy Models
"""

    elif "github" in text:
        return "GitHub helps developers manage and store code repositories."

    elif "project" in text:
        return """
Project Ideas

• AI Chatbot
• Face Detection
• Recommendation System
• Attendance System
• Tic Tac Toe AI
"""

    elif text.startswith("calculate"):
        try:
            expression = text.replace("calculate", "").strip()
            result = eval(expression)
            return f"Answer = {result}"
        except:
            return "Invalid Expression"

    elif "time" in text:
        return f"Current Time: {datetime.datetime.now().strftime('%H:%M:%S')}"

    elif "date" in text:
        return f"Today's Date: {datetime.date.today()}"

    elif "joke" in text:
        return random.choice(jokes)

    elif "motivate" in text or "quote" in text:
        return random.choice(quotes)

    elif "bye" in text:
        return "Goodbye! Have a wonderful day."

    return "Ask me about AI, Python, Career, Resume, Roadmap, Projects, Time, Date or Joke."

# ==========================
# MAIN WINDOW
# ==========================

root = tk.Tk()
root.title("Smart AI Assistant Pro")
root.geometry("1000x700")
root.configure(bg="#1E1E1E")

# --------------------------

def send_message():

    user_text = entry.get().strip()

    if user_text == "":
        return

    chat_area.insert(tk.END, f"You: {user_text}\n")

    response = get_response(user_text)

    chat_area.insert(tk.END, f"Bot: {response}\n\n")

    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

# --------------------------

def save_chat():

    content = chat_area.get("1.0", tk.END)

    with open("chat_history.txt", "w", encoding="utf-8") as file:
        file.write(content)

    messagebox.showinfo("Saved", "Chat Saved Successfully!")

# --------------------------

def view_history():

    try:

        with open("chat_history.txt", "r", encoding="utf-8") as file:
            data = file.read()

        history = tk.Toplevel(root)
        history.title("Chat History")
        history.geometry("700x500")

        txt = scrolledtext.ScrolledText(history)
        txt.pack(fill="both", expand=True)

        txt.insert(tk.END, data)

    except:
        messagebox.showinfo("Info", "No Chat History Found")

# --------------------------

title = tk.Label(
    root,
    text="🤖 SMART AI ASSISTANT PRO",
    font=("Segoe UI", 22, "bold"),
    bg="#1E1E1E",
    fg="cyan"
)

title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    width=100,
    height=28,
    font=("Consolas", 11),
    bg="#252526",
    fg="white"
)

chat_area.pack(padx=10, pady=10)

chat_area.insert(
    tk.END,
    """
WELCOME TO SMART AI ASSISTANT PRO

Try:

• What is AI?
• Python
• Career
• Resume
• Roadmap
• GitHub
• Project Ideas
• Tell me a joke
• Motivate me
• Calculate 500*10
• Current Time
• Current Date

--------------------------------------------

"""
)

entry = tk.Entry(
    root,
    width=70,
    font=("Segoe UI", 12)
)

entry.pack(pady=10)

entry.bind("<Return>", lambda event: send_message())

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Send", width=15, command=send_message).grid(row=0, column=0, padx=5)

tk.Button(frame, text="Save Chat", width=15, command=save_chat).grid(row=0, column=1, padx=5)

tk.Button(frame, text="History", width=15, command=view_history).grid(row=0, column=2, padx=5)

tk.Button(frame, text="Exit", width=15, command=root.destroy).grid(row=0, column=3, padx=5)

root.mainloop()