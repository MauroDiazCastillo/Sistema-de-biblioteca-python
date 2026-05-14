# Sistema de Gestión de Biblioteca en Python

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión de biblioteca realizado en Python.  
El programa permite administrar libros y usuarios mediante un sistema de menús interactivos en consola, utilizando archivos JSON para almacenar la información de manera persistente.

---

# Objetivos del proyecto

## Objetivo general

Desarrollar un sistema básico de biblioteca que permita gestionar usuarios y libros mediante programación en Python.

## Objetivos específicos

- Implementar un sistema de inicio de sesión y registro.
- Guardar información utilizando archivos JSON.
- Permitir búsqueda de libros por categorías.
- Gestionar préstamos y devoluciones.
- Validar entradas incorrectas del usuario.
- Organizar el programa mediante funciones.

---

# Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| JSON | Almacenamiento de datos |
| Consola | Interfaz de usuario |

---

# Estructura del proyecto

```plaintext
Proyecto Biblioteca/
│
├── biblioteca.py
├── libros.json
├── usuarios.json
└── README.md
```

---

# Explicación de los archivos

## `biblioteca.py`

Archivo principal que contiene toda la lógica del sistema.

---

## `libros.json`

Contiene la información de todos los libros registrados.

Ejemplo:

```json
{
    "id": 1,
    "titulo": "Cien años de soledad",
    "autor": "Gabriel Garcia Marquez",
    "etiquetas": [
        "novela",
        "literatura"
    ],
    "disponible": true,
    "prestado_a": null
}
```

---

## `usuarios.json`

Almacena la información de los usuarios registrados.

Ejemplo:

```json
{
    "usuario": "mauro",
    "contraseña": "1234"
}
```

---

# Funcionalidades implementadas

## Gestión de usuarios

- Registro de usuarios.
- Inicio de sesión.
- Validación de usuarios existentes.
- Cierre de sesión.

---

## Gestión de libros

- Ver todos los libros.
- Agregar libros nuevos.
- Buscar libros por etiquetas o temas.
- Mostrar disponibilidad de libros.

---

## Sistema de préstamos

- Alquilar libros disponibles.
- Registrar el usuario que tiene el préstamo.
- Devolver libros prestados.
- Evitar préstamos duplicados.

---

## Validación de entradas

El programa incluye validaciones para evitar:

- Ingreso de letras donde se esperan números.
- IDs negativos.
- Usuarios duplicados.
- Intentos de alquilar libros inexistentes.

---

# Funcionamiento general del sistema

## Diagrama general del flujo

```plaintext
INICIO
   │
   ▼
MENÚ PRINCIPAL
   │
   ├── Iniciar sesión
   │        │
   │        ▼
   │   MENÚ BIBLIOTECA
   │        │
   │        ├── Buscar libros
   │        ├── Agregar libros
   │        ├── Ver libros
   │        ├── Alquilar libro
   │        ├── Devolver libro
   │        └── Cerrar sesión
   │
   ├── Registrarse
   │
   └── Salir
```

---

# Diagrama del sistema de préstamo

```plaintext
Usuario selecciona alquilar libro
              │
              ▼
Mostrar libros disponibles
              │
              ▼
Ingresar ID del libro
              │
              ▼
¿El libro existe?
        │
 ┌──────┴──────┐
 │             │
Sí            No
 │             │
 ▼             ▼
¿Está disponible?   Mostrar error
 │
 ┌──────┴──────┐
 │             │
Sí            No
 │             │
 ▼             ▼
Asignar usuario   Mostrar mensaje
Guardar cambios
```

---

# Explicación de algunas funciones importantes

## `cargar_libros()`

Lee la información del archivo `libros.json` y la convierte en estructuras de Python.

---

## `guardar_libros()`

Guarda automáticamente los cambios realizados en los libros.

---

## `login()`

Verifica que el usuario y contraseña coincidan con los datos registrados.

---

## `buscar_libros()`

Permite buscar libros mediante etiquetas ingresadas por el usuario.

---

## `alquilar_libro()`

Controla el préstamo de libros disponibles y actualiza el estado del libro.

---

## `devolver_libro()`

Permite devolver libros previamente alquilados.

---

# Manejo de persistencia de datos

El programa utiliza archivos JSON para conservar la información incluso después de cerrar el programa.

Esto permite:

- mantener usuarios registrados,
- conservar libros agregados,
- guardar préstamos activos.

---

# Problemas encontrados durante el desarrollo

Durante el desarrollo surgieron varios problemas importantes:

- Manejo de rutas de archivos JSON.
- Validación de entradas incorrectas.
- Control de disponibilidad de libros.
- Manejo de sesiones y usuarios.

---

# Posibles mejoras futuras

El proyecto puede seguir expandiéndose con funcionalidades más avanzadas:

- Interfaz gráfica con Tkinter.
- Uso de SQLite como base de datos real.
- Contraseñas cifradas.
- Historial de préstamos.
- Fechas límite de devolución.
- Sistema de multas.
- Eliminación y edición de libros.
- Búsqueda por autor.

---

# Conclusión

Este proyecto permitió aplicar conceptos fundamentales de programación en Python, incluyendo:

- estructuras de datos,
- funciones,
- manejo de archivos,
- validación de entradas,
- organización modular del código,
- y persistencia de información.

Además, el sistema desarrollado representa una aproximación básica a un sistema real de gestión de bibliotecas.

---

# Autor

Proyecto desarrollado como práctica universitaria de programación en Python.
