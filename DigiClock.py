import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digi-Clock")

def time():
    string=strftime("%H:%M:%S\n%D")
    label.config(text=string)
    label.after(1000,time)

label=tk.Label(root,font=("Calibri",100,"bold"),background="brown",foreground="wheat")
label.pack(anchor="center")

time()

root.mainloop()