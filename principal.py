from Libro_modelo import Libro_modelo
from Autores import Autor_modelo
from Libro_bd import base_datos_libro
from api_datos_autores import Api_lista_autores

obj_bd = base_datos_libro()

obj_autor = Autor_modelo("sofia", "blanco","23", "2003","Koreana" )

# Crear libros primero
obj_libro1 = Libro_modelo("2019-01-08", 250, "Aventura", "No Ficción")
obj_libro2 = Libro_modelo("2023-05-15", 300, "Ciencia", "Ficción")
obj_libro3 = Libro_modelo("2022-11-20", 150, "Historia", "Ficción")
obj_libro4 = Libro_modelo("2021-07-10", 200, "Filosofía", "Ficción")
obj_libro5 = Libro_modelo("2020-03-30", 400, "Arte", "No Ficción") 
obj_libro6 = Libro_modelo("2019-12-25", 180, "Misterio", "Ficción")

# Listas de datos autor con libros asociados
print("Lista de datos del autor con libros asociados:")

lista_datos_autor1 = { "LISTA DE DATOS DEL AUTOR 1": {
    "nombre": "sofia",
    "apellido": "blanco",
    "edad": "23",
    "año": "2003",
    "pais": "Koreana",
    "libros": [obj_libro1, obj_libro4]  
}}

lista_datos_autor2 = { "LISTA DE DATOS DEL AUTOR 2": {
    "nombre": "Yasmin",
    "apellido": "costero",
    "edad": "37",
    "año": "1989",
    "pais": "Estadounidense",
    "libros": [obj_libro2, obj_libro6]  
}}

lista_datos_autor3 = { "LISTA DE DATOS DEL AUTOR 3": {
    "nombre": "Lucrecia",
    "apellido": "marin",
    "edad": "36",
    "año": "1990",
    "pais": "Colombiana",
    "libros": [obj_libro3, obj_libro5]  
}}

# Mostrar libros de cada autor
print("\n=== LIBROS DE CADA AUTOR ===\n")

for clave, datos in lista_datos_autor1.items():
    print(f"Autor: {datos['nombre'].upper()} {datos['apellido'].upper()}")
    print(f"País: {datos['pais']}")
    print("Libros:")
    for libro in datos['libros']:
        print(f"  Temática: {libro.get_tematica()} | Fecha: {libro.get_fecha()} | Hojas: {libro.get_cantidad_hojas()} | Género: {libro.get_genero()}")
    print()

for clave, datos in lista_datos_autor2.items():
    print(f"Autor: {datos['nombre'].upper()} {datos['apellido'].upper()}")
    print(f"País: {datos['pais']}")
    print("Libros:")
    for libro in datos['libros']:
        print(f"  Temática: {libro.get_tematica()} | Fecha: {libro.get_fecha()} | Hojas: {libro.get_cantidad_hojas()} | Género: {libro.get_genero()}")
    print()

for clave, datos in lista_datos_autor3.items():
    print(f"Autor: {datos['nombre'].upper()} {datos['apellido'].upper()}")
    print(f"País: {datos['pais']}")
    print("Libros:")
    for libro in datos['libros']:
        print(f"  Temática: {libro.get_tematica()} | Fecha: {libro.get_fecha()} | Hojas: {libro.get_cantidad_hojas()} | Género: {libro.get_genero()}")
    print()

obj_bd.guardar_libros(obj_libro1)
obj_bd.guardar_libros(obj_libro2)
obj_bd.guardar_libros(obj_libro3)
obj_bd.guardar_libros(obj_libro4)
obj_bd.guardar_libros(obj_libro5)
obj_bd.guardar_libros(obj_libro6)

obj_bd.extender_libros([Libro_modelo("2020-03-30", 400, "Arte", "No Ficción"), Libro_modelo("2019-12-25", 180, "Misterio", "Ficción")])

obj_bd.insertar_libros(1, Libro_modelo("2021-07-10", 200, "Filosofía", "No Ficción"))

obj_bd.remover_libros(obj_libro2)

obj_bd.eliminar_libros(2)

obj_bd.buscar_libros(obj_libro1)

obj_bd.contar_libros(obj_libro3)

obj_bd.ordenar_libros()

obj_bd.invertir_libros()

obj_bd.mostrar_info()

obj_api_autores = Api_lista_autores()
obj_api_autores.guardar_autores(obj_autor)
obj_api_autores.extender_autores([Autor_modelo("Yasmin", "costero", "37", "1989", "Estadounidense"), Autor_modelo("Lucrecia", "marin", "36", "1990", "Colombiana")])
obj_api_autores.insertar_autores(1, Autor_modelo("Carlos", "Perez", "35", "1991", "Mexicano"))
obj_api_autores.mostrar_lista_autores()


