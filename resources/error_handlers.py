from models.interfaces import Output
from models.constants import OutputStatus


class ErrorHandlers:
    @staticmethod
    def handle_404(e) -> dict:
        return Output(
            output_status=OutputStatus.ERROR,
            output_message=f"{str(e)}",
        ).__dict__

    @staticmethod
    def handle_500(e) -> dict:
        return Output(
            output_status=OutputStatus.ERROR,
            output_message=f"{str(e)}",
        ).__dict__
