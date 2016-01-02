" Detection if the interface between Vim and selected programming
" language is provided or not.

function! SupportForLanguage(languageName)
    echo "Support for language " . a:languageName . ":"
    if has(a:languageName)
        echo "provided"
    else
        echo "absent"
    end
endfunction

let s:langs=["Python", "Python3", "Perl", "Tcl", "mzscheme", "Lua", "Ruby"]

for lang in s:langs
    call SupportForLanguage(lang)
endfor

