#!/bin/bash


input_dir=$@

for path_file in `ls $inut_dir`;
do
	new_name=${path_file/'sbk10'/'sbk1067'}
	cp $path_file $input_dir"sb10k67/"$new_name
done
