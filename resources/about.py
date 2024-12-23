from flask import request
from models.common import Common
from flask_restful import Resource
from models.interfaces import AboutInput
from models.get_about.main import GetAbout


class AboutService(Resource):

    def get(self) -> dict:
        input = request.args
        input = Common.clean_dict(input, AboutInput)
        about = AboutInput(**input)
        output = GetAbout(about).process()

        return output.__dict__
