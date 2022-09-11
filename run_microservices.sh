#!/bin/bash

cd flaskr/auth
flask run -p 5001 &
cd ..
cd notification
flask run -p 5002 &
cd ..
cd monitor
flask run -p 5003 &
cd ..
cd signal_checker
flask run -p 5004 &
cd ..
cd sensor
flask run -p 5005 &
