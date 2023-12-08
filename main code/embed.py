import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Define root window
root = tk.Tk()
root.configure(bg='#0A4A6B')

# Define file paths
main_file = ""
logo_file = ""

# Function to open image files
def open_file(type):
    global main_file, logo_file
    # Open file dialog and get selected file path
    file_path = filedialog.askopenfilename(filetypes=[(type, "*." + type)])
    # Set global variable to selected file path
    if type == "jpg":
        main_file = file_path
    elif type == "png":
        logo_file = file_path

# Function to save result image
def save_image():
    global main_file, logo_file
    # Open main image and logo image with Pillow
    img_main = Image.open(main_file)
    img_logo = Image.open(logo_file)
    # Get image sizes
    img_main_width, img_main_height = img_main.size

    img_logo_width, img_logo_height = img_logo.size

    #checks the size of logo width/height compares with main width/height
    if img_logo_width > img_main_width or img_logo_height > img_main_height:
        tk.messagebox.showerror("Error", "Logo size is larger than main image size.")
        return

    # Create blank Pillow image
    img_result = Image.new("RGB", (img_main_width, img_main_height))
    # Paste main image onto result image
    img_result.paste(img_main, (0, 0))
    # Paste logo image onto result image
    img_result.paste(img_logo, (100, 100))
    # Save result image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    img_result.save(file_path)

# Define input frame
frm_input = tk.Frame(root)
lbl_main = tk.Label(frm_input, text="Main Image:",font=('Arial', 14), bg='#FFC857', fg='#333333')
lbl_main.pack(pady=20, padx=20, fill=tk.BOTH)
btn_main = tk.Button(frm_input, text="Open Image", command=lambda: open_file("jpg"),font=('Arial', 14), bg='#FFC857', fg='#333333')
btn_main.pack(pady=20, padx=20, fill=tk.BOTH)
lbl_logo = tk.Label(frm_input, text="Logo:",font=('Arial', 14), bg='#FFC857', fg='#333333')
lbl_logo.pack(pady=20, padx=20, fill=tk.BOTH)
btn_logo = tk.Button(frm_input, text="Open Image", command=lambda: open_file("png"),font=('Arial', 14), bg='#FFC857', fg='#333333')
btn_logo.pack(pady=20, padx=20, fill=tk.BOTH)
frm_input.pack()

# # Define preview frame
# frm_preview = tk.Frame(root)
# lbl_preview = tk.Label(frm_preview)
# lbl_preview.pack()
# frm_preview.pack()

# Define output frame
frm_output = tk.Frame(root)
btn_save = tk.Button(frm_output, text="Save as PNG", command=save_image,font=('Arial', 14), bg='#FFC857', fg='#333333')
btn_save.pack()
frm_output.pack()

# Run root window main loop
root.mainloop()
