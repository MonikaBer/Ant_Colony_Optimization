#!/bin/bash

python3=/usr/bin/python3
test_name=ant_colony_size_test
min_val=1
max_val=46
step=5

for algo_type in MMAS CAS; do 
	for i in `seq $min_val $step $max_val`; do
		outputfile=./test_outputs/${test_name}_${algo_type}_out
 		i=`echo ${i}|tr ',' '.'`
		start=`date +%s`
		echo $i ${algo_type}
		printf $i, >> $outputfile
		$python3 ./main.py input LosAngeles Atlanta 7 $i 100 1.0 5.0 0.7 1 $algo_type >> $outputfile
		end=`date +%s`
		echo `expr $end - $start` >> $outputfile
	done
done
