class Departamento:
    def __init__(self, departamento_ID, nombre, gerente=None):
        self.departamento_ID = departamento_ID
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def asignar_empleado(self, empleado):
        self.empleados.append(empleado)
        empleado.asignar_departamento(self)
        print(f'Empleado {empleado.nombre} ha sido asignado al departamento {self.nombre}')

    def asignar_gerente(self, empleado):
        self.gerente = empleado
        print(f'{empleado.nombre} es ahora el gerente del departamento {self.nombre}')

    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)
        empleado.departamento = None
        print(f'Empleado {empleado.nombre} ha sido eliminado del departamento {self.nombre}')
