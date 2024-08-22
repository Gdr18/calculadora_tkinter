import winreg


class ThemeManager:
    def __init__(self):
        self.bg_window = "#F3F3F3"
        self.bg_numbers = "#FFFFFF"
        self.bg_operators = "#F9F9F9"
        self.actbg_operators = "#F9F9F9"
        self.actbg_numbers = "#FFFFFF"
        self.fg = "#000000"
        self.set_theme()

    def is_dark_mode(self):
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

    def set_theme(self):
        if self.is_dark_mode():
            self.bg_window = "#221F21"
            self.bg_numbers = "#3E3A3B"
            self.bg_operators = "#353132"
            self.actbg_operators = "#353132"
            self.actbg_numbers = "#3E3A3B"
            self.fg = "#ffffff"

    def enter_operators_leave_numbers(self, event):
        if self.is_dark_mode():
            event.widget["background"] = "#3E3A3B"
        else:
            event.widget["background"] = "#FFFFFF"


    def enter_numbers_leave_operators(self, event):
        if self.is_dark_mode():
            event.widget["background"] = "#353132"
        else:
            event.widget["background"] = "#F9F9F9"
