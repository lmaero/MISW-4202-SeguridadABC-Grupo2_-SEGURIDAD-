import requests
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)
api = Api(app)


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class VistaMonitor(Resource):
    def get(self):
        services = {}

        try:
            print('---------------------------------------------------------------')
            print(Bcolors.WARNING + "AUTHENTICATION MICROSERVICE" + Bcolors.ENDC)

            response_auth = requests.post(f"http://127.0.0.1:5001/auth/login", json={"usuario": "monitor"})
            print('Authentication Microservice Status:', response_auth.status_code)
            print('Authentication Microservice Content:', response_auth.content)
            services["Authentication Microservice Status"] = response_auth.status_code
        except BaseException as error:
            services["Authentication Microservice Status"] = 503
            print("Authentication microservice is not available\n", error)

        try:
            print('---------------------------------------------------------------')
            print(Bcolors.WARNING + "NOTIFICATION MICROSERVICE" + Bcolors.ENDC)

            response_notification = requests.post(f"http://127.0.0.1:5002/notification/send",
                                                  json={"alerta_tipo": "ALERTA", "alerta_msg": "¡ALERTA!"})
            print('Notification Microservice Status:', response_notification.status_code)
            print('Notification Microservice Content:', response_notification.content)
            services["Notification Microservice Status"] = response_notification.status_code
        except BaseException as error:
            print("Notification microservice is not available\n", error)

        try:
            print('---------------------------------------------------------------')
            print(Bcolors.WARNING + "SIGNAL CHECKER MICROSERVICE" + Bcolors.ENDC)

            response_signal_checker = requests.post(f"http://127.0.0.1:5004/signal/checker", json={"signal": True})
            print('SignalChecker Microservice Status:', response_signal_checker.status_code)
            print('SignalChecker Microservice Content:', response_signal_checker.content)
            services["SignalChecker Microservice Status"] = response_signal_checker.status_code
        except BaseException as error:
            print("SignalChecker microservice is not available\n", error)

        finally:
            print('---------------------------------------------------------------')
            json_services = jsonify(services)
            return json_services


api.add_resource(VistaMonitor, '/monitor/check_services')
