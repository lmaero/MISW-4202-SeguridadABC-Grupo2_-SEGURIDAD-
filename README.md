# MISW-4202 Seguridad ABC

## Experimento 1 - Grupo 2

### Integrantes

- Diego Fernando Eslava Lozano
- Camilo Andrés Gálvez Vidal
- Alonso Daniel Cantú Trejo
- Luis Miguel Guzmán Pérez

### Evidencia del experimento



### Colección de Postman
[Descargar colección Postman. Requests](https://github.com/lmaero/MISW-4202-SeguridadABC-Grupo2/blob/main/experimento.postman_collection.json)

### Paso a paso

1. Clonar repositorio con el comando:

   ```shell
   git clone https://github.com/lmaero/MISW-4202-SeguridadABC-Grupo2_-SEGURIDAD-.git
   ```

2. Navegar al directorio clonado.
   ```shell
   cd MISW-4202-SeguridadABC-Grupo2_-SEGURIDAD-
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

8. El componente monitor fue pausado para evitar logs innecesarios en consola para este experimento. En este punto 
   todos los servicios estarán disponibles, incluyendo el nuevo servicio de generación de tokens.

9. A través de Postman enviar una solicitud POST al microservicio tokens `http://localhost:5006/tokens`. Como 
   respuesta a esta solicitud deberá obtener un token de acceso, cómo se muestra en la imagen a continuación:

10. Copie y pegue este token de acceso, lo va a necesitar para realizar la siguiente solicitud, recuerde que el 
    token expira en 1 minuto, por lo tanto, la siguiente solicitud debe ser realizada inmediatamente.

11. A través de Postman envíe una solicitud POST al microservicio sensor `http://localhost:5005/sensor/send`. 
    Incluya en la pestaña Authorization de la solicitud el token copiado previamente. Seleccione Bearer Token en el 
    Tipo de autorización, y pegue el token copiado previamente en el campo Token. Como resultado de esta solicitud 
    obtendrá un número de criticidad de la señal, este es el comportamiento esperado del sistema cuando se usa un 
    usuario que se encuentre en base de datos y provea un token válido.

12. Para verificar el comportamiento del sistema con un token adulterado a modo de simulación de ataque, cambie 
    cualquier caracter del token previamente ingresado en el campo Token y envíe la solicitud nuevamente. En la 
    consola donde ejecutó los microservicios debería ver el mensaje "Se intentó usar un token de acceso adulterado", 
    como se muestra en la imagen a continuación:

13. Para verificar el comportamiento del sistema con un token válido pero un usuario no registrado en base de datos, 
    genere un nuevo token cambiando el "usuario" de la solicitud a cualquier cadena de caracteres a excepción de las 
    siguientes: "lmaero" o "acantu" o "cgalvez" o "abubu11". Repita la solicitud del paso 11, debería ver un mensaje 
    en consola con el nombre del usuario que usted ingresó y el mensaje "El usuario no fue encontrado en la DB", tal 
    como se muestra en las imágenes a continuación:
