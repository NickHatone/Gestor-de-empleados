import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_db):
        self.connection = sqlite3.connect(nombre_db)
        self.cursor = self.connection.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        # Aquí deberías crear las tablas para empleados, departamentos, proyectos y registros de tiempo
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_inicio TEXT,
            salario REAL,
            administrador INTEGER
        )''')
        self.connection.commit()

    def agregar_empleado(self, empleado):
        self.cursor.execute('''INSERT INTO empleados (nombre, direccion, telefono, email, fecha_inicio, salario, administrador)
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', (empleado.nombre, empleado.direccion, empleado.telefono, empleado.email, empleado.fecha_inicio, empleado.salario, empleado.administrador))
        self.connection.commit()

    def obtener_empleados(self):
        self.cursor.execute('SELECT * FROM empleados')
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.connection.close()
