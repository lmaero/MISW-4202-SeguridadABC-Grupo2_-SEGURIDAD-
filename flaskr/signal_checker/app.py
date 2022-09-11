from datetime import datetime

from flask import Flask, request
from flask_restful import Api, Resource

from general_queue import new_log_signal, send_notification

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
api = Api(app)


class VistaSignalChecker(Resource):
    def post(self):
        sensor_criticality = request.json["signal"]
        if sensor_criticality > 3:
            new_log_signal('Señal validada', datetime.utcnow())
            send_notification('Llamando a servicios de emergencia...')
            return "", 200
        else:
            new_log_signal("La señal de alarma fue validada y no representa ningún riesgo", datetime.utcnow())
            return "", 200

    def get(self):
        return "OK", 200


api.add_resource(VistaSignalChecker, "/signal/checker")
