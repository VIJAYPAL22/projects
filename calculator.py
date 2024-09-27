import tkinter as tk 
from tkinter import messagebox


def add():
   result.set(float(entry1.get())+float(entry2.get()))
def sub():
    result.set(float(entry1.get())-float(entry2.get()))   
def multi():
    result.set(float*(entry1.get())*float(entry2.get()))
def divide():
    try:
        result.set(float(entry1.get())/float(entry2.get()))
    except ZeroDivisionError:
        messagebox.showerror("Error","Cannot divide by zero!")
        
root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root,text="Entre first number:").grid(row=0,column=0)
entry1=tk.Entry(root)
entry1.grid(row=0,column=1)

tk.Label(root,text="Entre second number:").grid(row=1,column=0)
entry2=tk.Entry(root)
entry2.grid(row=1,column=1)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=2,column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=2,column=1)

tk.Button(root, text="Add",command=add).grid(row=3,column=0)

tk.Button(root, text="Subtract",command=sub).grid(row=3,column=1)

tk.Button(root, text="Multiply",command=multi).grid(row=4,column=0)

tk.Button(root, text="Divide",command=divide).grid(row=4,column=1)

root.mainloop()