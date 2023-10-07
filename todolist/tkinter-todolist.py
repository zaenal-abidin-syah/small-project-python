import tkinter
from tkinter import ttk
root = tkinter.Tk()
root.geometry('600x600')
root.title('Todolist Sederhana')
root.config(bg='#ede9fe')

frame =ttk.Frame()
l1 = tkinter.Label(frame, text='from tkinter')
l2 = ttk.Label(frame, text='from ttk')
# frame.grid()
# frame.configure(fg='blue')
frame.pack()
l1.pack()
l2.pack()

root.mainloop()