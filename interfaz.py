import tkinter as tk
from tkinter import messagebox
from bd import BaseDeDatos
from seguridad import Seguridad
from empleado import Empleado
from proyecto import Proyecto
from departamento import Departamento

class Aplicacion:
    def __init__(self, master):
        self.master = master
        master.title("Gestión de Empleados")

        self.base_de_datos = BaseDeDatos('empleados.db')
        self.seguridad = Seguridad()  # Crear instancia de Seguridad

        # Crear elementos de la interfaz
        self.label_usuario = tk.Label(master, text="Usuario:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(master)
        self.entry_usuario.pack()

        self.label_password = tk.Label(master, text="Contraseña:")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.boton_login = tk.Button(master, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_login.pack()

        # Frame para gestionar empleados
        self.empleado_frame = tk.Frame(master)
        self.empleado_frame.pack()

        # Entradas para agregar empleado
        self.nombre_label = tk.Label(self.empleado_frame, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.empleado_frame)
        self.nombre_entry.pack()

        self.direccion_label = tk.Label(self.empleado_frame, text="Dirección:")
        self.direccion_label.pack()
        self.direccion_entry = tk.Entry(self.empleado_frame)
        self.direccion_entry.pack()

        self.telefono_label = tk.Label(self.empleado_frame, text="Teléfono:")
        self.telefono_label.pack()
        self.telefono_entry = tk.Entry(self.empleado_frame)
        self.telefono_entry.pack()

        self.email_label = tk.Label(self.empleado_frame, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.empleado_frame)
        self.email_entry.pack()

        self.fecha_inicio_label = tk.Label(self.empleado_frame, text="Fecha de Inicio:")
        self.fecha_inicio_label.pack()
        self.fecha_inicio_entry = tk.Entry(self.empleado_frame)
        self.fecha_inicio_entry.pack()

        self.salario_label = tk.Label(self.empleado_frame, text="Salario:")
        self.salario_label.pack()
        self.salario_entry = tk.Entry(self.empleado_frame)
        self.salario_entry.pack()

        self.admin_var = tk.BooleanVar()
        self.admin_check = tk.Checkbutton(self.empleado_frame, text="Es Administrador", variable=self.admin_var)
        self.admin_check.pack()

        self.agregar_button = tk.Button(self.empleado_frame, text="Agregar Empleado", command=self.agregar_empleado)
        self.agregar_button.pack()

        # Frame para gestionar proyectos
        self.proyecto_frame = tk.Frame(master)
        self.proyecto_frame.pack()

        self.proyecto_nombre_label = tk.Label(self.proyecto_frame, text="Nombre del Proyecto:")
        self.proyecto_nombre_label.pack()
        self.proyecto_nombre_entry = tk.Entry(self.proyecto_frame)
        self.proyecto_nombre_entry.pack()

        self.proyecto_descripcion_label = tk.Label(self.proyecto_frame, text="Descripción:")
        self.proyecto_descripcion_label.pack()
        self.proyecto_descripcion_entry = tk.Entry(self.proyecto_frame)
        self.proyecto_descripcion_entry.pack()

        self.proyecto_fecha_label = tk.Label(self.proyecto_frame, text="Fecha de Inicio:")
        self.proyecto_fecha_label.pack()
        self.proyecto_fecha_entry = tk.Entry(self.proyecto_frame)
        self.proyecto_fecha_entry.pack()

        self.agregar_proyecto_button = tk.Button(self.proyecto_frame, text="Agregar Proyecto", command=self.agregar_proyecto)
        self.agregar_proyecto_button.pack()

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        if self.seguridad.autenticar_usuario(usuario, password):
            messagebox.showinfo("Éxito", "Sesión iniciada correctamente.")
            # Mostrar secciones de gestión
            self.empleado_frame.pack()
            self.proyecto_frame.pack()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def agregar_empleado(self):
        nombre = self.nombre_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()
        fecha_inicio = self.fecha_inicio_entry.get()
        salario = float(self.salario_entry.get())
        administrador = self.admin_var.get()

        nuevo_empleado = Empleado(len(self.base_de_datos.obtener_empleados()) + 1, nombre, direccion, telefono, email, fecha_inicio, salario, administrador)
        self.base_de_datos.agregar_empleado(nuevo_empleado)
        messagebox.showinfo("Éxito", f"Empleado {nombre} agregado.")

    def agregar_proyecto(self):
        nombre = self.proyecto_nombre_entry.get()
        descripcion = self.proyecto_descripcion_entry.get()
        fecha_inicio = self.proyecto_fecha_entry.get()

        nuevo_proyecto = Proyecto(nombre, descripcion, fecha_inicio)
        # Aquí podrías agregar código para almacenar el proyecto en la base de datos si fuera necesario
        messagebox.showinfo("Éxito", f"Proyecto {nombre} agregado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
