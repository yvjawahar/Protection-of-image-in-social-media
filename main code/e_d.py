from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import filedialog
from Crypto.Util.Padding import pad, unpad

# define the encryption function
def encrypt_image():
    # get the filename and key from the user
    filename = filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=[('JPEG files', '*.jpg','.png')])
    key = key_entry.get().encode('utf-8')
    
    # open the image file and read its contents
    with open(filename, 'rb') as file:
        plaintext = file.read()
    
    # generate a random initialization vector
    iv = get_random_bytes(AES.block_size)
    
    # create the AES cipher object with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

     # pad the plaintext so its length is a multiple of 16 bytes
    padded_plaintext = pad(plaintext, AES.block_size)
    
    # encrypt the padded plaintext with the AES cipher
    ciphertext = cipher.encrypt(padded_plaintext)
    
    # write the encrypted data to a new file
    with open(filename + '.enc', 'wb') as file:
        file.write(iv + ciphertext)
    
    # show a success message
    tk.messagebox.showinfo('Encryption', 'Encryption complete.')

# define the decryption function
def decrypt_image():
    # get the filename and key from the user
    filename = filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=[('Encrypted files', '*.enc')])
    key = key_entry.get().encode('utf-8')
    
    # open the encrypted image file and read its contents
    with open(filename, 'rb') as file:
        ciphertext = file.read()
    
    # extract the initialization vector from the ciphertext
    iv = ciphertext[:AES.block_size]
    
    # create the AES cipher object with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

     # decrypt the ciphertext with the AES cipher
    padded_plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    
    # unpad the plaintext to remove the padding
    plaintext = unpad(padded_plaintext, AES.block_size)
    
 
    
    # write the decrypted data to a new file
    with open(filename[:-4] + '_decrypted.jpg', 'wb') as file:
        file.write(plaintext)
    
    # show a success message
    tk.messagebox.showinfo('Decryption', 'Decryption complete.')

# create the tkinter GUI
root = tk.Tk()
root.title('Image Encryption/Decryption')
root.configure(bg='#0A4A6B')

# create the key entry field
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=0, column=0, padx=5, pady=5)

# create the encrypt button
encrypt_button = tk.Button(root, text='Encrypt', command=encrypt_image,font=('Arial', 14), bg='#FFC857', fg='#333333')
encrypt_button.grid(row=0, column=1, padx=5, pady=5)

# create the decrypt button
decrypt_button = tk.Button(root, text='Decrypt', command=decrypt_image,font=('Arial', 14), bg='#FFC857', fg='#333333')
decrypt_button.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
