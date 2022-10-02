import random
from datetime import datetime

import jwt
from flask import Flask, request
from flask_jwt_extended import jwt_required, JWTManager
from flask_restful import Api, Resource

import general_queue as gq

app = Flask(_name_)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt_manager = JWTManager(app)
api = Api(app)


class VistaSensor(Resource):
    @jwt_required()
    def post(self):
        auth_header_token = request.headers["Authorization"].split(" ")[1]
        decoded_jwt = jwt.decode(
                            jwt=auth_header_token,
                            algorithms=['HS256'],
                            key="este_secreto_no_debe_de_saberse")
        user = decoded_jwt["sub"]
        print(user)
        sensor_criticality = random.randint(0, 5)
        gq.receive_sensor(sensor_criticality)
        gq.new_log_signal("Señal recibida del sensor con criticidad: {}".format(sensor_criticality), datetime.utcnow())
        return sensor_criticality, 200


api.add_resource(VistaSensor, '/sensor/send')
