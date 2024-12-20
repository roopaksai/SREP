from flask import request
from models.common import Common
from flask_restful import Resource
from models.constants import OutputStatus
from models.interfaces import FlashcardsInput, Output
from models.upload_flashcards.main import UploadFlashcards


class FlashcardsService(Resource):

    def get(self) -> dict:
        input = request.files
        print(input, 'input')
        if 'file' not in input:
            return "No file part"
        input = input['file']
        input = {"file": input}
        about = FlashcardsInput(**input)
        output = UploadFlashcards(about).process()

        return output.__dict__
