import tkinter
from functools import reduce

window = tkinter.Tk()

list_numbers = []
operators = []

window.geometry("260x475")

window.title("Calculadora")

screen_dos = tkinter.Label(window, bg="#E5E5E5", text="", font=("Google Sans Mono", 14))
screen_dos.grid(row=0, column=0, columnspan=5, sticky="nsew")
screen_dos.config(anchor=tkinter.E, fg="#AAA9A9")

screen = tkinter.Label(window, bg="#E5E5E5", text="0", font=("Google Sans Mono", 34))
screen.grid(row=1, column=1, columnspan=5, sticky="nsew")
screen.config(anchor=tkinter.E)


# BUTTONS
button_options = {"width": 5, "height": 2, "font": ("Google Sans Mono", 14)}

percentage = tkinter.Button(
    window, **button_options, text="%", command=lambda: operator_function("%")
)
percentage.grid(row=2, column=1)

remove = tkinter.Button(
    window, **button_options, text="CE", command=lambda: clear("CE")
)
remove.grid(row=2, column=2)

remove_all = tkinter.Button(
    window, **button_options, text="C", command=lambda: clear("C")
)
remove_all.grid(row=2, column=3)

division = tkinter.Button(
    window, **button_options, text="/", command=lambda: operator_function("/")
)
division.grid(row=2, column=4)

seven = tkinter.Button(
    window, **button_options, text="7", command=lambda: digit_function("7")
)
seven.grid(row=3, column=1)

eight = tkinter.Button(
    window, **button_options, text="8", command=lambda: digit_function("8")
)
eight.grid(row=3, column=2)

nine = tkinter.Button(
    window, **button_options, text="9", command=lambda: digit_function("9")
)
nine.grid(row=3, column=3)

multi = tkinter.Button(
    window, **button_options, text="x", command=lambda: operator_function("x")
)
multi.grid(row=3, column=4)

four = tkinter.Button(
    window, **button_options, text="4", command=lambda: digit_function("4")
)
four.grid(row=4, column=1)

five = tkinter.Button(
    window, **button_options, text="5", command=lambda: digit_function("5")
)
five.grid(row=4, column=2)

six = tkinter.Button(
    window, **button_options, text="6", command=lambda: digit_function("6")
)
six.grid(row=4, column=3)

minus = tkinter.Button(
    window, **button_options, text="-", command=lambda: operator_function("-")
)
minus.grid(row=4, column=4)

one = tkinter.Button(
    window, **button_options, text="1", command=lambda: digit_function("1")
)
one.grid(row=5, column=1)

two = tkinter.Button(
    window, **button_options, text="2", command=lambda: digit_function("2")
)
two.grid(row=5, column=2)

three = tkinter.Button(
    window, **button_options, text="3", command=lambda: digit_function("3")
)
three.grid(row=5, column=3)

plus = tkinter.Button(
    window, **button_options, text="+", command=lambda: operator_function("+")
)
plus.grid(row=5, column=4)

plus_minus = tkinter.Button(
    window, **button_options, text="+/-", command=lambda: operator_function("+/-")
)
plus_minus.grid(row=6, column=1)

zero = tkinter.Button(
    window, **button_options, text="0", command=lambda: digit_function("0")
)
zero.grid(row=6, column=2)

dot = tkinter.Button(
    window, **button_options, text=".", command=lambda: digit_function(",")
)
dot.grid(row=6, column=3)

equal = tkinter.Button(
    window, **button_options, text="=", command=lambda: operator_function("=")
)
equal.grid(row=6, column=4)


def clear(option):
    screen["text"] = "0"
    screen["font"] = ("Google Sans Mono", 34)
    if "=" in screen_dos["text"]:
        screen_dos["text"] = ""
    if option == "C":
        screen_dos["text"] = ""
        list_numbers.clear()
        operators.clear()


def digit_function(character):
    if len(screen["text"]) == 15:
        return
    elif not "=" in screen_dos["text"] and (screen["text"] != "0" or character == ","):
        screen["text"] += character
    else:
        screen["text"] = character
        if "=" in screen_dos["text"]:
            screen_dos["text"] = ""

    if len(screen["text"]) > 9:
        screen["font"] = ("Google Sans Mono", 20)
    else:
        screen["font"] = ("Google Sans Mono", 34)


def calculate():
    if "%" in operators:
        result = list_numbers[operators.index("%")] / 100
    elif operators[0] == "+":
        result = list_numbers[0] + list_numbers[1]
    elif operators[0] == "-":
        result = list_numbers[0] - list_numbers[1]
    elif operators[0] == "x":
        result = list_numbers[0] * list_numbers[1]
    elif operators[0] == "/":
        result = list_numbers[0] / list_numbers[1]

    if str(result).endswith(",0"):
        result = int(result)
    if len(str(result)) > 9:
        screen["font"] = ("Google Sans Mono", 20)

    # TODO: Terminar de implementar la notación científica
    # if len(str(result)) > 15:
    #     result = "{:.2e}".format(result)

    print(result, "calculate")

    return result


def operator_function(character):
    global list_numbers, screen_dos
    if character == "+/-" and screen["text"] != "0":
        if "-" in screen["text"]:
            screen["text"] = screen["text"].replace("-", "")
        else:
            screen["text"] = "-" + screen["text"]
    elif character == "%" and len(operators) == 0:
        screen["text"] = "0"
    elif character == "=" and len(operators) == 0:
        screen_dos = screen["text"] + " " + character + " "
    else:
        operators.append(character)
        if "." in screen["text"]:
            list_numbers.append(float(screen["text"]))
        else:
            list_numbers.append(int(screen["text"]))
        print(list_numbers, "list_numbers cuando se agrega, operator_function")

        if len(list_numbers) == 1:
            screen_dos["text"] = screen["text"] + " " + character + " "
            screen["text"] = "0"
        else:
            result = calculate()
            if character == "%":
                list_numbers[1] = result
                screen_dos["text"] += str(result)
                screen["text"] = "0"
                operators.remove(character)
            elif character == "=":
                screen_dos["text"] += screen["text"] + " " + character + " "
                screen["text"] = str(result)
                list_numbers.clear()
                operators.clear()
            else:
                screen_dos["text"] = str(result) + " " + character + " "
                screen["text"] = "0"
                list_numbers = [result]
                operators.remove(operators[0])

            print(list_numbers, "list_numbers despues de calculate, operator_function")
            print(operators, "operators despues de calculate, operator_function")


window.mainloop()
