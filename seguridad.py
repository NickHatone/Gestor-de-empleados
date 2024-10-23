class Seguridad:
    def __init__(self):
        self.usuarios = {}
        self.crear_administrador()

    def crear_administrador(self):
        self.usuarios['nick'] = '1234'
        print('Administrador predeterminado creado: nick')

    def autenticar_usuario(self, usuario, password):
        if usuario in self.usuarios and self.usuarios[usuario] == password:
            return True
        return False
