class Api_lista_autores:
    def __init__(self):
        self.Api_lista_autores= []
    def guardar_autores(self, nuevo_autor):
        datos_nuevos = [nuevo_autor.get_nombre(), nuevo_autor.get_fecha()]
        self.Api_lista_autores.append(datos_nuevos)


    def extender_autores(self, nuevos_autores):
        for autor in nuevos_autores:
            datos_nuevos = [autor.get_nombre(), autor.get_fecha()]
            self.Api_lista_autores.append(datos_nuevos)
        

    def insertar_autores(self, indice, nuevo_autor):
        datos_nuevos = [nuevo_autor.get_nombre(), nuevo_autor.get_fecha()]
        self.Api_lista_autores.insert(indice, datos_nuevos)

    def remover_autores(self, nombre_autor):
        for item in self.Api_lista_autores:
            if item and item[0] == nombre_autor:
                self.Api_lista_autores.remove(item)
                return
        raise ValueError(f"Autor con nombre '{nombre_autor}' no encontrado")

    def eliminar_autores(self, indice=-1):
        return self.Api_lista_autores.pop(indice)

    def buscar_autores(self, nombre_autor):
        return self.Api_lista_autores.index(nombre_autor)

    def contar_autores(self, valor_autores):
        return self.Api_lista_autores.count(valor_autores)
    
    def ordenar_autores(self, reverse=False):
        self.Api_lista_autores.sort(key=lambda x: x[0] if x else "", reverse=reverse)

    def invertir_autores(self):
        self.Api_lista_autores.reverse()

    def mostrar_lista_autores(self):
        print("Lista de autores:")
        for i, autor in enumerate(self.Api_lista_autores):
            print(f"[{i}] -> {autor}")