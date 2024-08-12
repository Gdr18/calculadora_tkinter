import tkinter


def recibir_datos_caja_texto():
    input_usuario = caja_texto.get()
    print("El usuario ha escrito: ", caja_texto.get())
    etiqueta["text"] = input_usuario
    etiqueta["bg"] = "red"
    # Para borrar el contenido de la caja de texto, el '0' representa el inicio y 'end' el final
    caja_texto.delete(0, "end")
    return input_usuario


ventana = tkinter.Tk()
# ventana.geometry("400x400")

ventana.title("Calculadora")

caja_texto = tkinter.Entry(ventana, font=("Google Sans Mono", 14))
caja_texto.pack()

# Para pasar argumentos a la función habría que utilizar una función lambda command= lambda: saludo("Gádor")
boton = tkinter.Button(
    ventana, text="Enviar", padx=25, pady=25, command=recibir_datos_caja_texto
)
# boton = tkinter.Button(
#     ventana, text="Enviar", width=25, height=25, command=recibir_datos_caja_texto
# )
boton.pack()

# Crear una etiqueta, con el texto "Calculadora", y dándole un background de color
# etiqueta = tkinter.Label(ventana, text="Calculadora", bg="red")
etiqueta = tkinter.Label(ventana)
# Para poner la etiqueta en la ventana, y que se expanda
# etiqueta.pack(fill="both", expand=True)
# Para poner la etiqueta en la ventana, y la posición que va a ocupar
# etiqueta.pack(side="top", fill="x")
# etiqueta.grid(row=0, column=0)
etiqueta.pack()

ventana.mainloop()
