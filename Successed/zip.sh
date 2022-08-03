#!/bin/bash
function getdir(){
    for element in `ls $1`
    do
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
		zip -r $dir_or_file".zip" $dir_or_file -P nanyuankeji 
        fi
    done
}

root_dir="."
getdir $root_dir
