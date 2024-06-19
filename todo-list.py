# Import necessary modules
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

# Database operations
class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connection = sql.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

def add_task_to_db(task):
    # Add a task to the database
    with Database('listOfTasks.db') as cursor:
        cursor.execute('INSERT INTO tasks VALUES (?)', (task,))

def delete_task_from_db(task):
    # Delete a task from the database
    with Database('listOfTasks.db') as cursor:
        cursor.execute('DELETE FROM tasks WHERE title = ?', (task,))

def delete_all_tasks_from_db():
    # Delete all tasks from the database
    with Database('listOfTasks.db') as cursor:
        cursor.execute('DELETE FROM tasks')

def fetch_tasks_from_db():
    # Fetch all tasks from the database
    with Database('listOfTasks.db') as cursor:
        cursor.execute('SELECT title FROM tasks')
        return [row[0] for row in cursor.fetchall()]

# Task list operations
def add_task():
    # Add a task to the list and database
    task = task_field.get()
    if not task:
        messagebox.showinfo('Error', 'Field is Empty.')
        return

    tasks.append(task)
    add_task_to_db(task)
    update_task_list()
    task_field.delete(0, 'end')

def delete_task():
    # Delete a task from the list and database
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        tasks.remove(selected_task)
        delete_task_from_db(selected_task)
        update_task_list()
    except tk.TclError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    # Delete all tasks from the list and database
    if messagebox.askyesno('Delete All', 'Are you sure?'):
        tasks.clear()
        delete_all_tasks_from_db()
        update_task_list()

def update_task_list():
    # Update the task listbox with tasks
    clear_task_list()
    for task in tasks:
        task_listbox.insert('end', task)

def clear_task_list():
    # Clear all tasks from the task listbox
    task_listbox.delete(0, 'end')

def close_app():
    # Close the application
    guiWindow.destroy()

def load_tasks():
    # Load tasks from the database
    tasks.clear()
    tasks.extend(fetch_tasks_from_db())

def display_tasks():
    # Display tasks from the database in the console
    print("Tasks:")
    with Database('listOfTasks.db') as cursor:
        cursor.execute('SELECT * FROM tasks')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
# GUI setup
def setup_gui():
    global guiWindow, task_field, task_listbox
    # Create the main window
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#C6CDC4")

    # Frames to organize GUI elements
    header_frame = tk.Frame(guiWindow, bg="#C6CDC4")
    functions_frame = tk.Frame(guiWindow, bg="#C6CDC4")
    listbox_frame = tk.Frame(guiWindow, bg="#C6CDC4")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    # Header label
    header_label = ttk.Label(header_frame, text="The To-Do List", font=("Lucida Calligraphy", 30,"bold"), background="#C6CDC4", foreground="#AF211D")
    header_label.pack(padx=40, pady=30)
    
    # Label and Entry for task input
    task_label = ttk.Label(functions_frame, text="Enter the Task:", font=("Times New Roman", 14, "bold"), background="#C6CDC4", foreground="#000000")
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(functions_frame, font=("Times New Roman", 12), width=18, background="#FFF8DC", foreground="#A52A2A")
    task_field.place(x=30, y=80)
     
    # Buttons for task operations
    add_button = ttk.Button(functions_frame, text="Add Task", width=24, command=add_task)
    del_button = ttk.Button(functions_frame, text="Delete Task", width=24, command=delete_task)
    del_all_button = ttk.Button(functions_frame, text="Delete All Tasks", width=24, command=delete_all_tasks)
    exit_button = ttk.Button(functions_frame, text="Exit", width=24, command=close_app)
    display_button = ttk.Button(functions_frame, text="Display Tasks", width=24, command=display_tasks)

    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)
    display_button.place(x=30, y=280)

    # Task listbox
    task_listbox = tk.Listbox(listbox_frame, width=26, height=13, selectmode='SINGLE', background="#FAF9F6", foreground="#000000", selectbackground="#A52A2A", selectforeground="#FFFFFF")
    task_listbox.place(x=40, y=80)

if __name__ == "__main__":
    tasks = []

    setup_gui()
    load_tasks()  # Load tasks from the database when the application starts
    update_task_list()  # Update the task listbox
    guiWindow.mainloop()  # Start the GUI event loop
