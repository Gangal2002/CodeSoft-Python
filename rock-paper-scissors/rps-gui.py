import tkinter as tk
from tkinter import messagebox
import random

# ---------------- Functions ----------------
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    lbl_computer_choice.config(text=f"Computer chose: {computer_choice}")
    lbl_user_choice.config(text=f"You chose: {choice}")
    
    result = ""
    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Scissors" and computer_choice == "Paper") or \
         (choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1
    
    lbl_result.config(text=result)
    lbl_score.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    lbl_user_choice.config(text="You chose: ")
    lbl_computer_choice.config(text="Computer chose: ")
    lbl_result.config(text="Result: ")
    lbl_score.config(text="Score - You: 0  Computer: 0")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("✊ Rock-Paper-Scissors Game")
root.geometry("450x400")
root.minsize(400, 400)
root.eval('tk::PlaceWindow . center')

# Top-Centered Frame
main_frame = tk.Frame(root)
main_frame.pack(anchor="n", pady=20)

# Heading
tk.Label(main_frame, text="✊ Rock-Paper-Scissors", font=("Arial", 20, "bold")).pack(pady=10)

# Buttons for user choices
btn_frame = tk.Frame(main_frame)
btn_frame.pack(pady=10)
for ch in choices:
    tk.Button(btn_frame, text=ch, font=("Arial", 14), width=10, command=lambda c=ch: play(c)).pack(side=tk.LEFT, padx=5)

# Labels to display choices and result
lbl_user_choice = tk.Label(main_frame, text="You chose: ", font=("Arial", 14))
lbl_user_choice.pack(pady=5)

lbl_computer_choice = tk.Label(main_frame, text="Computer chose: ", font=("Arial", 14))
lbl_computer_choice.pack(pady=5)

lbl_result = tk.Label(main_frame, text="Result: ", font=("Arial", 16, "bold"))
lbl_result.pack(pady=10)

lbl_score = tk.Label(main_frame, text="Score - You: 0  Computer: 0", font=("Arial", 14))
lbl_score.pack(pady=5)

# Reset button
tk.Button(main_frame, text="Reset Game", font=("Arial", 12), width=15, command=reset_game).pack(pady=10)

root.mainloop()
