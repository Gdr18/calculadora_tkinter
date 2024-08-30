from decimal import Decimal, getcontext, ROUND_HALF_UP

class Calculator:
    def __init__(self, screen, secondary_screen):
        self.list_numbers = []
        self.list_operators = []
        self.count = 1
        self.screen = screen
        self.secondary_screen = secondary_screen

    # region COMMON METHODS
    def checking_font(self):
        if len(self.screen.get()) > 13:
            self.screen["font"] = ("Google Sans Mono", 20)
        else:
            self.screen["font"] = ("Google Sans Mono", 30)

    def clear_screen(self):
        self.screen.delete(0, "end")
        self.screen.insert(0, "0")
        self.count = 1
        self.checking_font()

    def formatting_screen_with_dots(self):
        text_without_dots = self.screen.get().replace(".", "")
        self.count -= self.screen.get().count(".")
        self.screen.delete(0, "end")
        self.screen.insert(0, "{:,}".format(int(text_without_dots)).replace(",", "."))
        self.count += "{:,}".format(int(text_without_dots)).replace(",", ".").count(".")

    def calculate(self):
        getcontext().prec = 28

        def format_result(result):
            if result.as_tuple().exponent < -2:
                result = result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            if str(result).endswith(".0"):
                result = int(result)
            formatted_result = (
                "{:,}".format(float(result) if "." in str(result) else int(result))
                .replace(".", "#")
                .replace(",", ".")
                .replace("#", ",")
            )
            if len(formatted_result) > 20:
                formatted_result = formatted_result[:18] + "..."
            return formatted_result

        try:
            if "%" in self.list_operators:
                if self.list_operators[0] == "*":
                    result = Decimal(self.list_numbers[1]) / Decimal(100)
                else:
                    result = Decimal(self.list_numbers[0]) * Decimal(self.list_numbers[1]) / Decimal(100)
            elif self.list_operators[0] == "+":
                result = Decimal(self.list_numbers[0]) + Decimal(self.list_numbers[1])
            elif self.list_operators[0] == "-":
                result = Decimal(self.list_numbers[0]) - Decimal(self.list_numbers[1])
            elif self.list_operators[0] == "*":
                result = Decimal(self.list_numbers[0]) * Decimal(self.list_numbers[1])
            elif self.list_operators[0] == "/":
                result = Decimal(self.list_numbers[0]) / Decimal(self.list_numbers[1])


            if "%" in self.list_operators:
                self.list_numbers[1] = result
                self.list_operators.remove(self.list_operators[1])
            elif (
                not "=" in self.list_operators
                and result != "No se puede dividir entre 0"
            ):
                self.list_numbers[0] = result
                self.list_numbers.remove(self.list_numbers[1])
                self.list_operators.remove(self.list_operators[0])
            else:
                self.list_operators.clear()
                if result == "No se puede dividir entre 0":
                    self.list_numbers.clear()
                    return result
                self.list_numbers = [result]

            return format_result(result)

        except ZeroDivisionError:
            self.list_numbers.clear()
            self.list_operators.clear()
            return "No se puede dividir entre 0"

    # region CALCULATOR LOGIC
    def clear_logic(self, option):
        self.clear_screen()
        if option == "C":
            self.secondary_screen["text"] = ""
            self.list_numbers.clear()
            self.list_operators.clear()
        elif "=" in self.secondary_screen["text"]:
            self.secondary_screen["text"] = ""
            self.list_numbers.clear()

    def digit_logic(self, value):
        if value == "+/-":
            if (
                self.screen.get() != "0"
                and "Error" not in self.screen.get()
                and "No" not in self.screen.get()
            ):
                if "-" in self.screen.get():
                    self.screen.delete(0)
                    self.count -= 1
                else:
                    screen_text = self.screen.get()
                    self.screen.delete(0, "end")
                    self.screen.insert(0, "-" + screen_text)
                    self.count += 1
                if self.screen.get().endswith("..."):
                    self.list_numbers[0] = -1 * self.list_numbers[0]
        elif len(self.screen.get()) >= 20 or (
            "," in self.screen.get()
            and value == ","
            and "=" not in self.secondary_screen["text"]
        ):
            return
        elif (
            self.screen.get() == "0"
            or "Error" in self.screen.get()
            or "No" in self.screen.get()
            or "=" in self.secondary_screen["text"]
        ):
            self.screen.delete(0, "end")
            if value == ",":
                self.screen.insert(0, "0" + value)
                self.count += 1
            else:
                self.screen.insert(0, value)
        else:
            self.screen.insert(self.count, value)
            self.count += 1
            if len(self.screen.get()) > 3 and not "," in self.screen.get():
                self.formatting_screen_with_dots()

        if "=" in self.secondary_screen["text"]:
            self.secondary_screen["text"] = ""
            self.list_numbers.clear()

        self.checking_font()

    def operator_logic(self, operator):
        screen_text = self.screen.get()

        if screen_text.endswith(","):
            return

        if "No" in screen_text or screen_text.isalpha():
            self.screen.delete(0, "end")
            self.screen.insert(0, "Error")
            self.checking_font()
            return

        if operator == "%" and not self.list_operators:
            self.clear_screen()
            if "=" in self.secondary_screen["text"]:
                self.secondary_screen["text"] = ""
            return

        if operator == "=" and not self.list_operators:
            self.secondary_screen["text"] = f"{screen_text} {operator} "
            return

        if len(self.list_numbers) < 2 and not (
            "=" in self.secondary_screen["text"] and len(self.list_numbers) == 1
        ):
            formatting_screen = screen_text.replace(".", "")
            self.list_numbers.append(float(formatting_screen.replace(",", ".")))

        self.list_operators.append(operator)
        print_operator = {"*": "x", "/": "÷"}.get(operator, operator)

        if len(self.list_numbers) == 1:
            self.secondary_screen["text"] = f"{screen_text} {print_operator} "
            self.clear_screen()
            return

        result = self.calculate()

        if result == "No se puede dividir entre 0":
            self.secondary_screen["text"] = ""
            self.screen.delete(0, "end")
            self.screen.insert(0, result)
            self.screen["font"] = ("Google Sans Mono", 15)
            return

        if operator == "%":
            self.secondary_screen["text"] += result
            self.clear_screen()
            return

        if operator == "=":
            if self.secondary_screen["text"][-1].isdigit():
                self.secondary_screen["text"] += f" {print_operator} "
            else:
                self.secondary_screen["text"] += f"{screen_text} {print_operator} "

            if len(self.secondary_screen["text"]) > 30:
                self.secondary_screen["text"] = (
                    f"...{self.secondary_screen['text'][-27:]}"
                )
            self.screen.delete(0, "end")
            self.screen.insert(0, result)
            self.checking_font()
            return

        self.secondary_screen["text"] = f"{result} {print_operator} "
        self.clear_screen()
