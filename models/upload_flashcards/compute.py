from models.interfaces import FlashcardsInput as Input, Output
from models.constants import Constants
import os


class Compute:
    def __init__(self, input: Input) -> None:
        self.input = input

    def compute(self) -> Output:
        file = self.input.file
        print(file, 'file')
        file_path = os.path.join(Constants.UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        return Output(
            output_details={'path': file_path},
            output_message='File uploaded successfully'
        )
