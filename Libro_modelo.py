class Libro_modelo:
    def __init__(self, fecha, cant_hojas, tematica, genero):
        self.fecha = fecha
        self.cantidad_hojas = cant_hojas
        self.tematica = tematica
        self.genero = genero

    def get_cantidad_hojas(self):
        return self.cantidad_hojas

    def set_cantidad_hojas(self, dato):
        return self.cantidad_hojas

    def get_tematica(self):
        return self.tematica

    def get_fecha(self):
        return self.fecha
    
    def get_genero(self):
        return self.genero


    # hacer responsabilidades de la clase

    def registrar_cantidad_hojas(self):
        mensaje = "Se registraron en la base de datos"
        return mensaje
    
    def registrar_fecha_libro(self):
        mensaje = "Las fechas se registraron en la base de datos"
        return mensaje

    def mostrar_cantidad_hojas(self):
        mensaje = " El libro tiene la siguiente cantidad: "
        mensaje = mensaje + self.get_cantidad_hojas()
        return mensaje

    def registrar_tematica(self):
        # sql
        mensaje = "Tematica registrada"
        return mensaje

    def mostrar_tematica(self):
        # sql

        mensaje = self.get_tematica()
        return mensaje

    def ver_info_autor(self, obj_autor):
        obj_autor.ver_info()
    
    def ver_info_libro(self):
        return f"tematica libro: {self.tematica} - fecha libro: {self.fecha} - cantidad hojas: {self.cantidad_hojas} - genero: {self.genero}"