import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.second_window_button = tk.Button(root, text="Go to Second Window", command=self.open_second_window)
        self.second_window_button.pack()

    def submit(self):
        text = self.entry.get()
        if text:
            messagebox.showinfo("Info", f"You entered: {text}")
        else:
            messagebox.showwarning("Warning", "Entry cannot be empty!")

    def open_second_window(self):
        text = self.entry.get()
        if text:
            second_window = tk.Toplevel(self.root)
            second_window.title("Second Window")
            label = tk.Label(second_window, text=text)
            label.pack()
        else:
            messagebox.showwarning("Warning", "Entry cannot be empty!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
