import os
from flask import request
from flask_restful import Resource

UPLOAD_FOLDER = "temp"

class Flashcards(Resource):
    def post(self):
        # Debugging: Check if 'file' is in request
        if 'file' not in request.files:
            print("DEBUG: 'file' not found in request.files")
            return {"message": "No file part in the request"}, 400

        file = request.files['file']

        # Debugging: Check if the file has a valid name
        if file.filename == '':
            print("DEBUG: File selected has an empty filename")
            return {"message": "No file selected"}, 400

        # Debugging: Print the file name
        print(f"DEBUG: File received with filename: {file.filename}")

        # Save the file in the temp folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        try:
            file.save(file_path)
            print(f"DEBUG: File saved at {file_path}")
            return {"message": f"File {file.filename} uploaded successfully", "path": file_path}, 200
        except Exception as e:
            print(f"DEBUG: Error occurred while saving file: {e}")
            return {"message": f"Error saving file: {str(e)}"}, 500
