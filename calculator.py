import tkinter


from calculator_logic import Calculator
from theme_manager import ThemeManager


theme = ThemeManager()


window = tkinter.Tk()

window.iconbitmap("assets/Calculator_30001.ico")

window.geometry("340x390")
window.resizable(False, False)
window.title("Calculadora")

window.grid_rowconfigure(1, minsize=62)

window.configure(bg=theme.bg_window)


# region SCREENS
secondary_screen = tkinter.Label(
    window,
    fg=theme.fg,
    bg=theme.bg_window,
    text="",
    font=("Google Sans Mono", 14),
    anchor="e",
)
secondary_screen.grid(row=0, column=0, columnspan=5, sticky="nsew")

screen = tkinter.Label(
    window,
    bg=theme.bg_window,
    fg=theme.fg,
    text="0",
    font=("Google Sans Mono", 30),
    anchor="e",
)
screen.grid(row=1, column=1, columnspan=5, sticky="nsew")


calculator = Calculator(screen, secondary_screen)


# region BUTTONS
button_options = {
    "width": 7,
    "height": 1,
    "pady": 8,
    "fg": theme.fg,
    "bd": 1,
    "cursor": "hand2",
    "font": ("Google Sans Mono", 14),
    "activeforeground": theme.fg,
}

percentage = tkinter.Button(
    window,
    **button_options,
    bg=theme.bg_operators,
    text="%",
    command=lambda: calculator.operator_function("%"),
)
percentage.grid(row=2, column=1)

remove = tkinter.Button(
    window, **button_options, bg=theme.bg_operators, text="CE", command=lambda: calculator.clear_screen("CE")
)
remove.grid(row=2, column=2)

remove_all = tkinter.Button(
    window, **button_options, bg=theme.bg_operators, text="C", command=lambda: calculator.clear_screen("C")
)
remove_all.grid(row=2, column=3)

division = tkinter.Button(
    window,
    **button_options,
    text="/",
    command=lambda: calculator.operator_function("/"),
)
division.grid(row=2, column=4)

seven = tkinter.Button(
    window,
    **button_options,
    text="7",
    command=lambda: calculator.modifiying_screen("7"),
)
seven.grid(row=3, column=1)

eight = tkinter.Button(
    window,
    **button_options,
    text="8",
    command=lambda: calculator.modifiying_screen("8"),
)
eight.grid(row=3, column=2)

nine = tkinter.Button(
    window,
    **button_options,
    text="9",
    command=lambda: calculator.modifiying_screen("9"),
)
nine.grid(row=3, column=3)

multi = tkinter.Button(
    window,
    **button_options,
    text="x",
    command=lambda: calculator.operator_function("x"),
)
multi.grid(row=3, column=4)

four = tkinter.Button(
    window,
    **button_options,
    text="4",
    command=lambda: calculator.modifiying_screen("4"),
)
four.grid(row=4, column=1)

five = tkinter.Button(
    window,
    **button_options,
    text="5",
    command=lambda: calculator.modifiying_screen("5"),
)
five.grid(row=4, column=2)

six = tkinter.Button(
    window,
    **button_options,
    text="6",
    command=lambda: calculator.modifiying_screen("6"),
)
six.grid(row=4, column=3)

minus = tkinter.Button(
    window,
    **button_options,
    text="-",
    command=lambda: calculator.operator_function("-"),
)
minus.grid(row=4, column=4)

one = tkinter.Button(
    window,
    **button_options,
    text="1",
    command=lambda: calculator.modifiying_screen("1"),
)
one.grid(row=5, column=1)

two = tkinter.Button(
    window,
    **button_options,
    text="2",
    command=lambda: calculator.modifiying_screen("2"),
)
two.grid(row=5, column=2)

three = tkinter.Button(
    window,
    **button_options,
    text="3",
    command=lambda: calculator.modifiying_screen("3"),
)
three.grid(row=5, column=3)

plus = tkinter.Button(
    window,
    **button_options,
    text="+",
    command=lambda: calculator.operator_function("+"),
)
plus.grid(row=5, column=4)

plus_minus = tkinter.Button(
    window,
    **button_options,
    text="+/-",
    command=lambda: calculator.modifiying_screen("+/-"),
)
plus_minus.grid(row=6, column=1)

zero = tkinter.Button(
    window,
    **button_options,
    text="0",
    command=lambda: calculator.modifiying_screen("0"),
)
zero.grid(row=6, column=2)

dot = tkinter.Button(
    window,
    **button_options,
    text=",",
    command=lambda: calculator.modifiying_screen(","),
)
dot.grid(row=6, column=3)

equal = tkinter.Button(
    window,
    **button_options,
    bg="#DB9EE5",
    text="=",
    activebackground="#DB9EE5",
    command=lambda: calculator.operator_function("="),
)
equal.grid(row=6, column=4)

equal.bind("<Enter>", lambda event: event.widget.config(bg="#A174A8"))
equal.bind("<Leave>", lambda event: event.widget.config(bg="#DB9EE5"))


# region BUTTONS CONFIG
numbers_buttons = [
    seven,
    eight,
    nine,
    four,
    five,
    six,
    one,
    two,
    three,
    plus_minus,
    zero,
    dot,
]
operators_buttons = [percentage, remove, remove_all, division, multi, minus, plus]

for button in operators_buttons:
    button.config(bg=theme.bg_operators, activebackground=theme.actbg_operators)
    button.bind("<Enter>", theme.enter_operators_leave_numbers)
    button.bind("<Leave>", theme.enter_numbers_leave_operators)


for button in numbers_buttons:
    button.config(bg=theme.bg_numbers, activebackground=theme.actbg_numbers)
    button.bind("<Enter>", theme.enter_numbers_leave_operators)
    button.bind("<Leave>", theme.enter_operators_leave_numbers)


if __name__ == "__main__":
    window.mainloop()
