#!/bin/bash

python3=/usr/bin/python3
test_name=evaporation_speed_addit_test
min_val=0.5
max_val=0.8
step=0.02

for algo_type in MMAS CAS; do 
	for i in `seq $min_val $step $max_val`; do
		outputfile=./test_outputs/${test_name}_${algo_type}_out
 		i=`echo ${i}|tr ',' '.'`
		start=`date +%s`
		echo $i ${algo_type}
		printf $i, >> $outputfile
		$python3 ./main.py input LosAngeles Atlanta 7 30 100 1.0 5.0 $i 1 $algo_type 0 >> $outputfile
		end=`date +%s`
		echo `expr $end - $start` >> $outputfile
	done
done
