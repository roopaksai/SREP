from models.interfaces import AboutInput as Input


class Validator:
    def __init__(self, input: Input):
        self.input = input

    def validate_input(self) -> tuple:

        return True, ""
