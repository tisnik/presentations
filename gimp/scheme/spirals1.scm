; Článek "Tvoříme skripty pro grafický editor GIMP (2)"
; Demonstrační příklad číslo 1

; Tato funkce je zavolána příkazem vyvolaným
; uživatelem z grafického uživatelského rozhraní GIMPu.
(define (script-fu-spirals-1
                             selected-image
                             selected-layer)

    ; definice lokálních proměnných
    (let*
        (
            ; konstanta - počet vrcholů křivky
            ; na jednu otočku spirály
            (vertexes-per-spin 300)

            ; počet prvků vektoru = (x1, y1, x2, y2)
            (npoint 4)

            ; vykreslovaná úsečka je představována vektorem
            ; (vektorem je v tomto kontextu myšlena datová
            ; struktura programovacího jazyka Scheme)
            (segment (make-vector 4 ))

            ; úhly zvětšující se pro každý další vykreslený úsek
            (alfa 0)
            (beta 0)

            ; konstanta - 2xPi
            (full-circle (* 3.1415927 2))

            ; počet vykreslených segmentů
            (step (/ full-circle vertexes-per-spin))

            ; počet otoček spirály
            (spins 3)

            ; vzdálenost vykreslovaného úseku od středu spirály
            (radius 20)
            (old-radius 20)

            ; změna vzdálenosti pro každý další úsek
            (radius-delta (/ (- 200 20) (* vertexes-per-spin spins 1)))
        )
        (gimp-undo-push-group-start selected-image)

        ; programová smyčka, v níž se vykreslí úsečkové segmenty
        ; ze kterých se skládá aproximace spirály
        (while (&lt;= alfa (* full-circle spins 1))
            (set! beta (+ alfa step))
            (set! radius (+ radius radius-delta))
            ; vypočet počáteční a koncové souřadice úsečky
            (vector-set! segment 0 (+ 200 (* old-radius (cos alfa ) )))
            (vector-set! segment 1 (+ 200 (* old-radius (sin alfa ) )))
            (vector-set! segment 2 (+ 200 (* radius (cos beta ) )))
            (vector-set! segment 3 (+ 200 (* radius (sin beta ) )))

            ; vykreslení úsečky štětcem
            (gimp-paintbrush selected-layer 100 npoint segment 0 10)

            ; přinutíme GIMP, aby obrázek průběžně vykresloval
            (gimp-displays-flush)
            ; přechod na další úsek
            (set! alfa beta)
            (set! old-radius radius)
        )
        ; uložíme stav obrázku na zásobník
        (gimp-undo-push-group-end selected-image) 
    )
    ; naposledy přinutíme GIMP, aby finální obrázek vykreslil
    (gimp-displays-flush)  
)


; základní informace o skriptu - v tomto případě se zde nenachází
; žádné měnitelné položky, tudíž není ani zobrazen dialog
(script-fu-register "script-fu-spirals-1"
    "_Spirals-1"
    "Renders spiral with three spins to current layer using current brush"
    "Pavel Tisnovsky"
    "Pavel Tisnovsky"
    "2010-05-11"
    "RGB*, INDEXED*, GRAY*"
    SF-IMAGE       "Image"         0
    SF-DRAWABLE    "Drawable"      0
)


; registrace skriptu do menu
(script-fu-menu-register "script-fu-spirals-1"
                         "&lt;Image&gt;/Root.cz")

; finito
