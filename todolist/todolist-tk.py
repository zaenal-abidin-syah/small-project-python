from tkinter import * 

class TodoList():
    
    def __init__(self):
        self.todolist = []
        self.row_tugas = 2
        self.count = 0
        self.delete = []
        self.root = Tk()
        self.root.title('Todo List')
        self.createFrame()
        self.root.mainloop()
    def isEmpty(self):
        return self.todolist == []
    def destroy(self, tugas, count):
        tugas.destroy() and self.delete[count].destroy()
    def add(self, item):
        if self.isEmpty():self.emptyTodo.destroy();
            
        count = self.count
        tugas = Label(self.root, text=item, anchor='center', justify='center')
        delete = Button(self.root, text='hapus', command=lambda tgs=tugas, cnt=count: self.destroy(tgs, cnt))
            

        tugas.grid(row=self.row_tugas, pady=5, padx=10, columnspan=4)
        delete.grid(row=self.row_tugas, column=4)

        self.delete.append([tugas, delete])
        print(self.delete)
        self.row_tugas += 2



    def createFrame(self):
        td_list = Label(self.root, text='Todo List', width=50).grid(row=0, pady=5, padx=10, columnspan=4)
        action = Label(self.root, text='Action', width=50).grid(row=0, column=5, pady=5, padx=10, columnspan=2)
        entry = Entry(self.root)
        entry.grid(row=2, column=5, pady=5, padx=10)
        
        button = Button(self.root, text='add', command=lambda: self.add(entry.get())).grid(row=2, column=6, pady=5, padx=10)

        if self.isEmpty():
            self.emptyTodo = Label(self.root, text='Todo List Kosong', anchor='center', justify='center')
            self.emptyTodo.grid(row=2, pady=5, padx=10, columnspan=4)
            
    # def 
TodoList()