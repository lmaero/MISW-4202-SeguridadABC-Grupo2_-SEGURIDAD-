from flask import request
from flask_jwt_extended import create_access_token, JWTManager
from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)
api = Api(app)


class VistaNotification(Resource):
    def post(self):
        alerta_tipo = request.json["alerta_tipo"]
        alerta_msg = request.json["alerta_msg"]
        response = {"tipo": alerta_tipo, "msg": alerta_msg}
        print('Nueva Notificación!!', response)
        return response, 200
    
api.add_resource(VistaNotification, '/notification/send')
