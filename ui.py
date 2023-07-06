import tkinter as tk
from tkinter import ttk, messagebox
import datos

class Principal(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.parent = parent

        self.columnconfigure(0, weight=1)   # descripcion
        self.columnconfigure(1, weight=1)   # check
        self.columnconfigure(2, weight=1)   # check
        self.columnconfigure(3, weight=0)   # scrollbar

        # self.columnconfigure(3, weight=0)   # scrollbar
        self.rowconfigure(0, weight=1)  # titulo
        self.rowconfigure(1, weight=1)  # tipos
        self.rowconfigure(2, weight=1)  # tareas
        self.rowconfigure(3, weight=1)  # acciones
        self.rowconfigure(4, weight=1)  # salir

        ttk.Label(self, text="TODO app").grid(row=0, column=0, columnspan=4)
        self.set_botonera1()
        self.set_botonera2()
        self.set_tabla()
        ttk.Button(self, text="Salir",
                   command=self.salir).grid(row=4, column=1, columnspan=2, sticky=tk.E)

        self.cargar_tabla()
    
    def cargar_tabla(self, tipo="all"):
        """tipo es 'all', 'done' o 'pending' """
        self.vaciar_tabla()
        registros = datos.get_tareas(tipo)
        for id_tarea, tarea, completada in registros:
            self.tabla.insert('', tk.END, values=(tarea, "Si" if completada else "No"))
        
    def vaciar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

    def set_tabla(self):
        """crear la tabla"""
        columnas = ('tarea', 'completada')
        self.tabla = ttk.Treeview(self, columns=columnas,show='headings',
                                  selectmode="browse") # sin multi-seleccion
        self.tabla.grid(row=2, column=0, columnspan=3, sticky=(tk.NSEW))
        scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        scroll.grid(row=2, column=3, sticky=tk.NS)
        self.tabla.configure(yscroll=scroll.set)
        self.tabla.heading('tarea', text='Descripcion')
        self.tabla.heading('completada', text='Completada')

    def set_botonera1(self):
        """crear la botonera para mostrar tareas en la tabla"""
        botonera1 = ttk.Frame(self)
        botonera1.grid(row=1, column=0, columnspan=4)
        botonera1.columnconfigure(0, weight=1)
        botonera1.columnconfigure(1, weight=1)
        botonera1.columnconfigure(2, weight=1)
        ttk.Button(botonera1, text="Mostrar solo pendientes",
                   command=lambda:self.cargar_tabla("pending")).grid(row=0, column=0)
        ttk.Button(botonera1, text="Mostrar solo completadas",
                   command=lambda:self.cargar_tabla("done")).grid(row=0, column=1)
        ttk.Button(botonera1, text="Mostrar todo",
                   command=lambda:self.cargar_tabla("all")).grid(row=0, column=2)
    
    def set_botonera2(self):
        """crear botonera de abm de tareas"""
        botonera2 = ttk.Frame(self)
        botonera2.grid(row=3, column=0, columnspan=4)
        botonera2.columnconfigure(0, weight=1)
        botonera2.columnconfigure(1, weight=1)
        botonera2.columnconfigure(2, weight=1)
        ttk.Button(botonera2, text="Completar").grid(row=0, column=0)
        ttk.Button(botonera2, text="Editar").grid(row=0, column=1)
        ttk.Button(botonera2, text="Eliminar").grid(row=0, column=2)

    def agregar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion[0])
            id_tarea = item['values'][0]
            
        else:
            messagebox.showinfo(message="Debe seleccionar una tarea primero")

    def completar(self):
        pass

    def eliminar(self):
        pass

    def salir(self):
        self.parent.destroy()