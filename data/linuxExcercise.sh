#!/usr/bin/bash
echo -e "Download dataset \n"
curl https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/Iris_Data.csv -O

echo -e "Dataset size: $(du -h Iris_Data.csv) \n"
echo -e "Number of lines in Dataset: $(wc -c Iris_Data.csv)\n"
echo -e "fields in Dataset: $(sed -n 1p Iris_Data.csv)\n"

echo -e "Maximums and Minimums\n"

#The IFS( Internal Field Separator ) is a special shell variable used for word splitting 
#Set delimiter to comma to separete column titles
IFS=','

#Read the column titles into an array based on the delimiter
read -a columns <<< "$(sed -n 1p Iris_Data.csv)\n"

#remove last column by slicing the array
columns=("${columns[@]:0:4}") 

# get max and min val for each column
index=1
for col in "${columns[@]}";
do
  echo -e "Max $col: $(cut -d ',' -f $index < Iris_Data.csv | sort -nr | head -1)\n"
  echo -e "Min $col: $(cut -d ',' -f $index < Iris_Data.csv | sort -n | sed -n 3p)\n"
  echo -e "Average $col $(awk -F "," -v z=$index 'BEGIN {x=0; y=0}  {x=$z+x; y= y+1} END {print x/y}' Iris_Data.csv) \n"
  ((index++))
done

## create smaller sample file

head -140 Iris_Data.csv > sample.csv

## see diff between sample and original file
echo -e "See diffs between files\n"
diff -c Iris_Data.csv sample.csv

