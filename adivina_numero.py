import random

print("Bienvenido al Juego: Adivina el Número!")
print("El objetivo del juego es adivinar un número secreto entre 1 y 10")
print("Tienes 5 intentos para adivinar el número secreto")
print("Para salir del juego escribe: SALIR")


def adivina(a, b):
    numero_secreto = random.randint(a, b)
    rondas = 0
    salida = False

    while rondas < 5 and salida == False:
        numero_jugador = input(f"Inserta un número entre {a} y {b}: ")
        if numero_jugador.upper() == "SALIR":
            salida = True
        else:
            try:
                numero_jugador = int(numero_jugador)
                if numero_jugador == numero_secreto:
                    print("Felicidades!! Lo acertaste!!")
                    while True:
                        nueva_ronda = input(
                            '¿Deseas jugar de nuevo? Responde con "SI" o "NO": '
                        )
                        if nueva_ronda.upper() == "SI":
                            while True:
                                dificultad = input(
                                    '¿Deseas aumentar la dificultad? Responde con "SI" o "NO": '
                                )
                                if dificultad.upper() == "SI":
                                    return adivina(1, b + 5)
                                elif dificultad.upper() == "NO":
                                    return adivina(a, b)
                                else:
                                    print("Debes responder con 'SI' o 'NO'")
                                    continue
                        elif nueva_ronda.upper() == "NO":
                            salida = True
                            break
                        else:
                            print("Debes responder con 'SI' o 'NO'")
                            continue
                else:
                    rondas += 1
                    if numero_jugador < numero_secreto:
                        print("El número es demasiado bajo...")
                    elif numero_jugador > numero_secreto:
                        print("El número es demasiado alto...")
            except ValueError:
                print("Debes ingresar un número entero")
                continue

    if rondas == 5 and salida == False:
        print(f"Ooohh fallaste, el número secreto era {numero_secreto}")
        while True:
            nueva_ronda = input(
                "¿Deseas intentarlo de nuevo? Responde con 'SI' o 'NO': "
            )
            if nueva_ronda.upper() == "SI":
                return adivina(a, b)
            elif nueva_ronda.upper() == "NO":
                salida = True
                break
            else:
                print("Debes responder con 'SI' o 'NO'")
                continue

    if salida == True:
        print("Gracias por jugar!!")


adivina(1, 10)
