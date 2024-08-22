class Calculator:
    def __init__(self, screen, secondary_screen):
        self.list_numbers = []
        self.list_operators = []
        self.screen = screen
        self.secondary_screen = secondary_screen
    

    def checking_font(self):
        if len(self.screen["text"]) > 13:
            self.screen["font"] = ("Google Sans Mono", 20)
        else:
            self.screen["font"] = ("Google Sans Mono", 30)


    def clear_screen(self, option):
        self.screen.config(font=("Google Sans Mono", 30), text="0")
        if option == "C":
            self.secondary_screen["text"] = ""
            self.list_numbers.clear()
            self.list_operators.clear()
        elif "=" in self.secondary_screen["text"]:
            self.secondary_screen["text"] = ""
    

    def modifiying_screen(self, value):
        if value == "+/-":
            if self.screen["text"] != "0":
                if "-" in self.screen["text"]:
                    self.screen["text"] = self.screen["text"].replace("-", "")
                else:
                    self.screen["text"] = "-" + self.screen["text"]
                if self.screen["text"].endswith("..."):
                    self.list_numbers[0] = -1 * self.list_numbers[0]
        elif len(self.screen["text"]) >= 20 or (
        "," in self.screen["text"] and value == "," and not "=" in self.secondary_screen["text"]
        ):
            return
        elif (
            self.screen["text"] == "0"
            or "Error" in self.screen["text"]
            or "No" in self.screen["text"]
            or "=" in self.secondary_screen["text"]
        ):
            if value == ",":
                self.screen["text"] = "0" + value
            else:
                self.screen["text"] = value
        else:
            self.screen["text"] += value
            if len(self.screen["text"]) > 3 and not "," in self.screen["text"]:
                self.screen["text"] = self.screen["text"].replace(".", "")
                self.screen["text"] = "{:,}".format(int(self.screen["text"])).replace(",", ".")

        if "=" in self.secondary_screen["text"]:
            self.secondary_screen["text"] = ""
            self.list_numbers.clear()
        
        self.checking_font()


    def calculate(self):
        if "%" in self.list_operators:
            result = self.list_numbers[1] / 100
        elif self.list_operators[0] == "+":
            result = self.list_numbers[0] + self.list_numbers[1]
        elif self.list_operators[0] == "-":
            result = self.list_numbers[0] - self.list_numbers[1]
        elif self.list_operators[0] == "x":
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

        result = "{:,}".format(float(result) if "." in str(result) else int(result)).replace(".", "*").replace(",", ".").replace("*", ",")

        if len(result) > 20:
            result = result[:18] + "..."

        self.checking_font()

        print(result, "calculate")

        return result


    def operator_function(self, operator):
        if self.screen["text"].endswith(","):
            return
        elif "No" in self.screen["text"] or self.screen["text"].isalpha():
            self.screen["text"] = "Error"
        elif operator == "%" and len(self.list_operators) == 0:
            self.screen["text"] = "0"
            if "=" in self.secondary_screen["text"]:
                self.secondary_screen["text"] = ""
        elif (
            (operator == "=" and len(self.list_operators) == 0)
            or self.screen["text"].endswith("...")
            or ("=" in self.secondary_screen["text"] and len(self.list_numbers) != 0)
        ):
            self.secondary_screen["text"] = self.screen["text"] + " " + operator + " "
            if operator != "=":
                self.list_operators.append(operator)
                self.screen["text"] = "0"
        else:
            formatting_screen = self.screen["text"].replace(".", "")
            if "," in self.screen["text"]:
                self.list_numbers.append(float(formatting_screen.replace(",", ".")))
            else:
                self.list_numbers.append(int(formatting_screen))
            print(self.list_numbers, "list_numbers cuando se agrega, operator_function")
            self.list_operators.append(operator)
            print(self.list_operators, "list_operators cuando se agrega, operator_function")

            if len(self.list_numbers) == 1:
                self.secondary_screen["text"] = self.screen["text"] + " " + operator + " "
                self.screen["text"] = "0"
            else:
                result = self.calculate()
                if result == "No se puede dividir entre 0":
                    self.secondary_screen["text"] = ""
                    self.screen.config(font=("Google Sans Mono", 15), text=result)
                elif operator == "%":
                    self.secondary_screen["text"] += result
                    self.screen["text"] = "0"
                elif operator == "=":
                    self.secondary_screen["text"] += self.screen["text"] + " " + operator + " "
                    if len(self.secondary_screen["text"]) > 30:
                        self.secondary_screen["text"] = "..." + self.secondary_screen["text"][-27:]
                    self.screen["text"] = result
                else:
                    self.secondary_screen["text"] = result + " " + operator + " "
                    self.screen["text"] = "0"

                print(self.list_numbers, "list_numbers despues de calculate, operator_function")
                print(self.list_operators, "list_operators despues de calculate, operator_function")
