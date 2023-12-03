import tkinter as tk
import random
import string

def generate_random_word(length=8):
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))

def display_random_word():
    random_word = generate_random_word()
    word_label.config(text="Random Word: " + random_word)

# Create the main window
root = tk.Tk()
root.title("Random Word Generator")

# Create a label to display the random word
word_label = tk.Label(root, text="Random Word: ")
word_label.pack(pady=10)

# Create a button to generate and display a random word
generate_button = tk.Button(root, text="Generate Random Word", command=display_random_word)
generate_button.pack(pady=10)

# Run the main event loop
root.mainloop()
