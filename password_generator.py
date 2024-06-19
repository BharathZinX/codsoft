import tkinter as tk
from tkinter import messagebox
import random
import string

# Constants for character sets
ALPHABETS = string.ascii_letters
DIGITS = string.digits
SPECIAL_CHARACTERS = "!@#$%^&*()"

# Function to generate a password
def generate_password(length_entry, alphabets_entry, digits_entry, special_characters_entry, password_entry):
    try:
        length = int(length_entry.get())
        alphabets_count = int(alphabets_entry.get())
        digits_count = int(digits_entry.get())
        special_characters_count = int(special_characters_entry.get())

        characters_count = alphabets_count + digits_count + special_characters_count

        if characters_count > length:
            raise ValueError("Characters total count is greater than the password length")

        password = generate_random_password(length, alphabets_count, digits_count, special_characters_count)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to generate random password based on given parameters
def generate_random_password(length, alphabets_count, digits_count, special_characters_count):
    password = []

    for _ in range(alphabets_count):
        password.append(random.choice(ALPHABETS))

    for _ in range(digits_count):
        password.append(random.choice(DIGITS))

    for _ in range(special_characters_count):
        password.append(random.choice(SPECIAL_CHARACTERS))

    total_characters = alphabets_count + digits_count + special_characters_count
    if total_characters < length:
        all_characters = ALPHABETS + DIGITS + SPECIAL_CHARACTERS
        for _ in range(length - total_characters):
            password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)

# Function to create UI elements
def create_ui(root):
    root.title("Custom Password Generator")
    root.geometry("500x400")
    root.configure(bg='burlywood1')

    length_label, length_entry = create_entry(root, "Length:", 20, pady=5)
    alphabets_label, alphabets_entry = create_entry(root, "Alphabets Count:", 20, pady=5)
    digits_label, digits_entry = create_entry(root, "Digits Count:", 20, pady=5)
    special_characters_label, special_characters_entry = create_entry(root, "Special Characters Count:", 20, pady=5)

    generate_button = tk.Button(root, text="Generate Password", command=lambda: generate_password(length_entry, alphabets_entry, digits_entry, special_characters_entry, password_entry), bg='burlywood')
    generate_button.pack(pady=5)

    global password_entry
    password_label = tk.Label(root, text="Generated Password:", bg='burlywood')
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, width=30)
    password_entry.pack(pady=5)

# Function to create label and entry pair
def create_entry(root, label_text, width, pady):
    label = tk.Label(root, text=label_text, bg='burlywood')
    label.pack(pady=pady)
    entry = tk.Entry(root, width=width)
    entry.pack(pady=5)
    return label, entry

# Create the main window and start the GUI event loop
if __name__ == "__main__":
    root = tk.Tk()
    create_ui(root)
    root.mainloop()
