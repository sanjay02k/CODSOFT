import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# =====================================
# CAREER DATABASE
# =====================================

career_data = {
    "AI Engineer": {
        "salary": "₹8 - ₹20 LPA",
        "skills": "Python, ML, Deep Learning",
        "roadmap": "Python → ML → DL → NLP → Projects"
    },

    "Data Scientist": {
        "salary": "₹6 - ₹18 LPA",
        "skills": "Python, Pandas, Statistics",
        "roadmap": "Python → Pandas → SQL → ML"
    },

    "Machine Learning Engineer": {
        "salary": "₹8 - ₹22 LPA",
        "skills": "Python, TensorFlow, ML",
        "roadmap": "Python → ML → Deployment"
    },

    "Web Developer": {
        "salary": "₹4 - ₹12 LPA",
        "skills": "HTML, CSS, JavaScript",
        "roadmap": "HTML → CSS → JS → React"
    },

    "Cybersecurity Analyst": {
        "salary": "₹6 - ₹15 LPA",
        "skills": "Networking, Linux, Security",
        "roadmap": "Networking → Linux → Ethical Hacking"
    },

    "Cloud Engineer": {
        "salary": "₹7 - ₹18 LPA",
        "skills": "AWS, Azure, Docker",
        "roadmap": "Linux → Cloud → DevOps"
    },

    "Software Developer": {
        "salary": "₹4 - ₹15 LPA",
        "skills": "Programming, DSA",
        "roadmap": "Programming → DSA → Projects"
    }
}

# =====================================
# SCORING ENGINE
# =====================================

def calculate_scores(skill, interest):

    scores = {
        "AI Engineer": 0,
        "Data Scientist": 0,
        "Machine Learning Engineer": 0,
        "Web Developer": 0,
        "Cybersecurity Analyst": 0,
        "Cloud Engineer": 0,
        "Software Developer": 0
    }

    if skill == "Python":
        scores["AI Engineer"] += 40
        scores["Data Scientist"] += 35
        scores["Machine Learning Engineer"] += 35
        scores["Software Developer"] += 20

    elif skill == "Machine Learning":
        scores["Machine Learning Engineer"] += 50
        scores["AI Engineer"] += 45

    elif skill == "HTML/CSS":
        scores["Web Developer"] += 50

    elif skill == "Networking":
        scores["Cybersecurity Analyst"] += 40
        scores["Cloud Engineer"] += 35

    elif skill == "Cloud":
        scores["Cloud Engineer"] += 50

    if interest == "Artificial Intelligence":
        scores["AI Engineer"] += 50

    elif interest == "Data":
        scores["Data Scientist"] += 50

    elif interest == "Web Development":
        scores["Web Developer"] += 50

    elif interest == "Cyber Security":
        scores["Cybersecurity Analyst"] += 50

    elif interest == "Cloud":
        scores["Cloud Engineer"] += 50

    return scores


# =====================================
# MAIN RECOMMENDATION
# =====================================

def recommend_career():

    name = name_entry.get()

    if name == "":
        messagebox.showwarning(
            "Input Error",
            "Please enter your name."
        )
        return

    skill = skill_var.get()
    interest = interest_var.get()

    scores = calculate_scores(skill, interest)

    sorted_careers = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top1 = sorted_careers[0][0]
    top2 = sorted_careers[1][0]
    top3 = sorted_careers[2][0]

    match_score = min(sorted_careers[0][1], 100)

    progress["value"] = match_score

    result_label.config(
        text=f"🎯 {name}, Recommended Career:\n{top1}"
    )

    salary_label.config(
        text=f"💰 Salary: {career_data[top1]['salary']}"
    )

    skills_label.config(
        text=f"🛠 Skills:\n{career_data[top1]['skills']}"
    )

    roadmap_label.config(
        text=f"📚 Roadmap:\n{career_data[top1]['roadmap']}"
    )

    top3_label.config(
        text=f"""
🥇 {top1}
🥈 {top2}
🥉 {top3}
"""
    )

    save_history(name, top1)


# =====================================
# SAVE HISTORY
# =====================================

def save_history(name, career):

    current_time = datetime.datetime.now()

    with open(
        "career_history.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{current_time} | {name} | {career}\n"
        )
# =====================================
# VIEW HISTORY
# =====================================

def view_history():

    try:

        with open(
            "career_history.txt",
            "r",
            encoding="utf-8"
        ) as file:

            data = file.read()

        history_window = tk.Toplevel(root)
        history_window.title("Career Recommendation History")
        history_window.geometry("700x500")

        history_text = tk.Text(
            history_window,
            font=("Consolas", 11)
        )

        history_text.pack(
            fill="both",
            expand=True
        )

        history_text.insert(
            tk.END,
            data
        )

    except:

        messagebox.showinfo(
            "Info",
            "No history found."
        )


# =====================================
# SAVE REPORT
# =====================================

def save_report():

    try:

        report = f"""
==================================
CAREER RECOMMENDATION REPORT
==================================

Name: {name_entry.get()}
Age: {age_entry.get()}
Qualification: {qualification_var.get()}
Experience: {experience_var.get()}

{result_label.cget("text")}

{salary_label.cget("text")}

{skills_label.cget("text")}

{roadmap_label.cget("text")}

Generated On:
{datetime.datetime.now()}
"""

        with open(
            "career_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        messagebox.showinfo(
            "Success",
            "Report Saved Successfully!"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# =====================================
# THEME FUNCTIONS
# =====================================

def dark_theme():

    root.configure(bg="#1E1E1E")

    title.config(
        bg="#1E1E1E",
        fg="cyan"
    )

    profile_frame.config(
        bg="#1E1E1E",
        fg="cyan"
    )

    result_label.config(
        bg="#1E1E1E",
        fg="lime"
    )

    salary_label.config(
        bg="#1E1E1E",
        fg="white"
    )

    skills_label.config(
        bg="#1E1E1E",
        fg="white"
    )

    roadmap_label.config(
        bg="#1E1E1E",
        fg="white"
    )

    top3_label.config(
        bg="#1E1E1E",
        fg="gold"
    )


def light_theme():

    root.configure(bg="white")

    title.config(
        bg="white",
        fg="blue"
    )

    profile_frame.config(
        bg="white",
        fg="blue"
    )

    result_label.config(
        bg="white",
        fg="green"
    )

    salary_label.config(
        bg="white",
        fg="black"
    )

    skills_label.config(
        bg="white",
        fg="black"
    )

    roadmap_label.config(
        bg="white",
        fg="black"
    )

    top3_label.config(
        bg="white",
        fg="darkgreen"
    )


# =====================================
# MAIN WINDOW
# =====================================

root = tk.Tk()

root.title(
    "AI Career Recommendation System Pro"
)

root.geometry(
    "1100x850"
)

root.configure(
    bg="#1E1E1E"
)

# =====================================
# TITLE
# =====================================

title = tk.Label(
    root,
    text="🚀 AI CAREER RECOMMENDATION SYSTEM PRO",
    font=("Segoe UI", 22, "bold"),
    bg="#1E1E1E",
    fg="cyan"
)

title.pack(
    pady=15
)

# =====================================
# USER PROFILE
# =====================================

profile_frame = tk.LabelFrame(
    root,
    text="👤 User Profile",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E1E",
    fg="cyan",
    padx=10,
    pady=10
)

profile_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

# Name

tk.Label(
    profile_frame,
    text="Name",
    bg="#1E1E1E",
    fg="white"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)

name_entry = tk.Entry(
    profile_frame,
    width=25
)

name_entry.grid(
    row=0,
    column=1
)

# Age

tk.Label(
    profile_frame,
    text="Age",
    bg="#1E1E1E",
    fg="white"
).grid(
    row=0,
    column=2
)

age_entry = tk.Entry(
    profile_frame,
    width=15
)

age_entry.grid(
    row=0,
    column=3
)

# Qualification

tk.Label(
    profile_frame,
    text="Qualification",
    bg="#1E1E1E",
    fg="white"
).grid(
    row=1,
    column=0,
    pady=5
)

qualification_var = tk.StringVar()

qualification_combo = ttk.Combobox(
    profile_frame,
    textvariable=qualification_var,
    width=22
)

qualification_combo["values"] = (
    "High School",
    "Diploma",
    "BCA",
    "B.Sc",
    "B.Tech",
    "MCA",
    "M.Tech"
)

qualification_combo.grid(
    row=1,
    column=1
)

# Experience

tk.Label(
    profile_frame,
    text="Experience",
    bg="#1E1E1E",
    fg="white"
).grid(
    row=1,
    column=2
)

experience_var = tk.StringVar()

experience_combo = ttk.Combobox(
    profile_frame,
    textvariable=experience_var,
    width=22
)

experience_combo["values"] = (
    "Fresher",
    "0-1 Years",
    "1-3 Years",
    "3-5 Years",
    "5+ Years"
)

experience_combo.grid(
    row=1,
    column=3
)

# Skill

tk.Label(
    profile_frame,
    text="Skill",
    bg="#1E1E1E",
    fg="white"
).grid(
    row=2,
    column=0,
    pady=10
)

skill_var = tk.StringVar()

skill_combo = ttk.Combobox(
    profile_frame,
    textvariable=skill_var,
    width=22
)

skill_combo["values"] = (
    "Python",
    "Machine Learning",
    "HTML/CSS",
    "Networking",
    "Cloud"
)

skill_combo.grid(
    row=2,
    column=1
)

# Interest

tk.Label(
    profile_frame,
    text="Interest",
    bg="#1E1E1E",
    fg="white"
).grid(
    row=2,
    column=2
)

interest_var = tk.StringVar()

interest_combo = ttk.Combobox(
    profile_frame,
    textvariable=interest_var,
    width=22
)

interest_combo["values"] = (
    "Artificial Intelligence",
    "Data",
    "Web Development",
    "Cyber Security",
    "Cloud"
)

interest_combo.grid(
    row=2,
    column=3
)
# =====================================
# RECOMMEND BUTTON
# =====================================

recommend_btn = tk.Button(
    root,
    text="🎯 GET CAREER RECOMMENDATION",
    font=("Segoe UI", 12, "bold"),
    bg="#007ACC",
    fg="white",
    width=35,
    command=recommend_career
)

recommend_btn.pack(pady=15)

# =====================================
# MATCH SCORE
# =====================================

progress = ttk.Progressbar(
    root,
    length=500,
    mode="determinate"
)

progress.pack(pady=10)

# =====================================
# RESULT SECTION
# =====================================

result_frame = tk.LabelFrame(
    root,
    text="🎯 Recommendation Result",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E1E",
    fg="cyan",
    padx=15,
    pady=15
)

result_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

result_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 18, "bold"),
    bg="#1E1E1E",
    fg="lime"
)

result_label.pack(pady=10)

salary_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 12),
    bg="#1E1E1E",
    fg="white",
    justify="left"
)

salary_label.pack(pady=5)

skills_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 12),
    bg="#1E1E1E",
    fg="white",
    justify="left"
)

skills_label.pack(pady=5)

roadmap_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 12),
    bg="#1E1E1E",
    fg="white",
    justify="left"
)

roadmap_label.pack(pady=5)

# =====================================
# TOP 3 CAREERS
# =====================================

top3_frame = tk.LabelFrame(
    root,
    text="🏆 Top 3 Career Matches",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E1E",
    fg="gold",
    padx=10,
    pady=10
)

top3_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

top3_label = tk.Label(
    top3_frame,
    text="No Recommendation Yet",
    font=("Segoe UI", 14, "bold"),
    bg="#1E1E1E",
    fg="gold",
    justify="left"
)

top3_label.pack()

# =====================================
# CONTROL BUTTONS
# =====================================

button_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

button_frame.pack(pady=15)

history_btn = tk.Button(
    button_frame,
    text="📜 View History",
    width=18,
    command=view_history
)

history_btn.grid(
    row=0,
    column=0,
    padx=5
)

save_btn = tk.Button(
    button_frame,
    text="💾 Save Report",
    width=18,
    command=save_report
)

save_btn.grid(
    row=0,
    column=1,
    padx=5
)

dark_btn = tk.Button(
    button_frame,
    text="🌙 Dark Theme",
    width=18,
    command=dark_theme
)

dark_btn.grid(
    row=0,
    column=2,
    padx=5
)

light_btn = tk.Button(
    button_frame,
    text="☀ Light Theme",
    width=18,
    command=light_theme
)

light_btn.grid(
    row=0,
    column=3,
    padx=5
)

exit_btn = tk.Button(
    button_frame,
    text="❌ Exit",
    width=18,
    command=root.destroy
)

exit_btn.grid(
    row=0,
    column=4,
    padx=5
)

# =====================================
# STATUS BAR
# =====================================

status_bar = tk.Label(
    root,
    text="Ready | AI Career Recommendation System Pro",
    bd=1,
    relief=tk.SUNKEN,
    anchor=tk.W
)

status_bar.pack(
    side=tk.BOTTOM,
    fill=tk.X
)

# =====================================
# FOOTER
# =====================================

footer = tk.Label(
    root,
    text="CODSOFT Internship Project | Developed using Python & Tkinter",
    bg="#1E1E1E",
    fg="gray",
    font=("Segoe UI", 10)
)

footer.pack(
    side="bottom",
    pady=5
)

# =====================================
# START APPLICATION
# =====================================

root.mainloop()