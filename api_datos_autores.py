from Autores import Autor_modelo
class Api_lista_autores:
    def __init__(self, lista_autores, nuevo_autor, indice, nombre_autor):
        self.Api_lista_autores = lista_autores if lista_autores is not None else []
        self.nuevo_autor = nuevo_autor
        self.indice = indice
        self.nombre_autor = nombre_autor
    
    def guardar_autores(self, nuevo_autor):
        datos_nuevos = [nuevo_autor.get_nombre(), nuevo_autor.get_apellido(), nuevo_autor.get_edad(), nuevo_autor.get_año(), nuevo_autor.get_pais()]
        self.Api_lista_autores.append(datos_nuevos)

    def extender_libros(self, autores):
        for a in autores:
            self.Api_lista_autores.extend([[a.get_nombre(), a.get_fecha()]])

    def insertar_libros(self, indice, nuevo_autor):
        datos_nuevos = [nuevo_autor.get_nombre(), nuevo_autor.get_fecha()]
        self.Api_lista_autores.insert(indice, datos_nuevos)

    def remover_libros(self, nombre_autor):
        for item in self.Api_lista_autores:
            if item and item[0] == nombre_autor:
                self.Api_lista_autores.remove(item)
                return
        raise ValueError(f"Autor con nombre '{nombre_autor}' no encontrado")

    def eliminar_libros(self, indice=-1):
        return self.Api_lista_autores.pop(indice)

    def buscar_libros(self, nombre_autor):
        return [item for item in self.Api_lista_autores if item and item[0] == nombre_autor]

    def contar_libros(self, nombre_autor):
        count = 0
        for item in self.Api_lista_autores:
            if item and item[0] == nombre_autor:
                count += 1
        return count

    def ordenar_libros(self, reverse=False):
        self.Api_lista_autores.sort(key=lambda autor: autor[0], reverse=reverse)

    def invertir_libros(self):
        self.Api_lista_autores.reverse()

    def mostrar_lista_autores(self):
        if not self.Api_lista_autores:
            print("No hay autores registrados")
            return
        for i in range(len(self.Api_lista_autores)):
            nombre = self.Api_lista_autores[i][0]
            apellido = self.Api_lista_autores[i][1]
            edad = self.Api_lista_autores[i][2]
            año = self.Api_lista_autores[i][3]
            pais = self.Api_lista_autores[i][4]
            print(f"AUTOR #{i+1}: nombre: {nombre} | apellido: {apellido} | edad: {edad} | nacimiento: {año} | país: {pais}")