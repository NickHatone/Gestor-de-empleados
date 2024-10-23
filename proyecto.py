class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.empleados = []

    def asignar_empleado(self, empleado):
        self.empleados.append(empleado)
        empleado.registrar_proyecto(self)
        print(f'{empleado.nombre} ha sido asignado al proyecto {self.nombre}')

    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)
        print(f'{empleado.nombre} ha sido eliminado del proyecto {self.nombre}')
