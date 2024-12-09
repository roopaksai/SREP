from flask_restful import Resource
class About(Resource):
    def get(self):
        return {"status" : "sucess","data" : {"message": "SREP( Study Resources Enhancement Project ) is a web app that helps you in utilizing resources during exam preparation."}}
