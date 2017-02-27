
Funkce vyššího řádu
-------------------
let  sequence = range(10)
echo sequence
"
call map(sequence, {index, value -> value * 2})
echo sequence
"
call map(sequence, {index, value -> value * 2})
echo sequence
"
let  sequence2 = filter(copy(sequence), {index, value -> value % 2 == 0})
let  sequence3 = filter(copy(sequence), {index, value -> value % 3 == 0})
echo "sequence1=" sequence
echo "sequence2=" sequence2
echo "sequence3=" sequence3
