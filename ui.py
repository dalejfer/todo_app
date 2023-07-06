import tkinter as tk
from tkinter import ttk, messagebox


class Principal(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.parent = parent

        self.columnconfigure(0, weight=1)   # descripcion
        self.columnconfigure(1, weight=1)   # check
        self.columnconfigure(2, weight=1)   # eliminar
        self.columnconfigure(3, weight=0)   # scrollbar
        self.rowconfigure(0, weight=1)  # titulo
        self.rowconfigure(1, weight=1)  # tasks
        self.rowconfigure(2, weight=1)  # botones

        ttk.Label(self, text="TODO app").grid(row=0, column=0, columnspan=3)
        ttk.Frame(self).grid(row=1, column=0)
        ttk.Button(self, text="Salir").grid(row=2, column=2, columnspan=2)
