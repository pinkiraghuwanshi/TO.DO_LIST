import tkinter as tk
from tkinter import messagebox, filedialog
import os
import csv

# File to store tasks
TASK_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    """Load tasks from file when program starts"""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

# Function to save tasks to file
def save_tasks():
    """Save tasks to a file when updated"""
    with open(TASK_FILE, "w") as file:
        for task in listbox.get(0, tk.END):
            file.write(task + "\n")

# Function to add task
def add_task():
    """Add new task to listbox"""
    task = entry.get()
    priority = priority_var.get()
    category = category_var.get()

    if task:
        task_info = f"{task} | Priority: {priority} | Category: {category}"
        listbox.insert(tk.END, task_info)
        entry.delete(0, tk.END)
        save_tasks()  # Save after adding
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove selected task
def remove_task():
    """Remove selected task from listbox"""
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        save_tasks()  # Save after removing
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

# Function to enable dark mode
def toggle_dark_mode():
    """Toggle dark mode for better UI experience"""
    if dark_mode.get():
        root.config(bg="black")
        listbox.config(bg="gray", fg="white")
    else:
        root.config(bg="white")
        listbox.config(bg="white", fg="black")

# Function to export tasks to CSV
def export_to_csv():
    """Export tasks to a CSV file"""
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task", "Priority", "Category"])
            for task in listbox.get(0, tk.END):
                writer.writerow(task.split(" | "))
        messagebox.showinfo("Export", "Tasks exported successfully!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")

# Dark Mode Toggle
dark_mode = tk.BooleanVar()
dark_mode_button = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode)
dark_mode_button.pack()

# Task Entry
frame = tk.Frame(root)
frame.pack(pady=5)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.RIGHT)

# Priority Dropdown
priority_var = tk.StringVar(value="Medium")
priority_label = tk.Label(root, text="Priority:")
priority_label.pack()
priority_dropdown = tk.OptionMenu(root, priority_var, "Urgent", "High", "Medium", "Low")
priority_dropdown.pack()

# Category Dropdown
category_var = tk.StringVar(value="General")
category_label = tk.Label(root, text="Category:")
category_label.pack()
category_dropdown = tk.OptionMenu(root, category_var, "Work", "Personal", "Study", "Health", "Finance")
category_dropdown.pack()

# Listbox for Tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Remove Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Export Button
export_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_button.pack(pady=5)

# Load tasks when program starts
for task in load_tasks():
    listbox.insert(tk.END, task)

# Run the Tkinter main loop
root.mainloop()
