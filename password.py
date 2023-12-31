import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip

def generate_password():
    try:
        length = int(entry_length.get())

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password, fg="#006400")
        return password
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length")

def copy_password():
    try:
        password = generate_password()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!", icon="info")
    except AttributeError:
        messagebox.showwarning("No Password Generated", "Please generate a password first.", icon="warning")

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x250")
root.configure(bg="#A9A9A9")

length_label = tk.Label(root, text="Enter Password Length:", bg="#A9A9A9", font=("Arial", 14), fg="#2F4F4F")
length_label.grid(row=0, column=0, padx=20, pady=10)

entry_length = tk.Entry(root, font=("Arial", 14), bg="#D3D3D3")
entry_length.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#4682B4', fg="white", font=("Arial", 14))
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password, bg='#4682B4', fg="white", font=("Arial", 14))
copy_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, bg="#A9A9A9", font=("Arial", 16), fg="#006400")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
