#!/bin/bash

python3=/usr/bin/python3
test_name=min_pheromone_test
min_val=0.1
max_val=4.6
step=0.5

for algo_type in MMAS CAS; do 
	for i in `seq $min_val $step $max_val`; do
		outputfile=./test_outputs/${test_name}_${algo_type}_out
 		i=`echo ${i}|tr ',' '.'`
		start=`date +%s`
		echo $i ${algo_type}
		printf $i, >> $outputfile
		$python3 ./main.py input LosAngeles Atlanta 7 30 100 1.0 5.0 0.7 1 $algo_type >> $outputfile
		end=`date +%s`
		echo `expr $end - $start` >> $outputfile
	done
done
