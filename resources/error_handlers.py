from models.interfaces import Output
from models.constants import OutputStatus
from flask import jsonify

class ErrorHandlers:
    @staticmethod
    def handle_404(e) -> tuple:
        response = Output(
            output_status=OutputStatus.ERROR,
            output_message="Resource not found",
        ).__dict__
        return jsonify(response), 404

    @staticmethod
    def handle_500(e) -> tuple:
        response = Output(
            output_status=OutputStatus.ERROR,
            output_message="Internal server error",
        ).__dict__
        return jsonify(response), 500

    @staticmethod
    def handle_400(e) -> tuple:
        response = Output(
            output_status=OutputStatus.ERROR,
            output_message="Bad request",
        ).__dict__
        return jsonify(response), 400

    @staticmethod
    def handle_422(e) -> tuple:
        response = Output(
            output_status=OutputStatus.ERROR,
            output_message="Unprocessable entity",
        ).__dict__
        return jsonify(response), 422