from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.controller import *
from resources.error_handlers import ErrorHandlers


app = Flask(__name__)
api = Api(app)
CORS(app)

# Resources
api.add_resource(AboutService, "/about")
api.add_resource(FlashcardsService, "/upload")

# Error handlers
app.register_error_handler(404, ErrorHandlers.handle_404)
app.register_error_handler(500, ErrorHandlers.handle_500)


if __name__ == "__main__":
    app.run(debug=True)
