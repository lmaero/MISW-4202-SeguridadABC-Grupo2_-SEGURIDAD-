import requests
from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')


@celery_app.task()
def receive_sensor(sensor_criticality):
    requests.post('http://localhost:5004/signal/checker', json={"signal": sensor_criticality})


@celery_app.task()
def send_notification(notification):
    requests.post('http://localhost:5002/notification/send',
                  json={"alerta_tipo": "Apertura de puerta", "alerta_msg": notification})


@celery_app.task()
def new_log_signal(event, date):
    with open('../../log_signals.txt', 'a+') as file:
        file.write('Event: {} \t- Date: {}\n'.format(event, date))


def new_log_monitor(service, status, date):
    with open('../../log_services.txt', 'a+') as file:
        file.write('Service: {} \t- Status: {} \t- Date: {}\n'.format(service, status, date))
