import segno
from tkinter import *
from os import path, remove
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x400')
root.title('QR Code Generator')
e = Entry()
e.pack(side='top', fill='both', padx=5, pady=10)
e.focus()
def generate(first):
    if first:
        first = False
    else:
        print('canvas destroyer')
        label.destroy()

    word = e.get()
    
    if path.isfile('./main.png'):
        print('remove main.png')
        remove('./main.png')

        
    
        
    segno.make(word).save('main.png', scale=10)
    print('create file main.png')
    img = ImageTk.PhotoImage(Image.open('main.png'))
    label = Label(image=img)
    label.image = img
    label.pack()
    
    
    


first = True
b = Button(text='Generate', command=lambda : generate(first))
b.pack(side='top', pady=10)
# canvas = Canvas(width=400, height=400)
# canvas.pack(side='top', fill='both')


root.mainloop()
