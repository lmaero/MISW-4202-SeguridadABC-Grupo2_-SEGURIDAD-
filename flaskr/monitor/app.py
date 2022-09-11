import threading
from datetime import datetime

import requests
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api, Resource

from general_queue import new_log_monitor

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


def check_microservices():
    requests.get('http://localhost:5003/monitor/check_services')


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


class VistaMonitor(Resource):
    def get(self):
        services = {}

        try:
            print('---------------------------------------------------------------')
            print(Bcolors.WARNING + "AUTHENTICATION MICROSERVICE" + Bcolors.ENDC)
            response_auth = requests.get(f"http://127.0.0.1:5001/auth/login")
            print("Status: ", response_auth.status_code, "Content: ", response_auth.content)
            services["Authentication Microservice Status"] = response_auth.status_code
            new_log_monitor("Authentication", response_auth.status_code, datetime.utcnow())
        except BaseException as error:
            services["Authentication Microservice Status"] = 503
            print("Authentication microservice is not available\n", error)
            new_log_monitor("Authentication", 503, datetime.utcnow())

        try:
            print('---------------------------------------------------------------')
            print(Bcolors.WARNING + "NOTIFICATION MICROSERVICE" + Bcolors.ENDC)
            response_notification = requests.get(f"http://127.0.0.1:5002/notification/send")
            print("Status: ", response_notification.status_code, "Content: ", response_notification.content)
            services["Notification Microservice Status"] = response_notification.status_code
            new_log_monitor("Notification", response_notification.status_code, datetime.utcnow())
        except BaseException as error:
            print("Notification microservice is not available\n", error)
            new_log_monitor("Notification", 503, datetime.utcnow())

        try:
            print('---------------------------------------------------------------')
            print(Bcolors.WARNING + "SIGNAL CHECKER MICROSERVICE" + Bcolors.ENDC)
            response_signal_checker = requests.get(f"http://127.0.0.1:5004/signal/checker")
            print("Status: ", response_signal_checker.status_code, "Content: ", response_signal_checker.content)
            services["SignalChecker Microservice Status"] = response_signal_checker.status_code
            new_log_monitor("SignalChecker", response_signal_checker.status_code, datetime.utcnow())
        except BaseException as error:
            print("SignalChecker microservice is not available\n", error)
            new_log_monitor("SignalChecker", 503, datetime.utcnow())

        finally:
            print('---------------------------------------------------------------')
            json_services = jsonify(services)
            return json_services


api.add_resource(VistaMonitor, '/monitor/check_services')
set_interval(check_microservices, 10)
