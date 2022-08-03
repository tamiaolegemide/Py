#!/bin/bash
url="/mnt/hgfs/share/nwsx8_txt/folder/"
cd $url
folder=`ls`
for file in $folder
do 
	zip $file".zip" -r $file"/" -P nanyuankeji
done

