
Seznamy
-------
let list1=[1, 2, 3, 4]
echo list1
" 
let two=2
let list2=[1, two, "3", "čtyři"]
echo list2
" 
let list3=[[11, 12, 13] , [21, 22, 23], [31, 32, 33]]
echo list3
" 
let first=list1[0]
echo first
" 
let list2[1]="xyzzy"
echo list2
" 
let list3=[[11, 12, 13] , [21, 22, 23], [31, 32, 33]]
echo list3[2][2]
" 
echo "Indexes are ok:"
echo get(list1, 1)
echo get(list1, 2)
" 
echo "Indexes are out of bounds:"
echo get(list1,-1)
echo get(list1, 4)
