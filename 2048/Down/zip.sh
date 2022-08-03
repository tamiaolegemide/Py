#/bin/bash

dir=`ls`
for i in $dir
do
	if [ -d $i ]
	then
	cd $i
	zip $i".zip"  *  -P nanyuankeji
	cd ../
	fi
done

mkdir ../zip
find ./ -name "*.zip" -exec mv {} ../zip/ \;
mv ../zip ./

