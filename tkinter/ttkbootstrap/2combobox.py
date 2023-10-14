from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import os
import sys

def clicker():
  my_label.config(text=f"Kamu menekan hari {my_combo.get()}")

def click_bind(e):
  my_label.config(text=f"Kamu menekan hari {my_combo.get()}")

root = tb.Window(themename='superhero')
root.geometry('800x500')

root.title('Ttk Bootstrap')
icon = PhotoImage('./icon.png')

root.iconphoto(False, icon)

# combo box
my_label = tb.Label(root, text='Hello World', font=("helvetica", 14))

my_label.pack(pady=30)
days = [
  "Senin",
  "Selasa",
  "Rabu",
  "Kamis",
  "Jumat",
  "Sabtu",
  "Minggu"
]
my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack()
my_combo.current(0)
my_button = tb.Button(root, bootstyle="danger", text='Klik', command=clicker)
my_button.pack()
my_combo.bind("<<ComboboxSelected>>", click_bind)
root.mainloop()
