#!/bin/bash 

max=$(ls TP/ | cut -d '_' -f 2 | sort -n | tail -n 1)
num=$((max + 25))
cd TP/
for i in $(seq $((max + 1)) $((num))); do
    touch "junior_$i"
done