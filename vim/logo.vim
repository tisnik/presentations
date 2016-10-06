augroup __logo__
  au BufRead,BufNewFile vim.logo syn match zeleny_ctverec "+"
  au BufRead,BufNewFile vim.logo syn match ide "[#m\"]"
  au BufRead,BufNewFile vim.logo syn match okraj "[\\|/'_]"
  au BufRead,BufNewFile vim.logo hi  zeleny_ctverec ctermfg=lightgreen guifg=lightgreen ctermbg=black guibg=black
  au BufRead,BufNewFile vim.logo hi  okraj          ctermfg=white      guifg=white ctermbg=black guibg=black
  au BufRead,BufNewFile vim.logo hi  ide            ctermfg=yellow     guifg=yellow ctermbg=black guibg=black
  au BufRead,BufNewFile vim.logo hi  normal guifg=gray ctermbg=black guibg=black
augroup END

:e vim.logo

