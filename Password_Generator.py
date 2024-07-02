import tkinter as tk
from tkinter import messagebox
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.numPasswords = 0
        self.passwordLengths = []

        self.label1 = tk.Label(root, text="How many passwords do you want to generate?")
        self.label1.pack(pady=10)

        self.numPasswords_entry = tk.Entry(root, width=50)
        self.numPasswords_entry.pack(pady=10)

        self.numPasswords_button = tk.Button(root, text="Submit", command=self.get_num_passwords)
        self.numPasswords_button.pack(pady=5)

        self.lengths_label = tk.Label(root, text="")
        self.lengths_label.pack(pady=10)

        self.lengths_entry = tk.Entry(root, width=50)
        self.lengths_entry.pack(pady=10)

        self.lengths_button = tk.Button(root, text="Generate Passwords", command=self.generate_passwords)
        self.lengths_button.pack(pady=5)
        self.lengths_button.config(state=tk.DISABLED)

        self.passwords_label = tk.Label(root, text="")
        self.passwords_label.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def get_num_passwords(self):
        try:
            self.numPasswords = int(self.numPasswords_entry.get())
            if self.numPasswords <= 0:
                raise ValueError("Number of passwords must be greater than 0")
            self.lengths_label.config(text=f"Enter the lengths of {self.numPasswords} passwords (comma-separated):")
            self.numPasswords_entry.config(state=tk.DISABLED)
            self.numPasswords_button.config(state=tk.DISABLED)
            self.lengths_button.config(state=tk.NORMAL)
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    def generate_passwords(self):
        try:
            lengths = list(map(int, self.lengths_entry.get().split(',')))
            if len(lengths) != self.numPasswords:
                raise ValueError(f"Please enter exactly {self.numPasswords} lengths.")
            for length in lengths:
                if length < 3:
                    raise ValueError("Minimum length of password should be 3")
            self.passwordLengths = lengths
            passwords = self.generatePassword(self.passwordLengths)
            self.passwords_label.config(text="\n".join([f"Password #{i+1} = {password}" for i, password in enumerate(passwords)]))
            self.lengths_button.config(state=tk.DISABLED)
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    def generatePassword(self, pwlength):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        passwords = [] 
        for i in pwlength:
            password = "" 
            for j in range(i):
                next_letter_index = random.randrange(len(alphabet))
                password += alphabet[next_letter_index]
            password = self.replaceWithNumber(password)
            password = self.replaceWithUppercaseLetter(password)
            passwords.append(password)
        return passwords

    def replaceWithNumber(self, pword):
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(pword) // 2)
            pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
        return pword

    def replaceWithUppercaseLetter(self, pword):
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(pword) // 2, len(pword))
            pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
        return pword

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
