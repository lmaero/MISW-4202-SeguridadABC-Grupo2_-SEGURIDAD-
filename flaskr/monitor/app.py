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
            response_auth = requests.post(f"http://127.0.0.1:5001/auth/login",
                                          json={"usuario": "monitor", "contraseña": "monitor"})
            print('Estado microservicio auth:', response_auth.status_code)
            print('Contenido respuesta microservicio auth:', response_auth.content)
            print('---------------------------------------------------------------')
            response_notification = requests.post(f"http://127.0.0.1:5002/notification/send",
                                                  json={"alerta_tipo": "ALERTA", "alerta_msg": "ALERTA!!!"})
            print('Estado microservicio notification:', response_notification.status_code)
            print('Contenido respuesta microservicio notification:', response_notification.content)
            print('---------------------------------------------------------------')

            services = {"Authentication Microservice Status": response_auth.status_code, "Notification Microservice "
                                                                                         "Status":
                response_notification.status_code}
            json_services = jsonify(services)

            return json_services
        except print('Error en el microservicio monitor:', e):
            pass


api.add_resource(VistaMonitor, '/monitor/check_services')
