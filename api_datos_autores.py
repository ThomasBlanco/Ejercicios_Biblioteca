from Autores import Autor_modelo

class Api_lista_autores:
    def __init__(self, lista_autores=None):
        self.Api_lista_autores = lista_autores if lista_autores is not None else []
    
    # creo las responsabilidades de gestión de autores
    def guardar_autores(self, nuevo_autor):
        """Guarda un autor en la lista"""
        datos_nuevos = [nuevo_autor.get_nombre(), nuevo_autor.get_apellido(), 
        nuevo_autor.get_edad(), nuevo_autor.get_año(), nuevo_autor.get_pais()]
        self.Api_lista_autores.append(datos_nuevos)
        return True

    def extender_libros(self, autores):
        """Extiende la lista con múltiples autores"""
        for a in autores:
            datos_nuevos = [a.get_nombre(), a.get_apellido(), a.get_edad(), a.get_año(), a.get_pais()]
            self.Api_lista_autores.extend([datos_nuevos])
        return True

    def insertar_libros(self, indice, nuevo_autor):
        """Inserta un autor en una posición específica"""
        datos_nuevos = [nuevo_autor.get_nombre(), nuevo_autor.get_apellido(), 
        nuevo_autor.get_edad(), nuevo_autor.get_año(), nuevo_autor.get_pais()]
        self.Api_lista_autores.insert(indice, datos_nuevos)
        return True

    def remover_libros(self, nombre_autor):
        """Remueve un autor por nombre"""
        for item in self.Api_lista_autores:
            if item and item[0] == nombre_autor:
                self.Api_lista_autores.remove(item)
                return True
        return False

    def eliminar_libros(self, indice=-1):
        """Elimina un autor por índice"""
        if 0 <= indice < len(self.Api_lista_autores) or indice == -1:
            self.Api_lista_autores.pop(indice)
            return True
        return False

    def buscar_libros(self, nombre_autor):
        """Busca autores por nombre"""
        return [item for item in self.Api_lista_autores if item and item[0] == nombre_autor]

    def contar_libros(self, nombre_autor):
        """Cuenta autores con un nombre específico"""
        count = 0
        for item in self.Api_lista_autores:
            if item and item[0] == nombre_autor:
                count += 1
        return count

    def ordenar_libros(self, reverse=False):
        """Ordena autores alfabéticamente"""
        self.Api_lista_autores.sort(key=lambda autor: autor[0], reverse=reverse)
        return True

    def invertir_libros(self):
        """Invierte el orden de la lista"""
        self.Api_lista_autores.reverse()
        return True

    def mostrar_lista_autores(self):
        """Muestra todos los autores registrados"""
        if not self.Api_lista_autores:
            print("No hay autores registrados")
            return
        for i in range(len(self.Api_lista_autores)):
            nombre = self.Api_lista_autores[i][0]
            apellido = self.Api_lista_autores[i][1]
            edad = self.Api_lista_autores[i][2]
            año = self.Api_lista_autores[i][3]
            pais = self.Api_lista_autores[i][4]
            print(f"AUTOR #{i+1}: {nombre} {apellido} | Edad: {edad} | Nacimiento: {año} | País: {pais}")
    
    def contar_total_autores(self):
        """Retorna el total de autores en la lista"""
        count = len(self.Api_lista_autores)
        return count