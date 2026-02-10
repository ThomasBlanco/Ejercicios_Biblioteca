class Libro_modelo:
    def __init__(self, fecha, cant_hojas, tematica, genero):
        self.fecha = fecha
        self.cantidad_hojas = cant_hojas
        self.tematica = tematica
        self.genero = genero

    # getters
    def get_cantidad_hojas(self):
        return self.cantidad_hojas

    def get_tematica(self):
        return self.tematica

    def get_fecha(self):
        return self.fecha
    
    def get_genero(self):
        return self.genero

    # setters
    def set_cantidad_hojas(self, dato):
        self.cantidad_hojas = dato
        return True

    def set_tematica(self, dato):
        self.tematica = dato
        return True

    def set_fecha(self, dato):
        self.fecha = dato
        return True
    
    def set_genero(self, dato):
        self.genero = dato
        return True

    # responsabilidades
    def registrar_cantidad_hojas(self):
        return f"Libro {self.tematica} con {self.cantidad_hojas} hojas registrado"
    
    def registrar_fecha_libro(self):
        return f"Fecha de publicación {self.fecha} registrada"

    def mostrar_cantidad_hojas(self):
        return f"El libro tiene {self.cantidad_hojas} hojas"

    def registrar_tematica(self):
        return f"Temática '{self.tematica}' registrada"

    def mostrar_tematica(self):
        return f"Temática: {self.tematica}"

    def ver_info_autor(self, obj_autor):
        obj_autor.ver_info()
    
    def ver_info(self):
        print(f"Temática: {self.tematica} | Fecha: {self.fecha} | Hojas: {self.cantidad_hojas} | Género: {self.genero}")
    
    def ver_info_libro(self):
        return f"Temática: {self.tematica} | Fecha: {self.fecha} | Hojas: {self.cantidad_hojas} | Género: {self.genero}"