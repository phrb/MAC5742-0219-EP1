IFS=' ' read -r -a names  <<< `find ../results/ -name *.log`
IFS=' ' read -r -a titles <<< `find ../results/ -name *.log | awk '{gsub(/results\//, ""); gsub(/\//, "_"); gsub(/\.\._/,""); gsub(/\.log/, ""); print}'`
for i in "${!titles[@]}"; do
    awk -v t="${titles[$i]}" 'BEGIN{print t}; /seconds time elapsed/ {gsub(",",".",$1); gsub(",", ".", $7); gsub("%", "/100", $7); print $1 "\t" $7 }' ${names[$i]} | python ploter.py
done
