from flask import jsonify

class ErrorHandlers:
    @staticmethod
    def handle_404(e):
        return jsonify({"status": "error", "message": "Resource not found"}), 404

    @staticmethod
    def handle_500(e):
        return jsonify({"status": "error", "message": "Internal server error"}), 500
