from Libro_modelo import Libro_modelo
from Autores import Autor_modelo
from Libro_bd import base_datos_libro
from api_datos_autores import Api_lista_autores

obj_bd = base_datos_libro()

# Crear libros primero
obj_libro1 = Libro_modelo("2019-01-08", 250, "Aventura", "No Ficción")
obj_libro2 = Libro_modelo("2023-05-15", 300, "Ciencia", "Ficción")
obj_libro3 = Libro_modelo("2022-11-20", 150, "Historia", "Ficción")
obj_libro4 = Libro_modelo("2021-07-10", 200, "Filosofía", "Ficción")
obj_libro5 = Libro_modelo("2020-03-30", 400, "Arte", "No Ficción") 
obj_libro6 = Libro_modelo("2019-12-25", 180, "Misterio", "Ficción")

# Listas de datos autor con libros asociados 
lista_datos_autor1 = {
    "nombre": "Sofia",
    "apellido": "Blanco",
    "edad": "23",
    "año": "2001",
    "pais": "Coreana",
    "libros": [obj_libro1, obj_libro4]  
}

lista_datos_autor2 = {
    "nombre": "Yasmin",
    "apellido": "Costero",
    "edad": "35",
    "año": "1989",
    "pais": "Estadounidense",
    "libros": [obj_libro2, obj_libro6]  
}

lista_datos_autor3 = {
    "nombre": "Gabriela",
    "apellido": "Ortega",
    "edad": "28",
    "año": "1996",
    "pais": "Argentina",
    "libros": [obj_libro3, obj_libro5]  
}

lista_datos_autor4 = {
    "nombre": "Carlos",
    "apellido": "Perez",
    "edad": "32",
    "año": "1992",
    "pais": "Mexicano",
    "libros": []
}

print("\n------ LISTA LIBROS AUTOR 1 ------")
print(f"Nombre: {lista_datos_autor1['nombre']}")
print(f"Apellido: {lista_datos_autor1['apellido']}")
print(f"Edad: {lista_datos_autor1['edad']}")
print(f"Año: {lista_datos_autor1['año']}")
print(f"País: {lista_datos_autor1['pais']}")
for libro in lista_datos_autor1['libros']:
    print(libro.ver_info_libro())

print("\n------ LISTA LIBROS AUTOR 2 ------")
print(f"Nombre: {lista_datos_autor2['nombre']}")
print(f"Apellido: {lista_datos_autor2['apellido']}")
print(f"Edad: {lista_datos_autor2['edad']}")
print(f"Año: {lista_datos_autor2['año']}")
print(f"País: {lista_datos_autor2['pais']}")
for libro in lista_datos_autor2['libros']:
    print(libro.ver_info_libro())

print("\n------ LISTA LIBROS AUTOR 3 ------")
print(f"Nombre: {lista_datos_autor3['nombre']}")
print(f"Apellido: {lista_datos_autor3['apellido']}")
print(f"Edad: {lista_datos_autor3['edad']}")
print(f"Año: {lista_datos_autor3['año']}")
print(f"País: {lista_datos_autor3['pais']}")
for libro in lista_datos_autor3['libros']:
    print(libro.ver_info_libro())

print("\n------ LISTA LIBROS AUTOR 4 ------")
print(f"Nombre: {lista_datos_autor4['nombre']}")
print(f"Apellido: {lista_datos_autor4['apellido']}")
print(f"Edad: {lista_datos_autor4['edad']}")
print(f"Año: {lista_datos_autor4['año']}")
print(f"País: {lista_datos_autor4['pais']}")

obj_bd.guardar_libro(obj_libro1)
obj_bd.guardar_libro(obj_libro2)
obj_bd.guardar_libro(obj_libro3)
obj_bd.guardar_libro(obj_libro4)
obj_bd.guardar_libro(obj_libro5)
obj_bd.guardar_libro(obj_libro6)

obj_bd.extender_libros([Libro_modelo("2020-03-30", 400, "Arte", "No Ficción"), Libro_modelo("2019-12-25", 180, "Misterio", "Ficción")])

obj_bd.insertar_libro(1, Libro_modelo("2021-07-10", 200, "Filosofía", "No Ficción"))

obj_bd.remover_libros(obj_libro2)

obj_bd.eliminar_libros(2)

resultado_busca = obj_bd.buscar_libros(obj_libro1)

resultado_conta = obj_bd.contar_libros(obj_libro3)

obj_bd.ordenar_libros()

obj_bd.invertir_libros()

obj_bd.mostrar_info()

# API de autores
obj_api_autores = Api_lista_autores(None, None, None, None)

# Guardar los 4 autores
obj_api_autores.guardar_autores(Autor_modelo("Sofia", "Blanco", "23", "2001", "Coreana"))
obj_api_autores.guardar_autores(Autor_modelo("Yasmin", "Costero", "35", "1989", "Estadounidense"))
obj_api_autores.guardar_autores(Autor_modelo("Gabriela", "Ortega", "28", "1996", "Argentina"))
obj_api_autores.guardar_autores(Autor_modelo("Carlos", "Perez", "32", "1992", "Mexicano"))

# Operaciones sobre la lista
obj_api_autores.ordenar_libros()
obj_api_autores.invertir_libros()
resultado_busca_autor = obj_api_autores.buscar_libros("Gabriela")
resultado_conta_autor = obj_api_autores.contar_libros("Carlos")

# Mostrar todos los autores en la lista
print("\n------ LISTA DE AUTORES EN API ------")
obj_api_autores.mostrar_lista_autores()



