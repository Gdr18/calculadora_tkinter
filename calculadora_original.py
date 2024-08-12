def saludo():
    print("Bienvenidx a la calculadora!")
    print("Las operaciones son: suma, resta, div y multi.")
    print("Para salir del juego escriba: salir.")
    return primer_numero()


def primer_numero():
    n1 = input("Ingrese la primera cifra: ")

    if n1.lower() == "salir":
        print("Hasta la próxima!")
    else:
        try:
            n1 = float(n1)
        except ValueError:
            print("Sólo son aceptados números.")
            return primer_numero()
        else:
            return operacion(n1)


def operacion(n1):
    op = input("Ingrese un operador: ")

    if op.lower() == "salir":
        print("Hasta la próxima!")
    elif (
        op.lower() != "suma"
        and op.lower() != "resta"
        and op.lower() != "multi"
        and op.lower() != "div"
    ):
        print("Sólo son aceptados los siguientes operadores: suma, resta, multi o div.")
        return operacion(n1)
    else:
        return segundo_numero(op, n1)


def segundo_numero(op, n1):
    n2 = input("Ingrese la segunda cifra: ")

    if n2.lower() == "salir":
        print("Hasta la próxima!")
    else:
        try:
            n2 = float(n2)
        except ValueError:
            print("Sólo son aceptados números.")
            return segundo_numero(op, n1)
        else:
            if op.lower() == "suma":
                print(f"El resultado es: {n1 + n2}")
            elif op.lower() == "resta":
                print(f"El resultado es: {n1 - n2}")
            elif op.lower() == "multi":
                print(f"El resultado es: {n1 * n2}")
            elif op.lower() == "div":
                print(f"El resultado es: {n1 / n2}")
            return primer_numero()


saludo()
