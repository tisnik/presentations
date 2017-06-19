
Pseudoproměnné - proměnné prostředí
-----------------------------------
echo $HOME
echo $USER
echo $DISPLAY
 
Pseudoproměnné - konfigurační parametry
---------------------------------------
echo &backupdir
echo &encoding
echo &fileencoding
echo &fileformat
"
nmap ]] :let &tabstop += 1<CR>
nmap [[ :let &tabstop -= &tabstop > 1 ? 1 : 0<CR>
"
if &cp
    finish
end

