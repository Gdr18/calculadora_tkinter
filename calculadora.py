import tkinter
import winreg


def is_dark_mode():
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(
            registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        )
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        winreg.CloseKey(key)
        return value == 0
    except:
        return False


if is_dark_mode():
    bg_window = "#221F21"
    bg_numbers = "#3E3A3B"
    bg_operators = "#353132"
    fg = "#ffffff"
else:
    bg_window = "#F3F3F3"
    bg_numbers = "#FFFFFF"
    bg_operators = "#F9F9F9"
    fg = "#000000"


def enter_operators_focus_leave_numbers(event):
    if is_dark_mode():
        event.widget["background"] = "#3E3A3B"
    else:
        event.widget["background"] = "#FFFFFF"

def enter_numbers_focus_leave_operators(event):
    if is_dark_mode():
        event.widget["background"] = "#353132"
    else:
        event.widget["background"] = "#F9F9F9"

def hover_operators(operators):
    for button in operators:
        button.bind("<Enter>", enter_operators_focus_leave_numbers)
        # button.bind("<Button-1>", enter_operators_focus_leave_numbers)
        button.bind("<Leave>", enter_numbers_focus_leave_operators)


def hover_numbers(numbers):
    for button in numbers:
        button.bind("<Enter>", enter_numbers_focus_leave_operators)
        # button.bind("<Button-1>", enter_numbers_focus_leave_operators)
        button.bind("<Leave>", enter_operators_focus_leave_numbers)


window = tkinter.Tk()

window.iconbitmap("assets/Calculator_30001.ico")

window.geometry("340x390")
window.resizable(False, False)
window.title("Calculadora")

window.grid_rowconfigure(1, minsize=62)

window.configure(bg=bg_window)

# region SCREENS
secondary_screen = tkinter.Label(
    window,
    fg=fg,
    bg=bg_window,
    text="",
    font=("Google Sans Mono", 14),
    anchor="e",
)
secondary_screen.grid(row=0, column=0, columnspan=5, sticky="nsew")

screen = tkinter.Label(
    window,
    bg=bg_window,
    fg=fg,
    text="0",
    font=("Google Sans Mono", 30),
    anchor="e",
)
screen.grid(row=1, column=1, columnspan=5, sticky="nsew")

# region BUTTONS
button_options = {
    "width": 7,
    "height": 1,
    "pady": 8,
    "fg": fg,
    "bd": 1,
    "cursor": "hand2",
    "font": ("Google Sans Mono", 14),
}

percentage = tkinter.Button(
    window,
    **button_options,
    bg=bg_operators,
    text="%",
    command=lambda: operator_function("%")
)
percentage.grid(row=2, column=1)

remove = tkinter.Button(
    window, **button_options, bg=bg_operators, text="CE", command=lambda: clear("CE")
)
remove.grid(row=2, column=2)

remove_all = tkinter.Button(
    window, **button_options, bg=bg_operators, text="C", command=lambda: clear("C")
)
remove_all.grid(row=2, column=3)

division = tkinter.Button(
    window,
    **button_options,
    bg=bg_operators,
    text="/",
    command=lambda: operator_function("/")
)
division.grid(row=2, column=4)

seven = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="7",
    command=lambda: number_function("7")
)
seven.grid(row=3, column=1)

eight = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="8",
    command=lambda: number_function("8")
)
eight.grid(row=3, column=2)

nine = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="9",
    command=lambda: number_function("9")
)
nine.grid(row=3, column=3)

multi = tkinter.Button(
    window,
    **button_options,
    bg=bg_operators,
    text="x",
    command=lambda: operator_function("x")
)
multi.grid(row=3, column=4)

four = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="4",
    command=lambda: number_function("4")
)
four.grid(row=4, column=1)

five = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="5",
    command=lambda: number_function("5")
)
five.grid(row=4, column=2)

six = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="6",
    command=lambda: number_function("6")
)
six.grid(row=4, column=3)

minus = tkinter.Button(
    window,
    **button_options,
    bg=bg_operators,
    text="-",
    command=lambda: operator_function("-")
)
minus.grid(row=4, column=4)

one = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="1",
    command=lambda: number_function("1")
)
one.grid(row=5, column=1)

two = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="2",
    command=lambda: number_function("2")
)
two.grid(row=5, column=2)

three = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="3",
    command=lambda: number_function("3")
)
three.grid(row=5, column=3)

plus = tkinter.Button(
    window,
    **button_options,
    bg=bg_operators,
    text="+",
    command=lambda: operator_function("+")
)
plus.grid(row=5, column=4)

plus_minus = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="+/-",
    command=lambda: operator_function("+/-")
)
plus_minus.grid(row=6, column=1)

zero = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text="0",
    command=lambda: number_function("0")
)
zero.grid(row=6, column=2)

dot = tkinter.Button(
    window,
    **button_options,
    bg=bg_numbers,
    text=".",
    command=lambda: number_function(",")
)
dot.grid(row=6, column=3)

equal = tkinter.Button(
    window,
    **button_options,
    bg="#DB9EE5",
    text="=",
    command=lambda: operator_function("=")
)
equal.grid(row=6, column=4)
equal.bind("<Enter>", lambda event: event.widget.config(bg="#A174A8"))
# equal.bind("<Button-1>", lambda event: event.widget.config(bg="#DB9EE5"))
equal.bind("<Leave>", lambda event: event.widget.config(bg="#DB9EE5"))


numbers = [seven, eight, nine, four, five, six, one, two, three, plus_minus, zero, dot]
operators = [percentage, remove, remove_all, division, multi, minus, plus]
hover_numbers(numbers)
hover_operators(operators)

list_numbers = []
operators = []


# region FUNCTIONS
def clear(option):
    screen.config(font=("Google Sans Mono", 30), text="0")
    if option == "C":
        secondary_screen["text"] = ""
        list_numbers.clear()
        operators.clear()
    elif "=" in secondary_screen["text"]:
        secondary_screen["text"] = ""


def number_function(number):
    if number == "+/-":
        if screen["text"] != "0":
            if "-" in screen["text"]:
                screen["text"] = screen["text"].replace("-", "")
            else:
                screen["text"] = "-" + screen["text"]
            if screen["text"].endswith("..."):
                list_numbers[0] = -1 * list_numbers[0]
    elif len(screen["text"]) >= 20 or (
        "," in screen["text"] and number == "," and not "=" in secondary_screen["text"]
    ):
        return
    elif (
        screen["text"] == "0"
        or "Error" in screen["text"]
        or "No" in screen["text"]
        or "=" in secondary_screen["text"]
    ):
        if number == ",":
            screen["text"] = "0" + number
        else:
            screen["text"] = number
    else:
        screen["text"] += number

    if "=" in secondary_screen["text"]:
        secondary_screen["text"] = ""

    if len(screen["text"]) > 13:
        screen["font"] = ("Google Sans Mono", 20)
    else:
        screen["font"] = ("Google Sans Mono", 30)


def calculate():
    global list_numbers
    if "%" in operators:
        result = list_numbers[1] / 100
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
            result = "No se puede dividir entre 0"

    if str(result).endswith(".0"):
        result = int(result)

    if "%" in operators:
        list_numbers[1] = result
        operators.remove(operators[1])
    elif not "=" in operators and result != "No se puede dividir entre 0":
        list_numbers[0] = result
        list_numbers.remove(list_numbers[1])
        operators.remove(operators[0])
    else:
        operators.clear()
        if result == "No se puede dividir entre 0":
            list_numbers.clear()
            return result
        list_numbers = [result]

    if "." in str(result):
        result = str(result).replace(".", ",")
    elif len(str(result)) > 20:
        result = str(result)[:18] + "..."
    else:
        result = str(result)

    if len(result) > 10:
        screen["font"] = ("Google Sans Mono", 20)

    print(result, "calculate")

    return result


def operator_function(operator):
    global list_numbers, secondary_screen
    if screen["text"].endswith(","):
        return
    elif "No" in screen["text"] or screen["text"].isalpha():
        screen["text"] = "Error"
    elif operator == "%" and len(operators) == 0:
        screen["text"] = "0"
        if "=" in secondary_screen["text"]:
            secondary_screen["text"] = ""
    elif (
        (operator == "=" and len(operators) == 0)
        or screen["text"].endswith("...")
        or ("=" in secondary_screen["text"] and len(list_numbers) != 0)
    ):
        secondary_screen["text"] = screen["text"] + " " + operator + " "
        if operator != "=":
            operators.append(operator)
            screen["text"] = "0"
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
            elif operator == "%":
                secondary_screen["text"] += result
                screen["text"] = "0"
            elif operator == "=":
                secondary_screen["text"] += screen["text"] + " " + operator + " "
                if len(secondary_screen["text"]) > 30:
                    secondary_screen["text"] = "..." + secondary_screen["text"][-27:]
                screen["text"] = result
            else:
                secondary_screen["text"] = result + " " + operator + " "
                screen["text"] = "0"

            print(list_numbers, "list_numbers despues de calculate, operator_function")
            print(operators, "operators despues de calculate, operator_function")


window.mainloop()
