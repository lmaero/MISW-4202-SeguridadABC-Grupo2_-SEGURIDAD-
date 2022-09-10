from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)
api = Api(app)

def imprime_adios():
    print("adios mundo")

class VistaNotification(Resource):
    def post(self):
        alerta_tipo = request.json["alerta_tipo"]
        alerta_msg = request.json["alerta_msg"]
        response = {"tipo": alerta_tipo, "msg": alerta_msg}
        print('Nueva Alerta!!')
        print('Notificacion a POLICIA!!', response)
        print('Notificacion a FAMILIARES!!', response)
        return response, 200

api.add_resource(VistaNotification, '/notification/send')
