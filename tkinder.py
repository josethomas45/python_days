import tkinter as tk


root = tk.Tk()
root.title("Tkinter Example")
root.geometry("500x500")
root.configure(bg="#ADD8E6")  

frame = tk.Frame(root, bg="#ADD8E6")
frame.pack(expand=True)


tk.Label(frame, text='First Name', bg="#ADD8E6").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(frame, text='Last Name', bg="#ADD8E6").grid(row=1, column=0, padx=10, pady=5, sticky="w")


e1 = tk.Entry(frame)
e2 = tk.Entry(frame)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


button = tk.Button(frame, text='SUBMIT', width=25, command=root.destroy, bg="red", fg="white")
button.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
