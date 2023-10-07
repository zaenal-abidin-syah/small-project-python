from tkinter import *
from tkinter import ttk

root = Tk()
# # # creating label widget
# # mylabel1 = Label(root, text="hello world!", padx='10px', pady='4px').grid(row=0, column=0)
# # mylabel2 = Label(root, text="nama saya zzz").grid(row=1, column=1)
# # mylabel3 = Label(root, text="text lain").grid(row=3, column=5)


# myButton = Button(root, text='Click Me!', padx=50)
# myButton.pack()




# # saving it in to screen

# root.mainloop()

def start():
    b.configure(text='Stop', command=stop)
    l['text'] = 'Working...'
    global interrupt; interrupt = False
    root.after(1, step)
    
def stop():
    global interrupt; interrupt = True
    
def step(count=0):
    p['value'] = count
    if interrupt:
        result(None)
        return
    # root.after(100)  # next step in our operation; don't take too long!
    if count == 20:  # done!
        result(42)
        return
    root.after(1, lambda: step(count+1))
    
def result(answer):
    p['value'] = 0
    b.configure(text='Start!', command=start)
    l['text'] = "Answer: " + str(answer) if answer else "No Answer"
    
f = Frame(root); f.grid()
b = Button(f, text="Start!", command=start); b.grid(column=1, row=0, padx=5, pady=5)
l = Label(f, text="No Answer"); l.grid(column=0, row=0, padx=5, pady=5)
p = ttk.Progressbar(f, orient="horizontal", mode="determinate", maximum=20); 
p.grid(column=0, row=1, padx=5, pady=5)

root.mainloop()