#!/bin/bash

mac='Darwin'
os_name=`uname`

if [[ ${os_name} == ${mac} ]];
then
    process=$(ps aux | grep -i --color flask | cut '-d ' -f 7- | cut -d ' ' -f 1)
else
    process=$(ps aux | grep -i --color flask | cut '-d ' -f 6- | cut -d ' ' -f 1)
fi

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
