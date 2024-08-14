import tkinter

window = tkinter.Tk()

list_numbers = []
operators = []

window.geometry("340x390")
window.resizable(False, False)

window.title("Calculadora")

#region SCREENS
secondary_screen = tkinter.Label(
    window,
    fg="aliceblue",
    bg="black",
    text="",
    font=("Google Sans Mono", 14),
    anchor="e",
)
secondary_screen.grid(row=0, column=0, columnspan=5, sticky="nsew")

screen = tkinter.Label(
    window, bg="black", fg="aliceblue", text="0", font=("Google Sans Mono", 30), anchor="e"
)
screen.grid(row=1, column=1, columnspan=5, sticky="nsew")

window.grid_rowconfigure(1, minsize=62)

#region BUTTONS
button_options = {
    "width": 7,
    "height": 1,
    "pady": 8,
    "bg": "#494443",
    "fg": "aliceblue",
    "bd": 1,
    "cursor": "hand2",
    "font": ("Google Sans Mono", 14),
}

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

#region FUNCTIONS
def clear(option):
    screen.config(font=("Google Sans Mono", 30), text="0")
    if "=" in secondary_screen["text"]:
        secondary_screen["text"] = ""
    if option == "C":
        secondary_screen["text"] = ""
        list_numbers.clear()
        operators.clear()


def digit_function(digit):
    if len(screen["text"]) == 15 or ("," in screen["text"] and digit == ","):
        return
    elif screen["text"] == "0" or screen["text"].isalpha() or "No" in screen["text"] or "=" in secondary_screen["text"]:
        if digit == ",":
            screen["text"] = "0" + digit
        else:
            screen["text"] = digit
    else:
        screen["text"] += digit

    if "=" in secondary_screen["text"]:
        secondary_screen["text"] = ""

    if len(screen["text"]) > 10:
        screen["font"] = ("Google Sans Mono", 20)
    else:
        screen["font"] = ("Google Sans Mono", 30)


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
        try:
            result = list_numbers[0] / list_numbers[1]
        except ZeroDivisionError:
            return "No se puede dividir entre 0"

    if str(result).endswith(".0"):
        result = int(result)
    # TODO: Terminar de implementar la notación científica
    # if len(str(result)) > 15:
    #     result = "{:.2e}".format(result)
    if "." in str(result) and not "%" in operators:
        result = str(result).replace(".", ",")
    else:
        result = str(result)
   
    print(result, "calculate")

    return result


def operator_function(operator):
    global list_numbers, secondary_screen
    if screen["text"].endswith(","):
        return
    elif "No" in screen["text"] or screen["text"].isalpha():
        screen["text"] = "Error"
    elif operator == "+/-":
        if screen["text"] != "0" and not "No" in screen["text"] and not screen["text"].isalpha():
            if "-" in screen["text"]:
                screen["text"] = screen["text"].replace("-", "")
            else:
                screen["text"] = "-" + screen["text"]
    elif operator == "%" and len(operators) == 0:
        screen["text"] = "0"
        if "=" in secondary_screen["text"]:
            secondary_screen["text"] = ""
    elif operator == "=" and len(operators) == 0:
        secondary_screen["text"] = screen["text"] + " " + operator + " "
    else:
        if "," in screen["text"]:
            list_numbers.append(float(screen["text"].replace(",", ".")))
        else:
            list_numbers.append(int(screen["text"]))
        print(list_numbers, "list_numbers cuando se agrega, operator_function")
        operators.append(operator)
        print(operators, "operators cuando se agrega, operator_function")

        if len(list_numbers) == 1:
            secondary_screen["text"] = screen["text"] + " " + operator + " "
            screen["text"] = "0"
        else:
            result = calculate()
            if result == "No se puede dividir entre 0":
                secondary_screen["text"] = ""
                screen.config(font=("Google Sans Mono", 15), text=result)
                list_numbers.clear()
                operators.clear()
            elif len(str(result)) > 10:
                screen["font"] = ("Google Sans Mono", 20)
            elif operator == "%":
                list_numbers[1] = result
                secondary_screen["text"] += str(result).replace(".", ",")
                screen["text"] = "0"
                operators.remove(operator)
            elif operator == "=":
                secondary_screen["text"] += screen["text"] + " " + operator + " "
                screen["text"] = str(result)
                list_numbers.clear()
                operators.clear()
            else:
                secondary_screen["text"] = str(result) + " " + operator + " "
                screen["text"] = "0"
                list_numbers = [result]
                operators.remove(operators[0])

            print(list_numbers, "list_numbers despues de calculate, operator_function")
            print(operators, "operators despues de calculate, operator_function")


window.mainloop()
