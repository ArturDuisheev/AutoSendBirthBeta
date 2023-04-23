from builtins import Exception


class ExceptionClass(Exception):
    list_exception = [
        KeyboardInterrupt,
        SystemExit

    ]

    def __init__(self, keyboard_exception, system_exception):
        self.keyboard_exception = keyboard_exception
        self.system_exception = system_exception

        for exception in ExceptionClass.list_exception:
            if isinstance(exception, type):
                if issubclass(exception, keyboard_exception):
                    self.keyboard_exception = exception
                if issubclass(exception, system_exception):
                    self.system_exception = exception
