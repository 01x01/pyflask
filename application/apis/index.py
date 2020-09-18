from flask_restx import Namespace, Resource

ns = Namespace("index")

@ns.route("/")
class Index(Resource):
    def get(self):
        return "Hello World"