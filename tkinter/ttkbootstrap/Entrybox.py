from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')
root.geometry('800x500')

root.title('Ttk Bootstrap')
icon = PhotoImage('./icon.png')

root.iconphoto(False, icon)



root.mainloop()