from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import os
import sys

counter = 0
def changer():
  global counter
  counter += 1
  if counter % 2 == 0:
    label.config(text='Hello World')
  else:
    label.config(text='Goodbye World')

def checker():
  if var1.get() == 1:
    label.config(text='Checked')
  else:
    label.config(text='Unchecked')


root = tb.Window(themename='superhero')
root.geometry('800x500')

root.title('Ttk Bootstrap')
icon = PhotoImage('./icon.png')

root.iconphoto(False, icon)

# 1
label1 = tb.Label(text='Hello world', font=('helvetica', 24), bootstyle='danger')
label1.pack(pady=50)
button = tb.Button(text='Click Me', bootstyle='primary, outline', command=changer)
button.pack(padx=20)


# 2
label2 = tb.Label(text='click the button', font=('helvetica', 24), bootstyle='danger')
label2.pack(pady=50)
var1 = IntVar()
check = tb.Checkbutton(
  text='click me', 
  variable=var1, 
  bootstyle='primary', 
  onvalue=1,
  offvalue=0,
  command=checker)

var2 = IntVar()
check2 = tb.Checkbutton(
  text='Tools Button', 
  variable=var2, 
  bootstyle='primary, toolbutton', 
  onvalue=1,
  offvalue=0,
  command=checker)

# 3
var3 = IntVar()
check3 = tb.Checkbutton(
  text='Tools Button outline', 
  variable=var3, 
  bootstyle='danger, toolbutton, outline', 
  onvalue=1,
  offvalue=0,
  command=checker)

# 4
var4 = IntVar()
check4 = tb.Checkbutton(
  text='rounded toggle', 
  variable=var4, 
  bootstyle='success, round-toggle', 
  onvalue=1,
  offvalue=0,
  command=checker)

# 5
var5 = IntVar()
check5 = tb.Checkbutton(
  text='square toggle', 
  variable=var5, 
  bootstyle='success, square-toggle', 
  onvalue=1,
  offvalue=0,
  command=checker)

check.pack(pady=(30, 10))
check2.pack(pady=(30, 10))
check3.pack(pady=(30, 10))
check4.pack(pady=(30, 10))
check5.pack(pady=(30, 10))

root.mainloop()
