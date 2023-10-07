from tkinter import *
# from tkinter import ttk


root = Tk()
# root.config(bg='skyblue')
root.title('Simple Calculator')

e = Entry(root, width=45)
e.config(fg='#334155', borderwidth=3, bg='#f1f5f9', relief='raised')

e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

def button_add(num):

    if num == 'C':
        e.delete(0, END)
    elif num == '=':
        hitung(e.get())
    else:
        e.insert(END, num)
    
def hitung(mathStr: str):
    e.delete(0, END)
    e.insert(0, eval(mathStr))



button_1 = Button(root, text='1', height=4, width=8, command=lambda: button_add(1))
button_2 = Button(root, text='2', height=4, width=8, command=lambda: button_add(2))
button_3 = Button(root, text='3', height=4, width=8, command=lambda: button_add(3))
button_4 = Button(root, text='4', height=4, width=8, command=lambda: button_add(4))
button_5 = Button(root, text='5', height=4, width=8, command=lambda: button_add(5))
button_6 = Button(root, text='6', height=4, width=8, command=lambda: button_add(6))
button_7 = Button(root, text='7', height=4, width=8, command=lambda: button_add(7))
button_8 = Button(root, text='8', height=4, width=8, command=lambda: button_add(8))
button_9 = Button(root, text='9', height=4, width=8, command=lambda: button_add(9))
button_0 = Button(root, text='0', height=4, width=8, command=lambda: button_add(0))
button_plus = Button(root, text='+', height=4, width=8, command=lambda: button_add('+'))
button_minus = Button(root, text='-', height=4, width=8, command=lambda: button_add('-'))
button_kali = Button(root, text='x', height=4, width=8, command=lambda: button_add('*'))
button_bagi = Button(root, text='/', height=4, width=8, command=lambda: button_add('/'))


button_equals = Button(root, text='=', height=4, width=8, command=lambda: button_add('='))
button_clear = Button(root, text='C', height=4, width=8, command=lambda: button_add('C'))


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_kali.grid(row=3, column=3)
button_bagi.grid(row=4, column=3)

button_equals.grid(row=4, column=1)
button_clear.grid(row=4, column=2)



# button.pack()

root.mainloop()