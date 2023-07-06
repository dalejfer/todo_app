import tkinter as tk
import ui

def main():
    root = tk.Tk()
    root.title("TODO")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    ui.Principal(root).grid(sticky=tk.NSEW)
    root.mainloop()

if __name__ == "__main__":
    main()