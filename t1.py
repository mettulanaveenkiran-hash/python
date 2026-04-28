import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")

root.geometry("300x200")

lable = tk.lable(root, text="Hello GUI")
lable.pack()

root.mainloop()
