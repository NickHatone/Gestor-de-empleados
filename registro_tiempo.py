class RegistroTiempo:
    def __init__(self, id, fecha, horas_trabajadas, descripcion):
        self.id = id
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion

    def registrar_horas(self, empleado, proyecto):
        empleado.registrar_horas_trabajadas(proyecto, self.horas_trabajadas)
