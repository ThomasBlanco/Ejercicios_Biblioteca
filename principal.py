from Libro_modelo import Libro_modelo
from Autores import Autor_modelo
from Libro_bd import base_datos_libro
from api_datos_autores import Api_lista_autores

# Creo los objetos de base de datos y api de autores
obj_bd = base_datos_libro()
obj_api_autores = Api_lista_autores()

# Crear los autores
autor1 = Autor_modelo("Sofia", "Blanco", "23", "2001", "Coreana")
autor2 = Autor_modelo("Yasmin", "Costero", "35", "1989", "Estadounidense")
autor3 = Autor_modelo("Gabriela", "Ortega", "28", "1996", "Argentina")
autor4 = Autor_modelo("Carlos", "Perez", "32", "1992", "Mexicano")

# Creo los libros
obj_libro1 = Libro_modelo("2019-01-08", 250, "Aventura", "No Ficción")
obj_libro2 = Libro_modelo("2023-05-15", 300, "Ciencia", "Ficción")
obj_libro3 = Libro_modelo("2022-11-20", 150, "Historia", "Ficción")
obj_libro4 = Libro_modelo("2021-07-10", 200, "Filosofía", "Ficción")
obj_libro5 = Libro_modelo("2020-03-30", 400, "Arte", "No Ficción") 
obj_libro6 = Libro_modelo("2019-12-25", 180, "Misterio", "Ficción")

#mostrar información de autores y sus libros

print("INFORMACIÓN DE AUTORES Y SUS LIBROS")


print("\n------ AUTOR 1 ------")
autor1.ver_info()
print("Libros:")
obj_libro1.ver_info()
obj_libro4.ver_info()

print("\n------ AUTOR 2 ------")
autor2.ver_info()
print("Libros:")
obj_libro2.ver_info()
obj_libro6.ver_info()

print("\n------ AUTOR 3 ------")
autor3.ver_info()
print("Libros:")
obj_libro3.ver_info()
obj_libro5.ver_info()

print("\n------ AUTOR 4 ------")
autor4.ver_info()


print("OPERACIONES CON BASE DE DATOS DE LIBROS")


# Guardar libros
obj_bd.guardar_libro(obj_libro1)
obj_bd.guardar_libro(obj_libro2)
obj_bd.guardar_libro(obj_libro3)
obj_bd.guardar_libro(obj_libro4)
obj_bd.guardar_libro(obj_libro5)
obj_bd.guardar_libro(obj_libro6)

print(f"\nLibros guardados: {obj_bd.contar_total_libros()}")

# Extender lista con nuevos libros
obj_bd.extender_libros([Libro_modelo("2020-03-30", 400, "Arte", "No Ficción"), Libro_modelo("2019-12-25", 180, "Misterio", "Ficción")])

print(f"Libros después de extender: {obj_bd.contar_total_libros()}")

# Insertar libro en posición específica
obj_bd.insertar_libro(1, Libro_modelo("2021-07-10", 200, "Filosofía", "No Ficción"))
print(f"Libros después de insertar: {obj_bd.contar_total_libros()}")

# Remover libro
obj_bd.remover_libros(obj_libro2)
print(f"Libros después de remover: {obj_bd.contar_total_libros()}")

# Eliminar libro por índice
obj_bd.eliminar_libros(2)
print(f"Libros después de eliminar: {obj_bd.contar_total_libros()}")

# Ordenar y mostrar
obj_bd.ordenar_libros()
obj_bd.invertir_libros()

print("\n------ LISTA DE LIBROS EN BD ------")
obj_bd.mostrar_info()


print("OPERACIONES CON API DE AUTORES")


# Guardamos los cuatro autores
obj_api_autores.guardar_autores(autor1)
obj_api_autores.guardar_autores(autor2)
obj_api_autores.guardar_autores(autor3)
obj_api_autores.guardar_autores(autor4)

print(f"\nAutores guardados: {obj_api_autores.contar_total_autores()}")

# Ordenar e invertir
obj_api_autores.ordenar_libros()
obj_api_autores.invertir_libros()

# resultado de Búsquedas
resultado_busca_gabriela = obj_api_autores.buscar_libros("Gabriela")
resultado_cuenta_carlos = obj_api_autores.contar_libros("Carlos")

print(f"Búsqueda de 'Gabriela': {len(resultado_busca_gabriela)} encontrado(s)")
print(f"Conteo de 'Carlos': {resultado_cuenta_carlos} encontrado(s)")

# Mostrar todos los autores
print("\n------ LISTA DE AUTORES EN API ------")
obj_api_autores.mostrar_lista_autores()





