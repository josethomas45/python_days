import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("500x500")
root.configure(bg="#FFFFFF")  

# Load and set background image if it exists
image_path = r"D:\python\python_days\WhatsApp Image 2025-02-09 at 12.08.11 (3).jpeg"  # Use absolute path
if os.path.exists(image_path):
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((500, 500), Image.LANCZOS)  
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = bg_photo  # Keep reference to avoid garbage collection
    bg_label.lower()  # Send it to the background

frame = tk.Frame(root)  
frame.pack(expand=True)

tk.Label(frame, text='First Name', bg="#ADD8E6").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(frame, text='Last Name', bg="#ADD8E6").grid(row=1, column=0, padx=10, pady=5, sticky="w")

e1 = tk.Entry(frame)
e2 = tk.Entry(frame)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def submit_action():
    progress_bar.start()
    root.after(2000, complete_loading)

def complete_loading():
    progress_bar.stop()
    root.destroy()

button = tk.Button(frame, text='SUBMIT', width=25, command=submit_action, bg="red", fg="white")
button.grid(row=2, column=0, columnspan=2, pady=10)

progress_bar = ttk.Progressbar(frame, orient='horizontal', mode='indeterminate')
progress_bar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
