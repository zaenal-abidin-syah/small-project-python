from tkinter import *
from tkinter import ttk
# from ttkthemes import ThemedTk

# window
window = Tk()

# style
style = ttk.Style()
style.configure('Button1.TButton', background='blue', foreground='red')

style.configure('Button2.TButton', background='red', foreground='blue')



frame1 = ttk.Frame()
frame2 = ttk.Frame()

button1 = ttk.Button(frame1,text='button1', padding=5, style='Button1.TButton')
button2 = ttk.Button(frame2,text='button2', padding=5, style='Button2.TButton')
button1.pack()
button2.pack()

frame1.pack(side='left')
frame2.pack(side='right')


window.mainloop()