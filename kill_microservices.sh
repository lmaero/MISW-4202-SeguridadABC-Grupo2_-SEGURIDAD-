#!/bin/bash

process=`ps aux | grep -i --color flask | cut '-d ' -f 7- | cut -d ' ' -f 1`
#echo ${process}
for i in ${process}:
do
    echo "Process to killed ${i}"
    kill ${i}
    
done
