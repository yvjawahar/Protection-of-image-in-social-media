import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Create a Tkinter window
root = tk.Tk()

# Set the window title and size
root.title("Watermark Detection")
root.geometry("500x500")
root.configure(bg='#0A4A6B')

# Initialize watermark_path and watermarked_path variables
watermark_path = ""
watermarked_path = ""


# Create a label for the watermark image
watermark_label = tk.Label(root, text="Select the watermark image:")
watermark_label.pack()

# Create a button to allow the user to select the watermark image
def select_watermark():
    global watermark_path
    watermark_path = filedialog.askopenfilename()
    watermark_img = Image.open(watermark_path)
    watermark_img = watermark_img.resize((150, 150))
    watermark_img_tk = ImageTk.PhotoImage(watermark_img)
    watermark_display.configure(image=watermark_img_tk)
    watermark_display.image = watermark_img_tk
    watermark_display.pack()

watermark_button = tk.Button(root, text="Select Watermark Image", command=select_watermark,font=('Arial', 14), bg='#FFC857', fg='#333333')
watermark_button.pack()

# Create a label for the watermarked image
watermarked_label = tk.Label(root, text="Select the watermarked image:")
watermarked_label.pack()

# Create a button to allow the user to select the watermarked image
def select_watermarked():
    global watermarked_path
    watermarked_path = filedialog.askopenfilename()
    watermarked_img = Image.open(watermarked_path)
    watermarked_img = watermarked_img.resize((150, 150))
    watermarked_img_tk = ImageTk.PhotoImage(watermarked_img)
    watermarked_display.configure(image=watermarked_img_tk)
    watermarked_display.image = watermarked_img_tk
    watermarked_display.pack()

watermarked_button = tk.Button(root, text="Select Watermarked Image", command=select_watermarked,font=('Arial', 14), bg='#FFC857', fg='#333333')
watermarked_button.pack()

# Create a label to display the result
result_label = tk.Label(root)
result_label.pack()

# Create a button to perform the watermark detection
def detect_watermark():
    # Load the watermark and watermarked images
    watermark = cv2.imread(watermark_path, cv2.IMREAD_GRAYSCALE)
    watermarked = cv2.imread(watermarked_path, cv2.IMREAD_GRAYSCALE)

    # Check if the size of the watermark image is not larger than the watermarked image
    if watermark.shape[0] > watermarked.shape[0] or watermark.shape[1] > watermarked.shape[1]:
        result_label.configure(text="Error: Watermark image cannot be larger than the watermarked image.")
        return

    # Apply template matching using the watermark image as the template
    result = cv2.matchTemplate(watermarked, watermark, cv2.TM_CCOEFF_NORMED)

    # Define a threshold value to determine if the watermark is present or not
    threshold = 0.8

    # Find the location(s) where the template matches the image above the threshold
    locations = np.where(result >= threshold)
    if locations[0].size > 0:
        result_label.configure(text="Watermark found!")
    else:
        result_label.configure(text="Watermark not found.")

detect_button = tk.Button(root, text="Detect Watermark", command=detect_watermark,font=('Arial', 14), bg='#FFC857', fg='#333333')
detect_button.pack()

# Create labels to display the selected images
watermark_display = tk.Label(root)
watermarked_display = tk.Label(root)

# Start the Tkinter event loop
root.mainloop()

