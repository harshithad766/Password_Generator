import tkinter as tk
from tkinter import messagebox
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")  # Set the title of the GUI window

        self.numPasswords = 0  # Initialize the number of passwords to generate
        self.passwordLengths = []  # Initialize a list to store the lengths of the passwords

        # Label to ask how many passwords to generate
        self.label1 = tk.Label(root, text="How many passwords do you want to generate?")
        self.label1.pack(pady=10)

        # Entry to input the number of passwords
        self.numPasswords_entry = tk.Entry(root, width=50)
        self.numPasswords_entry.pack(pady=10)

        # Button to submit the number of passwords
        self.numPasswords_button = tk.Button(root, text="Submit", command=self.get_num_passwords)
        self.numPasswords_button.pack(pady=5)

        # Label to prompt the user to enter the lengths of the passwords
        self.lengths_label = tk.Label(root, text="")
        self.lengths_label.pack(pady=10)

        # Entry to input the lengths of the passwords
        self.lengths_entry = tk.Entry(root, width=50)
        self.lengths_entry.pack(pady=10)

        # Button to generate the passwords
        self.lengths_button = tk.Button(root, text="Generate Passwords", command=self.generate_passwords)
        self.lengths_button.pack(pady=5)
        self.lengths_button.config(state=tk.DISABLED)  # Disable the button until the number of passwords is provided

        # Label to display the generated passwords
        self.passwords_label = tk.Label(root, text="")
        self.passwords_label.pack(pady=10)

        # Button to quit the application
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def get_num_passwords(self):
        try:
            # Get the number of passwords from the entry
            self.numPasswords = int(self.numPasswords_entry.get())
            if self.numPasswords <= 0:
                raise ValueError("Number of passwords must be greater than 0")
            # Prompt the user to enter the lengths of the passwords
            self.lengths_label.config(text=f"Enter the lengths of {self.numPasswords} passwords (comma-separated):")
            self.numPasswords_entry.config(state=tk.DISABLED)  # Disable the entry after getting the number
            self.numPasswords_button.config(state=tk.DISABLED)  # Disable the submit button
            self.lengths_button.config(state=tk.NORMAL)  # Enable the generate passwords button
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))  # Show a warning if input is invalid

    def generate_passwords(self):
        try:
            # Get the lengths of the passwords from the entry
            lengths = list(map(int, self.lengths_entry.get().split(',')))
            if len(lengths) != self.numPasswords:
                raise ValueError(f"Please enter exactly {self.numPasswords} lengths.")
            for length in lengths:
                if length < 3:
                    raise ValueError("Minimum length of password should be 3")
            self.passwordLengths = lengths
            # Generate passwords based on the lengths provided
            passwords = self.generatePassword(self.passwordLengths)
            # Display the generated passwords
            self.passwords_label.config(text="\n".join([f"Password #{i+1} = {password}" for i, password in enumerate(passwords)]))
            self.lengths_button.config(state=tk.DISABLED)  # Disable the generate passwords button after generation
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))  # Show a warning if input is invalid

    def generatePassword(self, pwlength):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        passwords = [] 
        for i in pwlength:
            password = "" 
            for j in range(i):
                next_letter_index = random.randrange(len(alphabet))
                password += alphabet[next_letter_index]
            # Replace some letters with numbers
            password = self.replaceWithNumber(password)
            # Replace some letters with uppercase letters
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
    root = tk.Tk()  # Create the main window
    app = PasswordGenerator(root)  # Create an instance of the PasswordGenerator class
    root.mainloop()  # Run the application

