import tkinter as tk
import os

# Function to navigate to the watermark embedding page
def embed_watermark():
    os.system('python embed.py')

# Function to navigate to the watermark detection page
def detect_watermark():
    os.system('python fulldetection.py')

# Function to navigate to the encrytion decryption page
def encrypt_decrypt():
    os.system('python e_d.py')

def attack():
    os.system('python attack_fin.py')

# Create a Tkinter window
root = tk.Tk()

# Set the title and size of the window
root.title('Watermarking')
root.geometry('300x200')
root.configure(bg='#0A4A6B')

# Create the "Embed Watermark" button
embed_button = tk.Button(root, text='Embed Watermark', command=embed_watermark, font=('Arial', 14), bg='#FFC857', fg='#333333')
embed_button.pack(pady=20, padx=20, fill=tk.BOTH)

# Create the "Detect Watermark" button
detect_button = tk.Button(root, text='Detect Watermark', command=detect_watermark, font=('Arial', 14), bg='#FFC857', fg='#333333')
detect_button.pack(pady=20, padx=20, fill=tk.BOTH)

# Create the "encryption/decryption" button
detect_button = tk.Button(root, text='Encryption Decryption', command=encrypt_decrypt, font=('Arial', 14), bg='#FFC857', fg='#333333')
detect_button.pack(pady=20, padx=20, fill=tk.BOTH)

# Create the "attack" button
attack_button = tk.Button(root, text='Attack', command=attack, font=('Arial', 14), bg='#FFC857', fg='#333333')
attack_button.pack(pady=20, padx=20, fill=tk.BOTH)

# Start the Tkinter event loop
root.mainloop()
