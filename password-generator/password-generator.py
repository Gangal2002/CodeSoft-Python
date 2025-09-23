import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# ---------------- Functions ----------------
def generate_password():
    """Generates a strong random password and updates strength indicator."""
    try:
        length = int(spin_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter a positive number")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    # Characters: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    # Reset Entry to normal temporarily
    entry_password.config(state="normal")
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    entry_password.config(state="readonly")

    # Ensure password is visible after generation
    entry_password.config(show="")  
    btn_show_hide.config(text="Hide")  # Update toggle button to match

    update_strength(password)

def copy_to_clipboard():
    if entry_password.get():
        root.clipboard_clear()
        root.clipboard_append(entry_password.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def toggle_show_password():
    if entry_password.cget('show') == "":
        entry_password.config(show="*")
        btn_show_hide.config(text="Show")
    else:
        entry_password.config(show="")
        btn_show_hide.config(text="Hide")

def update_strength(password):
    """Simple strength indicator based on length and character variety."""
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    # Update progress bar
    progress_strength['value'] = score
    if score <= 2:
        lbl_strength.config(text="Weak", fg="red")
    elif score <= 4:
        lbl_strength.config(text="Medium", fg="orange")
    else:
        lbl_strength.config(text="Strong", fg="green")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🔒 Professional Password Generator")
root.geometry("450x350")
root.minsize(400, 350)
root.eval('tk::PlaceWindow . center')

# ---------------- Top-Centered Frame ----------------
main_frame = tk.Frame(root)
main_frame.pack(anchor="n", pady=20)

# Heading
tk.Label(main_frame, text="🔒 Password Generator", font=("Arial", 20, "bold")).pack(pady=10)

# Length input
frame_length = tk.Frame(main_frame)
frame_length.pack(pady=10)
tk.Label(frame_length, text="Password Length:", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)

spin_length = tk.Spinbox(frame_length, from_=4, to=32, font=("Arial", 14), width=5)
spin_length.pack(side=tk.LEFT, padx=5)
spin_length.delete(0, "end")  # Make empty by default

# Generate button
tk.Button(main_frame, text="Generate Password", font=("Arial", 14), width=20,
          command=generate_password).pack(pady=15)

# Password display
frame_password = tk.Frame(main_frame)
frame_password.pack(pady=5)

tk.Label(frame_password, text="Generated Password:", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
entry_password = tk.Entry(frame_password, font=("Arial", 14), width=25, justify="center", state="readonly")
entry_password.pack(side=tk.LEFT, padx=5)

# Buttons for copy and show/hide
btn_frame = tk.Frame(main_frame)
btn_frame.pack(pady=5)
btn_copy = tk.Button(btn_frame, text="Copy", font=("Arial", 12), width=10, command=copy_to_clipboard)
btn_copy.pack(side=tk.LEFT, padx=5)
btn_show_hide = tk.Button(btn_frame, text="Hide", font=("Arial", 12), width=10, command=toggle_show_password)
btn_show_hide.pack(side=tk.LEFT, padx=5)

# Strength indicator
frame_strength = tk.Frame(main_frame)
frame_strength.pack(pady=10)
tk.Label(frame_strength, text="Strength:", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
progress_strength = ttk.Progressbar(frame_strength, length=200, maximum=5)
progress_strength.pack(side=tk.LEFT, padx=5)
lbl_strength = tk.Label(frame_strength, text="", font=("Arial", 14))
lbl_strength.pack(side=tk.LEFT, padx=5)

root.mainloop()

