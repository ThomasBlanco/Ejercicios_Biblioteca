class base_datos_libro:
    
    def __init__(self):
        self.base_datos_libro = []

    def guardar_libro(self, obj_libro):
        self.base_datos_libro.append(obj_libro)

    def extender_libros(self, Nueva_lista):
        self.base_datos_libro.extend(Nueva_lista)

    def insertar_libro(self, pos_index, obj_libro):
        self.base_datos_libro.insert(pos_index, obj_libro)

    def remover_libros(self, obj_libro):
        self.base_datos_libro.remove(obj_libro)

    def eliminar_libros(self, pos_index):
        self.base_datos_libro.pop(pos_index)

    def buscar_libros(self, Nombre_objeto):
        return self.base_datos_libro.index(Nombre_objeto)

    def contar_libros(self, valor):
        return self.base_datos_libro.count(valor)

    def ordenar_libros(self):
        self.base_datos_libro.sort(reverse=True, key=lambda libro: libro.get_tematica())

    def invertir_libros(self):
        self.base_datos_libro.reverse()

    def mostrar_info(self):
        for i in range(len(self.base_datos_libro)):
            tematica = self.base_datos_libro[i].get_tematica()
            fecha = self.base_datos_libro[i].get_fecha()
            cant_hojas = self.base_datos_libro[i].get_cantidad_hojas()
            genero = self.base_datos_libro[i].get_genero()
            print(f"tematica libro: {tematica} - fecha libro: {fecha} - cantidad hojas: {cant_hojas} - genero: {genero}")