import tkinter as tk
from tkinter import messagebox

def click(button_text):
    """Handles button clicks."""
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(True, True)

# Validation function for Entry widget
def validate_input(new_value):
    allowed_chars = "0123456789.+-*/"
    for char in new_value:
        if char not in allowed_chars:
            return False
    return True

vcmd = (root.register(validate_input), "%P")

# Entry display with validation
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge",
                 justify="right", validate="key", validatecommand=vcmd)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
entry.focus_set()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create buttons (mouse clicks)
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "C":
            btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: click(t))
            btn.grid(row=i+1, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        else:
            btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: click(t))
            btn.grid(row=i+1, column=j, sticky="nsew", padx=2, pady=2)

# Make grid cells expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Keyboard bindings (Enter and Clear)
def key_press(event):
    if event.keysym == "Return":
        click("=")
    elif event.keysym in ("BackSpace", "Delete"):
        click("C")
    # All other keys handled by Entry validation

root.bind("<Key>", key_press)

root.mainloop()
