#!/bin/bash
IFS=$'\n'
num=1
echo "$1 $2 $3"
while [ $num -le $1 ]
do
echo "outputs/csv/$num.html" >>outputs/csv/files
num=$(($num+1))
done

for i in `cat outputs/csv/files`
do
python script $i
done

sed -i 's/html/csv/g' outputs/csv/files

for i in `cat outputs/csv/files`
do
sed -i '19,$ d' $i
done

cat outputs/csv/$1.csv | awk -F ',' '{print $1}' >outputs/csv/names



i=1
while [ $i -le $1 ]
do
echo "$i/$2/$3" >> outputs/csv/monthlyreport
i=$(($i+1))
done


cat outputs/csv/monthlyreport | tr '\n' ',' >>outputs/csv/sortreport

echo "NAME,AVG,"$(cat outputs/csv/sortreport)"" >>outputs/csv/latest.csv


for i in `cat outputs/csv/names`
do
echo $i >>outputs/csv/newvalue
echo "" >>outputs/csv/newvalue
j=1
while [ $j -le $1 ]
do
field=`cat $j.csv | grep -i $i | awk -F ',' '{print $2}' | tr -d '"'`
if [ -z "$field" ]
then
echo "Null" >>outputs/csv/newvalue
else
echo $field >>outputs/csv/newvalue
fi
echo 
j=$(($j+1))
done
sed 'H;1h;$!d;x;s/\n/,/g' outputs/csv/newvalue >>outputs/csv/latest.csv

cat /dev/null >outputs/csv/newvalue
done 

rm -rf outputs/csv/newvalue outputs/csv/files outputs/csv/names outputs/csv/sortreport outputs/csv/monthlyreport
