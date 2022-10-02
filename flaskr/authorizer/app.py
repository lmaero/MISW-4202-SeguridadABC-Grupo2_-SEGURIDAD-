from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)
api = Api(app)


class VistaToken(Resource):
    def post(self):
        usuario = request.json["usuario"]
        token_de_acceso = create_access_token(identity=usuario)
        return token_de_acceso


api.add_resource(VistaToken, '/token')
