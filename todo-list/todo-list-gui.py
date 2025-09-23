import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"title": task, "done": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        refresh_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Mark task as done
def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        save_tasks(tasks)
        refresh_list()
    else:
        messagebox.showwarning("Warning", "Please select a task!")

# Delete task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        save_tasks(tasks)
        refresh_list()
    else:
        messagebox.showwarning("Warning", "Please select a task!")

# Edit task
def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        old_task = tasks[index]["title"]
        new_task = simpledialog.askstring("Edit Task", f"Edit task:", initialvalue=old_task)
        if new_task and new_task.strip():
            tasks[index]["title"] = new_task.strip()
            save_tasks(tasks)
            refresh_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to edit!")

# Refresh task list
def refresh_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["done"] else "❌"
        listbox.insert(tk.END, f"{task['title']} {status}")

# ---------------------- GUI ----------------------
root = tk.Tk()
root.title("✅ To-Do List App")
root.geometry("600x500")
root.resizable(True, True)  # Allow resizing

tasks = load_tasks()

# ------------------ Heading ------------------
tk.Label(root, text="📝 My To-Do List", font=("Arial", 20, "bold")).pack(pady=10)

# Input field
task_entry = tk.Entry(root, width=40, font=("Arial", 14))
task_entry.pack(pady=10, padx=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", width=12)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="Mark Done", command=mark_done, bg="#2196F3", fg="white", width=12)
done_btn.grid(row=0, column=1, padx=5)

del_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white", width=12)
del_btn.grid(row=0, column=2, padx=5)

edit_btn = tk.Button(btn_frame, text="Edit Task", command=edit_task, bg="#FF9800", fg="white", width=12)
edit_btn.grid(row=0, column=3, padx=5)

# Scrollbar and Listbox
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, font=("Arial", 12), yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

refresh_list()

root.mainloop()
