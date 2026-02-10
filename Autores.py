class Autor_modelo:
    def __init__(self, dato_nombre, dato_apellido, dato_edad, dato_año, dato_pais):
        self.nombre = dato_nombre
        self.apellido = dato_apellido
        self.edad = dato_edad
        self.año = dato_año
        self.pais = dato_pais

    # getters
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_año(self):
        return self.año

    def get_pais(self):
        return self.pais

    # setters
    def set_nombre(self, dato_nombre):
        self.nombre = dato_nombre
        return True

    def set_apellido(self, dato_apellido):
        self.apellido = dato_apellido
        return True

    def set_edad(self, dato_edad):
        self.edad = dato_edad
        return True

    def set_año(self, dato_año):
        self.año = dato_año
        return True

    def set_pais(self, dato_pais):
        self.pais = dato_pais
        return True

    # responsabilidades
    def registrar_datos(self):
        return f"Autor {self.nombre} {self.apellido} registrado correctamente"

    def buscar_autor(self, dato_buscar):
        if dato_buscar.lower() in self.nombre.lower() or dato_buscar.lower() in self.apellido.lower():
            return True
        return False

    def dar_baja_autor(self):
        return f"El autor {self.nombre} {self.apellido} ha sido dado de baja"

    def ver_info(self):
        print(f"Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad} | Año: {self.año} | País: {self.pais}")