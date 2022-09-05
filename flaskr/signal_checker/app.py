from flask import request
from flask_jwt_extended import create_access_token
from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
api = Api(app)


class VistaAuth(Resource):
    def post(self):
        usuario = request.json["usuario"]
        token_de_acceso = create_access_token(identity=usuario)
        return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}
    
api.add_resource(VistaAuth, '/auth/login')
