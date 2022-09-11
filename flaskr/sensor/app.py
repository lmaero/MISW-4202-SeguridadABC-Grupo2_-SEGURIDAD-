import random
from datetime import datetime

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

import general_queue as gq

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)
api = Api(app)


class VistaSensor(Resource):
    def post(self):
        sensor_criticality = random.randint(0, 5)
        gq.receive_sensor(sensor_criticality)
        gq.new_log_signal("Señal recibida del sensor con criticidad: {}".format(sensor_criticality), datetime.utcnow())
        return sensor_criticality, 200


api.add_resource(VistaSensor, '/sensor/send')
