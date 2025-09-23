import tkinter as tk
from tkinter import messagebox

# ------------------ Functions ------------------
allowed_chars = "0123456789+-*/."

def click_button(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + str(value))

def clear_display():
    entry_display.delete(0, tk.END)

def calculate(event=None):
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")

def validate_input(event):
    if (event.char not in allowed_chars and 
        event.keysym not in ("Return", "BackSpace", "Delete")):
        return "break"

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("🧮 Calculator")
root.geometry("400x500")
root.minsize(400, 500)
root.maxsize(800, 700)
root.eval('tk::PlaceWindow . center')

# ------------------ Outer Frame (centered) ------------------
outer_frame = tk.Frame(root)
outer_frame.pack(anchor="n", pady=20)  # Top-center alignment

# ------------------ Inner Frame ------------------
main_frame = tk.Frame(outer_frame)
main_frame.pack()  # keeps content compact and centered

# Heading
tk.Label(main_frame, text="🧮 Calculator", font=("Arial", 20, "bold")).pack(pady=10)

# Display Entry
entry_display = tk.Entry(main_frame, width=20, font=("Arial", 20), justify="right")
entry_display.pack(pady=10)
entry_display.bind("<Key>", validate_input)
entry_display.bind("<Return>", calculate)

# Buttons Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(main_frame)
    row_frame.pack(pady=5)
    for btn_text in row:
        if btn_text == "=":
            b = tk.Button(row_frame, text=btn_text, width=5, height=2, font=("Arial", 14),
                          bg="#4CAF50", fg="white", command=calculate)
        else:
            b = tk.Button(row_frame, text=btn_text, width=5, height=2, font=("Arial", 14),
                          command=lambda val=btn_text: click_button(val))
        b.pack(side=tk.LEFT, padx=5)

# Clear button (full width under all buttons)
tk.Button(main_frame, text="C", width=23, height=2, font=("Arial", 14),
          bg="#f44336", fg="white", command=clear_display).pack(pady=10)

root.mainloop()
