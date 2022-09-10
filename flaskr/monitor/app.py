from cmath import e

import requests
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)
api = Api(app)


class VistaMonitor(Resource):
    def get(self):
        try:
            print('---------------------------------------------------------------')
            response_auth = requests.post(f"http://127.0.0.1:5001/auth/login",
                                          json={"usuario": "monitor"})
            print('Authentication Microservice Status:', response_auth.status_code)
            print('Authentication Microservice Content:', response_auth.content)

            print('---------------------------------------------------------------')
            response_notification = requests.post(f"http://127.0.0.1:5002/notification/send",
                                                  json={"alerta_tipo": "ALERTA", "alerta_msg": "¡ALERTA!"})
            print('Notification Microservice Status:', response_notification.status_code)
            print('Notification Microservice Content:', response_notification.content)

            print('---------------------------------------------------------------')
            response_signal_checker = requests.post(f"http://127.0.0.1:5004/signal/checker",
                                                    json={"signal": True})
            print('SignalChecker Microservice Status:', response_signal_checker.status_code)
            print('SignalChecker Microservice Content:', response_signal_checker.content)

            print('---------------------------------------------------------------')
            services = {"Authentication Microservice Status": response_auth.status_code,
                        "Notification Microservice Status": response_notification.status_code,
                        "SignalChecker Microservice Status:": response_signal_checker.status_code,
                        }
            json_services = jsonify(services)

            return json_services
        except print('Error en el microservicio monitor:', e):
            pass


api.add_resource(VistaMonitor, '/monitor/check_services')
