import random
from datetime import datetime

import jwt
from flask import Flask, request
from flask_jwt_extended import jwt_required, JWTManager
from flask_restful import Api, Resource
from jwt import InvalidSignatureError

import general_queue as gq
from general_queue import new_log_monitor

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt_manager = JWTManager(app)
api = Api(app)


class VistaSensor(Resource):
    @jwt_required()
    def post(self):
        try:
            auth_header_token = request.headers["Authorization"].split(" ")[1]
            decoded_jwt = jwt.decode(
                jwt=auth_header_token,
                algorithms=['HS256'],
                key="este_secreto_no_debe_de_saberse")
            user = decoded_jwt["sub"]
            print(user)

            # Simulación usuarios existentes en base de datos
            if user == "lmaero" or user == "acantu" or user == "cgalvez" or user == "abubu11":
                sensor_criticality = random.randint(0, 5)
                gq.receive_sensor(sensor_criticality)
                gq.new_log_signal("Señal recibida del sensor con criticidad: {}".format(sensor_criticality),
                                  datetime.utcnow())
                return sensor_criticality, 200
            else:
                print("El usuario no fue encontrado en la DB\n")
                new_log_monitor("Usuario no encontrado en la DB", 404, datetime.utcnow())

        except jwt.exceptions.InvalidSignatureError:
            print("Se intentó usar un token de acceso adulterado\n")
            new_log_monitor("Authorization", 401, datetime.utcnow())
        except jwt.exceptions.DecodeError:
            print("Se intentó usar un token de acceso adulterado\n")
            new_log_monitor("Authorization", 401, datetime.utcnow())


api.add_resource(VistaSensor, '/sensor/send')
