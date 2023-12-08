import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageEnhance

def open_image():
    global img_watermarked, img_watermarked_width, img_watermarked_height
    file_path = tk.filedialog.askopenfilename()
    img_watermarked = Image.open(file_path)
    img_watermarked_width, img_watermarked_height = img_watermarked.size
   

def save_image():
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".png")
    img_result.save(file_path)

def apply_logo():
    global img_logo, img_logo_width, img_logo_height, img_result
    logo_file_path = tk.filedialog.askopenfilename()
    img_logo = Image.open(logo_file_path)
    img_logo_width, img_logo_height = img_logo.size
    img_result = Image.new("RGB", (img_watermarked_width, img_watermarked_height))
    img_result.paste(img_watermarked, (0, 0))
    img_result.paste(img_logo, (100, 100))
    enhancer = ImageEnhance.Brightness(img_logo)
    img_logo_lightened = enhancer.enhance(1.5)
    logo_new_size = (int(img_logo_width/2), int(img_logo_height/2))
    img_logo_resized = img_logo_lightened.resize(logo_new_size)
    img_result.paste(img_logo_resized, (150, 150))
   

# Create tkinter root
root = tk.Tk()
root.title('ATTACK')
root.geometry('300x200')
root.configure(bg='#0A4A6B')


# Create open image button
btn_open_image = tk.Button(root, text="Open Image", command=open_image,font=('Arial', 14), bg='#FFC857', fg='#333333')
btn_open_image.pack()

# Create apply logo button
btn_apply_logo = tk.Button(root, text="Attack", command=apply_logo,font=('Arial', 14), bg='#FFC857', fg='#333333')
btn_apply_logo.pack()

# Create save image button
btn_save_image = tk.Button(root, text="Save Image", command=save_image,font=('Arial', 14), bg='#FFC857', fg='#333333')
btn_save_image.pack()

# Run tkinter event loop
root.mainloop()
