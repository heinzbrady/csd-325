## Brady Heinz 3/8/26 10.2 Assignment

import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("Heinz-ToDo")
        self.geometry("300x400")

        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)

        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self,
            orient="vertical",
            command=self.tasks_canvas.yview
        )

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.colour_schemes = [
            {"bg": "#0414F0", "fg": "white"}, 
            {"bg": "#FF7B00", "fg": "black"}, 
        ]

        self.instruction_label = tk.Label(
            self.tasks_frame,
            text="*** Added --- * Right Click Item to Delete*",
            pady=10
        )
        self.instruction_label.bind("<Button-3>", self.remove_task)
        self.tasks.append(self.instruction_label)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.recolour_tasks()

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if task_text:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            new_task.bind("<Button-3>", self.remove_task)  
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)

            self.recolour_tasks()

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            if task in self.tasks:
                self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        if self.tasks:
            self.tasks[0].configure(bg="#2431E6", fg="white")  

        for index, task in enumerate(self.tasks[1:], start=0):
            scheme = self.colour_schemes[(index + 1) % 2]  
            task.configure(bg=scheme["bg"], fg=scheme["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        self.tasks_canvas.itemconfig(self.canvas_frame, width=event.width)

    def mouse_scroll(self, event):
        self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()