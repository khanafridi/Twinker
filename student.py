import tkinter as tk

class Std():
    def __init__(self, root):
        self.root = root
        self.root.title('Student Record')

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="Student Record Management System", bd=4, bg="blue", relief='raised', font=('Arial', 50, 'bold'))
        title.pack(side="top", fill="x")

        optframe = tk.Frame(self.root, bd=5, relief="ridge", bg=self.color(173,216,230))
        optframe.place(width=self.width/3, height=self.height-180, x=50, y=100)

        detframe = tk.Frame(self.root, bd=5, relief="ridge", bg=self.color(173,216,230))
        detframe.place(width=self.width/3, height=self.height-180, x=self.width/3, y=100)

        def color(self, r,g,b):
            return f"#{r:02x}{g:02x}{b:02x}"

root = tk.Tk()
obj = Std(root)
root.mainloop()