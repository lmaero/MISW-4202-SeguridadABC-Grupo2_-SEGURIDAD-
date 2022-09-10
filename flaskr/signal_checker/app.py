import requests
from flask import Flask, request
from flask_restful import Api, Resource
import general_queue as gq

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "este_secreto_no_debe_de_saberse"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
api = Api(app)


class VistaSignalChecker(Resource):
    def post(self):
        signal = request.json["signal"]
        #gq.imprime_esto()
        gq.imprime_adios()
        if signal:            
            requests.post("http://127.0.0.1:5002/notification/send",
                          json={"alerta_tipo": "ALERTA", "alerta_msg": "¡ALERTA!"})
            print("Señal enviada a la cola de mensajería")
            return "", 200
        else:
            print("La señal de alarma fue validada y no representa ningún riesgo")
            return "", 200


api.add_resource(VistaSignalChecker, '/signal/checker')
