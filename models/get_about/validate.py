from models.interfaces import AboutInput as Input


class Validator:
    def __init__(self, input: Input):
        self.input = input

    def validate_input(self) -> tuple:
        if not self.input.file:
            return False, "No file provided"
        if not self.input.file.filename.endswith('.pdf'):
            return False, "Invalid file format. Only PDF allowed."
        return True, ""
