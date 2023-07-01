# Matriz global para almacenar la disponibilidad de los lotes
clientes = []
matriz = [
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
]

matriz_enumerada = [[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20]]

precio = 100000
tamaño_terreno = "50 km x 50 km"


def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Ver disponibilidad de lotes")
    print("2. Seleccionar un lote")
    print("3. Ver detalles del lote seleccionado")
    print("4. Ver Clientes")
    print("5. Salir")

def ver_disponibilidad_lotes():
    # Mostrar la matriz de disponibilidad de lotes
    print("Lotes Disponibles:")
    for fila in matriz:
        print(" ".join(fila))

def seleccionar_lote():
    ver_disponibilidad_lotes()

    fila = int(input("Ingrese la fila del lote que desea comprar (1-4): "))
    columna = int(input("Ingrese la columna del lote que desea comprar (1-5): "))

    if matriz[fila - 1][columna - 1] == "[ ]":
        # Solicitar datos del usuario
        rut = input("Ingrese su RUT: ")
        nombre = input("Ingrese su nombre completo: ")
        telefono = input("Ingrese su número de teléfono: ")
        email = input("Ingrese su dirección de correo electrónico: ")

        # Realizar el proceso de compra con los datos del usuario
        matriz[fila - 1][columna - 1] = "[X]"
        print("¡Lote seleccionado y comprado con éxito!")
        print("Datos del usuario:")
        print("RUT:", rut)
        print("Nombre:", nombre)
        print("Teléfono:", telefono)
        print("Email:", email)

                # Agregar el nombre del cliente a la lista de clientes
        clientes.append(nombre)

    else:
        print("El lote seleccionado no está disponible para comprar.")

def ver_detalles_lote_seleccionado():
    fila = int(input("Ingrese la fila del lote que desea ver: "))
    columna = int(input("Ingrese la columna del lote que desea ver: "))

    if fila < 1 or fila > len(matriz) or columna < 1 or columna > len(matriz[0]):
        print("La posición ingresada no es válida.")
    else:
        numero_lote = matriz[fila - 1][columna - 1]
        print("Lote seleccionado:")
        print("Número de fila:", fila)
        print("Número de columna:", columna)
        print("Precio:", precio, "pesos chilenos")
        print("Tamaño del terreno:", tamaño_terreno)

def ver_clientes():
    print("Clientes:")
    for cliente in clientes:
        print(cliente)

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_disponibilidad_lotes()
        elif opcion == "2":
            seleccionar_lote()
        elif opcion == "3":
            ver_detalles_lote_seleccionado()
        elif opcion == "4":
            ver_clientes()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

# Llamar a la función principal para iniciar el programa
main()

#prueba
