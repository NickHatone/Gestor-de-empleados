class Empleado:
    def __init__(self, empleadoID, nombre, direccion, telefono, email, fecha_inicio, salario, administrador=False):
        self.empleadoID = empleadoID
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.administrador = administrador
        self.departamento = None
        self.proyectos = []
        self.horas_trabajadas = {}

    def asignar_departamento(self, departamento):
        self.departamento = departamento
        print(f'{self.nombre} ha sido asignado al departamento {departamento.nombre}')

    def registrar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        print(f'{self.nombre} ha sido asignado al proyecto {proyecto.nombre}')

    def registrar_horas_trabajadas(self, proyecto, horas):
        if proyecto in self.proyectos:
            if proyecto.nombre not in self.horas_trabajadas:
                self.horas_trabajadas[proyecto.nombre] = 0
            self.horas_trabajadas[proyecto.nombre] += horas
            print(f'Se registraron {horas} horas en el proyecto {proyecto.nombre} para {self.nombre}')
        else:
            print(f'{self.nombre} no está asignado al proyecto {proyecto.nombre}')

    def mostrar_horas_trabajadas(self):
        for proyecto, horas in self.horas_trabajadas.items():
            print(f'{self.nombre} ha trabajado {horas} horas en el proyecto {proyecto}')
