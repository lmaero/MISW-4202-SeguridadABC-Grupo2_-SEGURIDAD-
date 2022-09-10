#!/bin/bash

process=$(ps aux | grep -i --color flask | cut '-d ' -f 7- | cut -d ' ' -f 1)

for i in ${process}:; do
    if [[ ${i} == *":"* ]];
    then        
        process_id=`echo ${i} |cut -d ':' -f 1`
        echo "Process id to kill ${process_id}"
        kill ${process_id}
    else
        echo "Process id to kill ${i}"
        kill ${i}
    fi
done
