# MISW-4202 Seguridad ABC

## Experimento 1 - Grupo 2

### Integrantes

- Diego Fernando Eslava Lozano
- Camilo Andrés Gálvez Vidal
- Alonso Daniel Cantú Trejo
- Luis Miguel Guzmán Pérez

### Paso a paso

1. Clonar repositorio con el comando:

   ```shell
   git clone https://github.com/lmaero/MISW-4202-SeguridadABC-Grupo2
   ```

2. Navegar al directorio clonado.
   ```shell
   cd MISW-4202-SeguridadABC-Grupo2
   ```

3. Dentro del directorio clonado, crear el entorno virtual con el comando
   ```shell
   python3 -m venv venv
   ```

4. Activar entorno virtual con el comando:
    - Windows:
   ```shell
   venv/Scripts/activate.bat
   ```
    - Linux o Mac:
   ```shell
   source venv/bin/activate
   ```

5. Instalar dependencias con el comando
   ```shell
   pip install -r requirements.txt
   ```

6. Establecer los permisos de ejecución en los siguientes archivos:
   ```shell
   chmod 777 kill_authentication.sh
   chmod 777 kill_microservices.sh
   chmod 777 run_microservices.sh
   ```

7. Correr en terminal el script run_microservices.sh con el comando
   ```shell
   ./run_microservices.sh
   ```

8. El componente monitor empezará a escribir un log cada 10 segundos con el estado de los servicios, consulte el
   archivo: `log_services.txt`, en este punto todos los servicios retornarán 200 (servicio disponible).

9. Opcional: Abrir Postman y hacer una solicitud GET al endpoint `http://localhost:5003/monitor/check_services` para
   comprobar el estado de los microservicios.

10. A través de Postman enviar una solicitud POST al microservicio sensor `http://localhost:5005/sensor/send`. La
    secuencia de eventos se describe a continuación:

- El sensor envía una señal con criticidad aleatoria en el rango (0-5) incluyente.
- La cola de mensajería implementada con la librería celery crea una nueva tarea que hace un solicitud POST al
  validador de señal (Signal Checker)
- Se registra en el log la criticidad de la señal y la fecha de recepción de la misma.
- Se registra en el log la validación de la señal.
- El validador de señal establece que si la criticidad es mayor a 3 deberá enviar una nueva tarea a la cola de
  mensajería, específicamente disparando una solicitud POST al microservicio Notification.
- El microservicio de notificación registra el mensaje de la alerta junto con el tiempo en el archivo
  `log_signals.txt`
- El llamado al servicio de emergencias es condicional dependiendo de la criticidad de la señal emitida por el sensor.

11. Para comprobar que todos los microservicios continúan funcionando así el servicio de autenticación no esté
    disponible, ejecutar en la terminal el script (kill_authentication.sh). Esto inhabilitará el servicio. Puede
    comprobarlo en el archivo `log_services.txt` (Está establecido un tiempo de 10 segundos entre cada ejecución del
    componente Monitor)

   ```shell
   ./kill_authentication.sh
   ```

12. Ejecute nuevamente el paso 10 para validar que las señales de los sensores se siguen recibiendo, analizando y
    notificando (en caso que sea necesario) con total normalidad, a pesar de que el servicio de autenticación no
    esté disponible.
