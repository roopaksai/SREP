from flask import Flask
from flask_restful import Api, Resource
from resources.about import About
from resources.error_handlers import ErrorHandlers
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
class Home(Resource):
    def get(self):
        return {"status" : "success","data" : {"message": "Hello! This is my first Flask web app!"}}
api.add_resource(Home, "/")
api.add_resource(About, "/about")
app.register_error_handler(404, ErrorHandlers.handle_404)
app.register_error_handler(500, ErrorHandlers.handle_500)
if __name__ == "__main__":
    app.run(debug=True)
CORS(app)


