from datetime import datetime
from colorama import Fore, Style, init


class SimpleLogger:
    DEBUG = 10
    INFO = 20
    WARNING = 30
    DISABLED = 100

    def __init__(self, level=INFO, name: str | None = None):
        self.level = level
        self.name = name
        init()

    def set_level(self, level):
        self.level = level

    def _display(self, label, message, color):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        if self.name:
            label = self.name + "] [" + label
        print(f"{color}[{timestamp}] [{label}] {message}{Style.RESET_ALL}", flush=True)

    def debug(self, message):
        if self.level <= self.DEBUG:
            self._display("DEBUG", message, Fore.LIGHTGREEN_EX)

    def info(self, message):
        if self.level <= self.INFO:
            self._display("INFO", message, Fore.LIGHTBLUE_EX)

    def warning(self, message):
        if self.level <= self.WARNING:
            self._display("WARNING", message, Fore.LIGHTRED_EX)