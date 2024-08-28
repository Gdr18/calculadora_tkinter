class Calculator:
    def __init__(self, screen, secondary_screen):
        self.list_numbers = []
        self.list_operators = []
        self.count = 1
        self.screen = screen
        self.secondary_screen = secondary_screen

    #region COMMON METHODS
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
        if "%" in self.list_operators:
            if self.list_operators[0] == "*":
                result = self.list_numbers[1] / 100
            else:
                result = self.list_numbers[0] * self.list_numbers[1] / 100
        elif self.list_operators[0] == "+":
            result = self.list_numbers[0] + self.list_numbers[1]
        elif self.list_operators[0] == "-":
            result = self.list_numbers[0] - self.list_numbers[1]
        elif self.list_operators[0] == "*":
            result = self.list_numbers[0] * self.list_numbers[1]
        elif self.list_operators[0] == "/":
            try:
                result = self.list_numbers[0] / self.list_numbers[1]
            except ZeroDivisionError:
                result = "No se puede dividir entre 0"

        if str(result).endswith(".0"):
            result = int(result)

        if "%" in self.list_operators:
            self.list_numbers[1] = result
            self.list_operators.remove(self.list_operators[1])
        elif not "=" in self.list_operators and result != "No se puede dividir entre 0":
            self.list_numbers[0] = result
            self.list_numbers.remove(self.list_numbers[1])
            self.list_operators.remove(self.list_operators[0])
        else:
            self.list_operators.clear()
            if result == "No se puede dividir entre 0":
                self.list_numbers.clear()
                return result
            self.list_numbers = [result]

        result = (
            "{:,}".format(float(result) if "." in str(result) else int(result))
            .replace(".", "#")
            .replace(",", ".")
            .replace("#", ",")
        )

        if len(result) > 20:
            result = result[:18] + "..."

        return result

    #region CALCULATOR LOGIC METHODS
    def clear_logic(self, option):
        self.clear_screen()
        if option == "C":
            self.secondary_screen["text"] = ""
            self.list_numbers.clear()
            self.list_operators.clear()
        elif "=" in self.secondary_screen["text"]:
            self.secondary_screen["text"] = ""

    def digit_logic(self, value):
        if value == "+/-":
            if (
                self.screen.get() != "0"
                and not "Error" in self.screen.get()
                and not "No" in self.screen.get()
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
            and not "=" in self.secondary_screen["text"]
        ):
            return
        elif (
            self.screen.get() == "0"
            or "Error" in self.screen.get()
            or "No" in self.screen.get()
            or "=" in self.secondary_screen["text"]
        ):
            if value == ",":
                self.screen.delete(0, "end")
                self.screen.insert(0, "0" + value)
                self.count += 1

            else:
                self.screen.delete(0, "end")
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
        if self.screen.get().endswith(","):
            return
        elif "No" in self.screen.get() or self.screen.get().isalpha():
            self.screen.delete(0, "end")
            self.screen.insert(0, "Error")
            self.checking_font()
        elif operator == "%" and len(self.list_operators) == 0:
            self.clear_screen()
            if "=" in self.secondary_screen["text"]:
                self.secondary_screen["text"] = ""
        elif operator == "=" and len(self.list_operators) == 0:
            self.list_operators.append(operator)
            self.clear_screen()
        else:
            if not len(self.list_numbers) == 2 and not (
                "=" in self.secondary_screen["text"] and len(self.list_numbers) == 1
            ):
                formatting_screen = self.screen.get().replace(".", "")
                if "," in self.screen.get():
                    self.list_numbers.append(float(formatting_screen.replace(",", ".")))
                else:
                    self.list_numbers.append(int(formatting_screen))

            self.list_operators.append(operator)

            if operator == "*":
                print_operator = "x"
            elif operator == "/":
                print_operator = "÷"
            else:
                print_operator = operator

            if len(self.list_numbers) == 1:
                self.secondary_screen["text"] = (
                    self.screen.get() + " " + print_operator + " "
                )
                self.clear_screen()
            else:
                result = self.calculate()
                if result == "No se puede dividir entre 0":
                    self.secondary_screen["text"] = ""
                    self.screen.delete(0, "end")
                    self.screen.insert(0, result)
                    self.screen["font"] = ("Google Sans Mono", 15)
                elif operator == "%":
                    self.secondary_screen["text"] += result
                    self.clear_screen()
                elif operator == "=":
                    if self.secondary_screen["text"][-1].isdigit():
                        self.secondary_screen["text"] += " " + print_operator + " "
                    else:
                        self.secondary_screen["text"] += (
                            self.screen.get() + " " + print_operator + " "
                        )
                    if len(self.secondary_screen["text"]) > 30:
                        self.secondary_screen["text"] = (
                            "..." + self.secondary_screen["text"][-27:]
                        )
                    self.screen.delete(0, "end")
                    self.screen.insert(0, result)
                    self.checking_font()
                else:
                    self.secondary_screen["text"] = result + " " + print_operator + " "
                    self.clear_screen()
