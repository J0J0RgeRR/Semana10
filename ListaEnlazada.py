"""Lista enlazada simple: gestión de turnos."""


def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}


def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo


def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo
    return cabeza


def mostrar(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" → ")
        actual = actual["siguiente"]
    print("None")


def buscar(cabeza, dato):
    actual = cabeza
    posicion = 0
    while actual is not None:
        if actual["dato"] == dato:
            return posicion
        actual = actual["siguiente"]
        posicion += 1
    return -1


def eliminar(cabeza, dato):
    if cabeza is None:
        return None, False
    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True
    anterior = cabeza
    actual = cabeza["siguiente"]
    while actual is not None:
        if actual["dato"] == dato:
            anterior["siguiente"] = actual["siguiente"]
            return cabeza, True
        anterior = actual
        actual = actual["siguiente"]
    return cabeza, False


def contar(cabeza):
    total = 0
    actual = cabeza
    while actual is not None:
        total += 1
        actual = actual["siguiente"]
    return total


def menu():
    cabeza = None
    while True:
        print("\n1. Agregar al inicio  2. Agregar al final  3. Mostrar")
        print("4. Buscar  5. Eliminar turno  6. Contar  0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            break
        if opcion in ("1", "2", "4", "5"):
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Escriba un nombre.")
                continue
        match opcion:
            case "1":
                cabeza = insertar_inicio(cabeza, nombre)
            case "2":
                cabeza = insertar_final(cabeza, nombre)
            case "3":                mostrar(cabeza)
            case "4":
                posicion = buscar(cabeza, nombre)
                if posicion != -1:
                    print(f"{nombre} encontrado en la posición {posicion}.")
                else:
                    print(f"{nombre} no encontrado.")
            case "5":
                cabeza, eliminado = eliminar(cabeza, nombre)
                if eliminado:
                    print(f"{nombre} eliminado.")
                else:
                    print(f"{nombre} no encontrado.")
            case "6":
                total = contar(cabeza)
                print(f"Total de turnos: {total}")
            case _:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()