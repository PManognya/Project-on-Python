#Typing Speed Test in Python
from tkinter import *
import random
import time

SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog while the sun sets slowly",
    "Python is a powerful programming language used for web development and data science",
    "Practice makes perfect when it comes to improving your typing speed and accuracy",
    "Consistency and patience are the keys to mastering any new skill over time",
    "Success comes from hard work dedication and a willingness to keep learning daily"
]

start_time = None
current_text = ""

def new_text():
    global current_text
    current_text = random.choice(SAMPLE_TEXTS)
    sample_label.config(text=current_text)
    input_entry.delete(0, END)
    result_label.config(text="")

def start_test(event=None):
    global start_time
    if start_time is None:
        start_time = time.time()

def check_result(event=None):
    global start_time
    if start_time is None:
        return

    typed_text = input_entry.get()
    elapsed_time = time.time() - start_time
    elapsed_minutes = elapsed_time / 60

    typed_words = typed_text.split()
    wpm = round(len(typed_words) / elapsed_minutes) if elapsed_minutes > 0 else 0

    # Accuracy check
    original_words = current_text.split()
    correct_words = sum(
        1 for i, word in enumerate(typed_words)
        if i < len(original_words) and word == original_words[i]
    )
    accuracy = round((correct_words / len(original_words)) * 100) if original_words else 0

    result_label.config(
        text=f"Time: {round(elapsed_time, 1)}s | Speed: {wpm} WPM | Accuracy: {accuracy}%"
    )
    start_time = None

def on_key_release(event):
    typed_text = input_entry.get()
    if typed_text == current_text:
        check_result()

# --- GUI Setup ---
window = Tk()
window.title("Typing Speed Test")
window.config(padx=40, pady=40, bg="#2C3E50")

title_label = Label(window, text="Typing Speed Test", font=("Arial", 20, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

sample_label = Label(window, text="", font=("Arial", 14), wraplength=500, bg="#2C3E50", fg="#ECF0F1", justify="center")
sample_label.pack(pady=20)

input_entry = Entry(window, width=60, font=("Arial", 12))
input_entry.pack(pady=10)
input_entry.bind("<Key>", start_test)
input_entry.bind("<KeyRelease>", on_key_release)

result_label = Label(window, text="", font=("Arial", 12, "bold"), bg="#2C3E50", fg="#2ECC71")
result_label.pack(pady=10)

new_button = Button(window, text="New Text", command=new_text, font=("Arial", 11))
new_button.pack(pady=10)

new_text()  # load first sample on startup

window.mainloop()