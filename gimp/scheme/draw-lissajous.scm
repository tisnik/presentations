; Funkce, která do existujícího obrázku vykreslí
; Lissajousův obrazec buď vybraným perem/tužkou nebo štětcem.
(define (script-fu-draw-lissajous selected-image selected-layer cx cy rx ry dx dy)
    ; definice lokálních proměnných
    (let*
        (
            ; vykreslovaná úsečka je představována vektorem
            ; (vektorem je zde myšlena datová struktura Scheme)
            (segment (make-vector 4 ))
            ; počet prvků vektoru
            (npoint 4)
            (alfa 0)
            (beta 0)
            ; 2xPi
            (full-circle (* 3.1415927 2))
            ; počet vykreslených segmentů
            (step (/ full-circle 200))
        )
        (gimp-undo-push-group-start selected-image)
        ; programová smyčka, v níž se vykreslí úsečkové segmenty
        ; ze kterých se skládá aproximace Lissajousovy křivky
        (while (<= alfa full-circle)
            (set! beta (+ alfa step))
            ; výpočet počáteční a koncové souřadnice úsečky
            (vector-set! segment 0 (+ cx (* rx (cos (* alfa dx )) )))
            (vector-set! segment 1 (+ cy (* ry (cos (* alfa dy )) )))
            (vector-set! segment 2 (+ cx (* rx (cos (* beta dx )) )))
            (vector-set! segment 3 (+ cy (* ry (cos (* beta dy )) )))

            ; na tomto místě je možné vybrat buď kreslení
            ; tužkou/perem (pencil) nebo štětcem (brush)
            ;(gimp-pencil selected-layer npoint segment )
            (gimp-paintbrush selected-layer 100 npoint segment 0 10)

            ; přinutíme GIMP, aby obrázek vykreslil
            (gimp-displays-flush)
            (set! alfa beta)
        )
        ; uložíme stav obrázku na zásobník
        (gimp-undo-push-group-end selected-image) 
    )
    ; naposledy přinutíme GIMP, aby obrázek vykreslil
    (gimp-displays-flush)  
)

; Registrace skriptu do prostředí grafického editoru GIMP
; a specifikace proměnných nastavitelných uživatelem,
; které se posléze přenesou jako parametry skriptu.
(script-fu-register "script-fu-draw-lissajous"
                    "<Image>/Filters/Render/Lissajous"
                    "Vykresli Lissajousuv obrazec na zaklade zadanych parametru"
                    "Pavel Tisnovsky"
                    "Pavel Tisnovsky"
                    "2017-02-11"
                    "RGB* GRAY* INDEXED*"
                    SF-IMAGE "The Image" 0
                    SF-DRAWABLE "The Layer" 0
                    SF-ADJUSTMENT "X center" '(200 0 999 1 10 0 1)
                    SF-ADJUSTMENT "Y center" '(200 0 999 1 10 0 1)
                    SF-ADJUSTMENT "X radius" '(160 0 999 1 10 0 1)
                    SF-ADJUSTMENT "Y radius" '(160 0 999 1 10 0 1)
                    SF-ADJUSTMENT "Xd" '(2 0 10 1 10 0 1)
                    SF-ADJUSTMENT "Yd" '(3 0 10 1 10 0 1)
)

; finito

