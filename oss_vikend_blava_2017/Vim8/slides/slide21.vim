
Práce s registry Vimu
---------------------
let @"="foo bar"
let @*="xyzzy"
let @+=42
" 
reg
" 
" nyní vyzkoušejte 'Paste' v jiné aplikaci (Firefox, Gedit, atd.)

for x in range(10)
   let @" = x+1
   normal p
   normal o
endfor

