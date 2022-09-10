#!/bin/bash

mac='Darwin'
os_name=$(uname)

# Obtener el tipo de sistema operativo
if [[ ${os_name} == ${mac} ]]; then
  process=$(ps aux | grep -i --color flask | cut '-d ' -f 7- | cut -d ' ' -f 1)
  if [[ ${process} == *":"* || -z "${process}"  ]]; then
    process=$(ps aux | grep -i --color "flask run -p 5001" | cut '-d ' -f 6- | cut -d ' ' -f 1)
  fi
else
  process=$(ps aux | grep -i --color flask | cut '-d ' -f 6- | cut -d ' ' -f 1)
fi

# Extrae el process id de cada microservicio y lo termina
for i in ${process}:; do
  if [[ ${i} == *":"* ]]; then
    process_id=$(echo ${i} | cut -d ':' -f 1)
    echo "Process id killed ${process_id}"
    kill ${process_id}
  else
    echo "Process id killed ${i}"
    kill ${i}
  fi
done
