names=`find ../results/ -name *.log`
titles=`find ../results/ -name *.log | awk '{gsub(/results\//, ""); gsub(/\//, "_"); gsub(/\.\._/,"") ;print}'`

# for each (name, title) do
title='Sequential Full'; name=full; awk -v t="$title" 'BEGIN{print t}; /seconds time elapsed/ {gsub(",",".",$1); gsub(",", ".", $7); gsub("%", "/100", $7); print $1 "\t" $7 }' $name.log | python ../../ploter/ploter.py
#done
