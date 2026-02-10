class base_datos_libro:
    
    def __init__(self):
        self.base_datos_libro = []

    #creo las responsabilidades de gestión de libros

    def guardar_libro(self, obj_libro):
        """Guarda un libro en la base de datos"""
        self.base_datos_libro.append(obj_libro)
        return True

    def extender_libros(self, Nueva_lista):
        """Extiende la lista con múltiples libros"""
        self.base_datos_libro.extend(Nueva_lista)
        return True

    def insertar_libro(self, pos_index, obj_libro):
        """Inserta un libro en una posición específica"""
        self.base_datos_libro.insert(pos_index, obj_libro)
        return True

    def remover_libros(self, obj_libro):
        """Remueve un libro específico"""
        self.base_datos_libro.remove(obj_libro)
        return True

    def eliminar_libros(self, pos_index):
        """Elimina un libro por índice"""
        self.base_datos_libro.pop(pos_index)
        return True

    def buscar_libros(self, Nombre_objeto):
        """Busca un libro y retorna su índice"""
        return self.base_datos_libro.index(Nombre_objeto)

    def contar_libros(self, valor):
        """Cuenta libros específicos"""
        return self.base_datos_libro.count(valor)

    def ordenar_libros(self):
        """Ordena libros por temática"""
        self.base_datos_libro.sort(reverse=True, key=lambda libro: libro.get_tematica())
        return True

    def invertir_libros(self):
        """Invierte el orden de la lista"""
        self.base_datos_libro.reverse()
        return True

    def mostrar_info(self):
        """Muestra información de todos los libros"""
        if not self.base_datos_libro:
            print("No hay libros registrados")
            return
        for i in range(len(self.base_datos_libro)):
            print(f"LIBRO #{i+1}:")
            self.base_datos_libro[i].ver_info()
    
    def contar_total_libros(self):
        """Retorna el total de libros en la base de datos"""
        return len(self.base_datos_libro)