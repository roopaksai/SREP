from models.interfaces import AboutInput as Input, Output


class Compute:
    def __init__(self, input: Input) -> None:
        self.input = input

    def compute(self) -> Output:

        data = {
            'message': 'SREP( Study Resources Enhancement Project ) is a web app that helps you in utilizing resources during exam preparation.'
        }

        return Output(
            output_details=data,
            output_message='About fetched successfully'
        )
