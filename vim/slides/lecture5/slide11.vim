
" ---------------------------------------------
" Vim Script #10
" ---------------------------------------------
" Usage of Vim pseudovariables
" 
nmap ]] :let &tabstop += 1<CR>
nmap [[ :let &tabstop -= &tabstop > 1 ? 1 : 0<CR>
