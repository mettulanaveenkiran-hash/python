import tkinter as tk

root = tk.Tk()

frame = tk.frame(root)
frame.pack()

tk.lable(frame, text="Inside Frame").pack()

root.mainloop()
