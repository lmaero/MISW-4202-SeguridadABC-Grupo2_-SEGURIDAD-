from datetime import datetime

from flask import request, Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

from general_queue import new_log_signal

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
        new_log_signal(alerta_msg, datetime.utcnow())
        return response, 200

    def get(self):
        return "OK", 200


api.add_resource(VistaNotification, '/notification/send')
