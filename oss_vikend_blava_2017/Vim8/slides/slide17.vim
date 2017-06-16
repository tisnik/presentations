
Výpis všech konstant a proměnných Vimu
--------------------------------------
echo v:
" 
let vars = v:
for item in keys(vars)
    echo item
    echo vars[item]
    echo "----------------"
endfor
