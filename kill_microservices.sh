#!/bin/bash

process=$(ps aux | grep -i --color flask | cut '-d ' -f 6- | cut -d ' ' -f 1)

for i in ${process}:; do
  echo "${i}"
  echo "Process to killed ${i}"
  kill ${i}

done
