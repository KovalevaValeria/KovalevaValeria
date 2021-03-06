import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#87CEEB', bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#87CEEB', bd=0,
                                    compound=tk.TOP)

        btn_open_dialog.pack(side=tk.LEFT)

        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#87CEEB', bd=0, compound=tk.TOP,
                                    command=self.open_update_dialog)

        btn_edit_dialog.pack(side=tk.LEFT)

        btn_delete = tk.Button(toolbar, text='Удалить', bg='#87CEEB', bd=0, compound=tk.TOP,
                                    command=self.delete_records)

        btn_delete.pack(side=tk.LEFT)


        self.tree = ttk.Treeview(self, columns=('N', 'name', 'EGE', 'level', 'code', 'contact'),
                                 height=15, show='headings')

        self.tree.column('N', width=40, anchor=tk.CENTER)
        self.tree.column('name', width=250, anchor=tk.CENTER)
        self.tree.column('EGE', width=160, anchor=tk.CENTER)
        self.tree.column('level', width=140, anchor=tk.CENTER)
        self.tree.column('code', width=350, anchor=tk.CENTER)
        self.tree.column('contact', width=160, anchor=tk.CENTER)

        self.tree.heading('N', text='№')
        self.tree.heading('name', text='ФИО')
        self.tree.heading('EGE', text='Результаты экзаменов')
        self.tree.heading('level', text='Ступень образования')
        self.tree.heading('code', text='Код направления')
        self.tree.heading('contact', text='Контакты')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, name, EGE, level, code, contact):
        self.db.insert_data(name, EGE, level, code, contact)
        self.view_records()

    def update_record(self, name, EGE, level, code, contact):
        self.db.c.execute('''UPDATE record SET name=?, EGE=?, level=?, code=?, contact=? WHERE n=?''',
                          (name, EGE, level, code, contact, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM record ''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM record  WHERE n=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить данные')
        self.geometry('400x230+500+400')
        self.resizable(False, False)


        label_name = tk.Label(self, text='ФИО')
        label_name.place(x=50, y=20)
        label_EGE = tk.Label(self, text='Результаты экзаменов')
        label_EGE.place(x=50, y=50)
        label_level = tk.Label(self, text='Ступень образования')
        label_level.place(x=50, y=80)
        label_code = tk.Label(self, text='Код направления')
        label_code.place(x=50, y=110)
        label_contact = tk.Label(self, text='Контакты')
        label_contact.place(x=50, y=140)


        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=20)

        self.entry_EGE = ttk.Entry(self)
        self.entry_EGE.place(x=200, y=50)

        self.entry_level = ttk.Entry(self)
        self.entry_level.place(x=200, y=80)

        self.entry_code = ttk.Entry(self)
        self.entry_code.place(x=200, y=110)

        self.entry_contact = ttk.Entry(self)
        self.entry_contact.place(x=200, y=140)


        self.combobox1 = ttk.Combobox(self, values=['Бакалавриат', 'Специалитет', 'Магистратура', 'Аспирантура'])
        self.combobox1.current(0)
        self.combobox1.place(x=200, y=80)

        self.combobox2 = ttk.Combobox(self, values=['03.03.01 — «Прикладные математика и физика»',
                                                   '11.04.04 — «Электроника и наноэлектроника»',
                                                   '03.04.02 — «Физика»',
                                                   '03.04.01 — «Прикладные математика и физика»',
                                                   '03.06.01 — «Физика полупроводников»',
                                                   '03.06.01 — «Физика конденсированного состояния»',
                                                   '06.06.01 — «Биологические науки»',
                                                   '03.01.06 — «Биотехнологии, в т.ч. бионанотехнологии»',
                                                   '03.06.01 — «Физика полупроводников»',
                                                   '01.06.01 — «Математика и механика»',
                                                   '09.06.01 — «Информатика и вычислительная техника»'
                                                   ])
        self.combobox2.current(0)
        self.combobox2.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_name.get(),
                                                                       self.entry_EGE.get(),
                                                                       self.combobox1.get(),
                                                                       self.combobox2.get(),
                                                                       self.entry_contact.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_name.get(),
                                                                          self.entry_EGE.get(),
                                                                          self.combobox1.get(),
                                                                          self.combobox2.get(),
                                                                          self.entry_contact.get()))
        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM record  WHERE n=?''', (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.c.fetchall()
        self.entry_name.insert(0, row[1])
        if row[2] != 'Экзамены':
            self.combobox1.current(1)
        self.entry_level.insert(0, row[3])

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('record .db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS record  (n integer primary key, name text, EGE integer, level text, 
            code integer, contact text)''')
        self.conn.commit()

    def insert_data(self, name, EGE, level, code, contact):
        self.c.execute('''INSERT INTO record (name, EGE, level, code, contact) VALUES (?, ? , ?, ? , ?)''',
                       (name, EGE, level, code, contact))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('Students database')
    root.geometry('1130x400+300+200')
    root.resizable(False, False)
    root.mainloop()
