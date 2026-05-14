import json
#Toda esta parte la uso para cargar y usar los .json de los libros y usuarios

#Esta función lee los libros del .json
def cargar_libros():
    try:
        with open("libros.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

#Esta función guarda la lista libros
#ensure_ascii=False permite acentos y ñ correctamente
def guardar_libros(libros):
    with open("libros.json", "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)

#Esta función lee los usuarios en usuarios.json
def cargar_usuarios():
    try:
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
#Esta función guarda los usuarios
def guardar_usuarios(usuarios):

    with open("usuarios.json", "w", encoding="utf-8") as archivo:

        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

#Esta función te loguea en el sistema con tu usuario y contraseña
def login(usuarios):

    print("\n--- INICIO DE SESION ---")

    usuario = input("Usuario: ").lower()
    contraseña = input("Contraseña: ")

    for u in usuarios:
        
        if u["usuario"] == usuario and u["contraseña"] == contraseña:

            print(f"\nBienvenido {usuario} :D")
            return usuario

    print("\nUsuario o contraseña incorrectos.")
    return None

#Esta función registra a nuevos usuarios
def registrar_usuario(usuarios):

    print("\n--- REGISTRO DE USUARIO ---")

    nuevo_usuario = input("Nuevo usuario: ").lower()
    nueva_contraseña = input("Nueva contraseña: ")

    for u in usuarios:

        if u["usuario"] == nuevo_usuario:
            print("Ese usuario ya existe.")
            return

    usuario_nuevo = {
        "usuario": nuevo_usuario,
        "contraseña": nueva_contraseña
    }

    usuarios.append(usuario_nuevo)

    guardar_usuarios(usuarios)

    print("Usuario registrado correctamente :D")

#Este es el menu para poder seleccionar la opcion que nos interesa.
def buscar_libros(libros):
    tema = input("Ingresa el tema del libro que quieres buscar. Si son varios temas, separalos por comas. ").lower()
    temas = [t.strip() for t in tema.split(",")]

    resultados = []

    for libro in libros:

        for etiqueta in libro["etiquetas"]:
            if etiqueta in temas:
                resultados.append(libro)
                break
    
    if resultados:
        
        print("\n Libros encontrados :D :")
        for libro in resultados:
            if libro["disponible"]:

                estado = "Disponible"

            else:

                estado = f'Prestado a {libro["prestado_a"]}'
            print(f"-ID: {libro["id"]} | -{libro['titulo']} de {libro['autor']} | Estado: {estado} | Etiquetas: {','.join(libro['etiquetas'])}")
    else:
           print("No se encontraron libros de ese tema :c, quieres agregar o volver a buscar?")

#Este bloque fue meramente hecho para buscar los libros. recuerda que el .join es para juntar las palabras y que no quede todo por separado.
def agregar_libro(libros):
    titulo = input("Titulo del libro:")
    autor = input("Autor del libro:")
    etiquetas = input("Etiquetas (deben ir separadas por coma):").lower()
    nuevo_id = len(libros) + 1
    lista_etiquetas = [e.strip() for e in etiquetas.split(",")]

    nuevo_libro = {"id": nuevo_id ,
    "titulo": titulo,
    "autor": autor,
    "etiquetas": lista_etiquetas,
    "disponible": True,
    "prestado_a": None}

    libros.append(nuevo_libro)

    guardar_libros(libros)

    print("Libro agregado con exito :D.")

#Este bloque es para el funcionamiento de agregar libros.
def ver_libros(libros):
    if libros:
        print("\n Aqui puedes ver nuestra biblioteca completa. Si el libro que buscas no se encuentra puedes agregarlo.")
        for libro in libros:

            if libro["disponible"]:
                estado = "disponible"
            else:
                estado = f"Prestado a {libro["prestado_a"]}"

            print(f"-ID: {libro["id"]} | -{libro['titulo']} de {libro['autor']} | Estado: {estado} | Etiquetas:{','.join(libro['etiquetas'])}")
    else:
        print("Lo sentimos, no tenemos ese libro disponible :c.") 

#Esta función te permite alquilar
def alquilar_libro(libros, usuario_actual):

    print("\n--- LIBROS DISPONIBLES ---")

    disponibles = False

    for libro in libros:
        
        #Esta parte revisa si existe por lo menos un libro disponible e imprime su id y su título
        if libro["disponible"]:

            disponibles = True

            print(f'{libro["id"]} - {libro["titulo"]}')

    if not disponibles:

        print("No hay libros disponibles.")
        return

    while(True):
        
        entrada = input("Ingresa el ID del libro que quiera alquilar o escribe 'salir': ")
        if entrada.lower() == "salir":
            print("Saliendo del menú...")
            return

        try:
            libro_id = int(entrada)
        except ValueError:
            print("Ingresa un número entero")
        else:
            if libro_id < 0:
                print("Ingresa un número positivo")
            
            else:
                break

    for libro in libros:

        if libro["id"] == libro_id:

            if libro["disponible"]:

                libro["disponible"] = False
                libro["prestado_a"] = usuario_actual

                guardar_libros(libros)

                print("Libro prestado correctamente :D")

            else:

                print("Ese libro ya esta prestado.")

            return

    print("Libro no encontrado.")

#Esta función te permite devolver un libro
def devolver_libro(libros, usuario_actual):

    print("\n--- TUS LIBROS ---")

    encontrados = False

    for libro in libros:

        if libro["prestado_a"] == usuario_actual:

            encontrados = True

            print(f'{libro["id"]} - {libro["titulo"]}')

    if not encontrados:

        print("No tienes libros prestados.")
        return

    while(True):
        
        entrada = input("Ingresa el ID del libro a devolver o escribe 'salir': ")
        if entrada.lower() == "salir":
            print("Saliendo del menú...")
            return

        try:
            libro_id = int(entrada)
        except ValueError:
            print("Ingresa un número entero")
        else:
            if libro_id < 0:
                print("Ingresa un número positivo")
            
            else:
                break

    for libro in libros:

        if libro["id"] == libro_id and libro["prestado_a"] == usuario_actual:

            libro["disponible"] = True
            libro["prestado_a"] = None

            guardar_libros(libros)

            print("Libro devuelto correctamente :D")

            return

    print("No puedes devolver ese libro.")

#Funciones para los menus
def menu_inicio():
    print("\n--- BIBLIOTECA ---")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. salir ")


def mostrar_menu():
    print(" Bienvenido a nuestra Biblioteca!! :D ")
    print("1. Buscar libros por tema")
    print("2. Agregar libros")
    print("3. Ver todos los libros")
    print("4. Alquilar libro")
    print("5. Devolver libro")
    print("6. cerrar sesión ")

#Les asigno las funciones de cargar los libros y usuarios a una variable para mayor comodidad
libros = cargar_libros()
usuarios = cargar_usuarios()


while True:

    usuario_actual = None

    while usuario_actual is None:

        menu_inicio()

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            usuario_actual = login(usuarios)

        elif opcion == "2":
            registrar_usuario(usuarios)

        elif opcion == "3":
            print("Saldras de la biblioteca. Hasta pronto!")
            exit() #Este exit() Cierra el programa por completo, lo uso debido a que un break me mandaría al siguiente menú

        else:
            print("Opcion invalida.")

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            buscar_libros(libros)

        elif opcion == "2":
            agregar_libro(libros)

        elif opcion == "3":
            ver_libros(libros)

        elif opcion == "4":
            alquilar_libro(libros, usuario_actual)

        elif opcion == "5":
            devolver_libro(libros, usuario_actual)

        elif opcion == "6":
            print("Cerrando sesión...")
            break

        else:
            print("Opcion invalida.")