import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("665x400+550+250")
        self.root.resizable(0, 0)
        self.root.configure(bg="#FFE4E1")

        self.tasks = []

        self.functions_frame = tk.Frame(root, bg="#87CEEB")
        self.functions_frame.pack(side="top", expand=True, fill="both")

        self.task_label = tk.Label(
            self.functions_frame,
            text="Add a Task:",
            font=("Arial", "14", "bold"),
            bg="#87CEEB",
            fg="#800000"
        )
        self.task_label.place(x=20, y=30)

        self.task_field = tk.Entry(
            self.functions_frame,
            font=("Arial", "14"),
            width=42,
            fg="black",
            bg="#FFFACD",
        )
        self.task_field.place(x=140, y=30)

        self.add_button = tk.Button(
            self.functions_frame,
            text="Add Task",
            width=20,
            bg='#CD853F',
            font=("Arial", "12", "bold"),
            command=self.add_task,
        )
        self.del_button = tk.Button(
            self.functions_frame,
            text="Remove Task",
            width=20,
            bg='#CD853F',
            font=("Arial", "12", "bold"),
            command=self.remove_task,
        )
        self.del_all_button = tk.Button(
            self.functions_frame,
            text="Delete All",
            width=20,
            font=("Arial", "12", "bold"),
            bg='#CD853F',
            command=self.delete_all_tasks
        )

        self.exit_button = tk.Button(
            self.functions_frame,
            text="Close",
            width=52,
            bg='#CD853F',
            font=("Arial", "12", "bold"),
            command=self.close
        )
        self.add_button.place(x=40, y=100)
        self.del_button.place(x=260, y=100)
        self.del_all_button.place(x=470, y=100)
        self.exit_button.place(x=65, y=330)

        self.task_listbox = tk.Listbox(
            self.functions_frame,
            width=70,
            height=9,
            font=("Arial", "12"),
            selectmode='SINGLE',
            bg="#FFFACD",
            fg="black",
            selectbackground="#CD853F",
            selectforeground="black"
        )
        self.task_listbox.place(x=20, y=140)

        root.mainloop()

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def remove_task(self):
        try:
            the_value = self.task_listbox.get(self.task_listbox.curselection())
            if the_value in self.tasks:
                self.tasks.remove(the_value)
                self.list_update()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            while(len(self.tasks) != 0):
                self.tasks.pop()
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        self.root.destroy()

if __name__ == "__main__":
    guiWindow = tk.Tk()
    app = ToDoApp(guiWindow)
