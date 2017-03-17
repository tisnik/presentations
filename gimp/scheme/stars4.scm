; Funkce, která vytvoří nový obrázek o zadané velikosti.
; V obrázku bude jedna hladina nazvaná "Stars" a
; v této hladině bude vykreslena hvězdná obloha.
(define (script-fu-stars-4 width height stars1 stars2 stars3)
    ; definice lokálních proměnných
    (let*
        (
            ; vytvoření nového obrázku, jehož ID se uloží
            ; do proměnné nazvané "image"
            (image (car (gimp-image-new width height RGB)))
            ; vytvoření nové hladiny, jejíž ID se uloží
            ; do proměnné nazvané "layer"
            (layer (car (gimp-layer-new image width height RGB-IMAGE "Stars" 100 NORMAL-MODE)))
            ; pole s uloženými RGB hodnotami pixelu
            (pixel (cons-array 3 'byte)))

        ; barva vykreslovanych hvezd
        (aset pixel 0 255)
        (aset pixel 1 255)
        (aset pixel 2 50)

        ; zákaz ukládání operací do zásobníku
        (gimp-image-undo-disable image)
        ; přidání hladiny do vytvořeného obrázku
        (gimp-image-add-layer image layer 0)

        ; změna barvy popředí a pozadí
        (gimp-palette-set-foreground '(255 255 255))
        (gimp-context-set-background '(0 0 40))

        ; vyplnění hladiny konstantní barvou
        (gimp-drawable-fill layer 1)  ;0 FG, 1 BG

        (define (pixel-1x1 layer x y pixel)
            (gimp-drawable-set-pixel layer x y 3 pixel))

        (define (pixel-2x2 layer x y pixel)
            (gimp-drawable-set-pixel layer x       y       3 pixel)
            (gimp-drawable-set-pixel layer (+ 1 x) y       3 pixel)
            (gimp-drawable-set-pixel layer x       (+ 1 y) 3 pixel)
            (gimp-drawable-set-pixel layer (+ 1 x) (+ 1 y) 3 pixel))

        (define (pixel-3x3 layer x y pixel)
            (gimp-drawable-set-pixel layer x       y       3 pixel)
            (gimp-drawable-set-pixel layer (+ 1 x) y       3 pixel)
            (gimp-drawable-set-pixel layer (+ 2 x) y       3 pixel)
            (gimp-drawable-set-pixel layer x       (+ y 1) 3 pixel)
            (gimp-drawable-set-pixel layer (+ 1 x) (+ y 1) 3 pixel)
            (gimp-drawable-set-pixel layer (+ 2 x) (+ y 1) 3 pixel)
            (gimp-drawable-set-pixel layer x       (+ y 2) 3 pixel)
            (gimp-drawable-set-pixel layer (+ 1 x) (+ y 2) 3 pixel)
            (gimp-drawable-set-pixel layer (+ 2 x) (+ y 2) 3 pixel))

        (do ((i 0 (+ i 1)))
            ((= i stars1))
            (let* (
               (x (rand width))
               (y (rand height)))
               ; vykreslení hvězdy
               (pixel-1x1 layer x y pixel))
        ) ; end of loop

        (do ((i 0 (+ i 1)))
            ((= i stars2))
            (let* (
               (x (rand (- width 1)))
               (y (rand (- height 1))))
               ; vykreslení hvězdy
               (pixel-2x2 layer x y pixel))
        ) ; end of loop

        (do ((i 0 (+ i 1)))
            ((= i stars3))
            (let* (
               (x (rand (- width 2)))
               (y (rand (- height 2))))
               ; vykreslení hvězdy
               (pixel-3x3 layer x y pixel))
        ) ; end of loop

        ; zobrazení právě vytvořeného obrázku
        (gimp-display-new image)

        ; povolení ukládání operací do zásobníku
        (gimp-image-undo-enable image)))

; Registrace skriptu do prostředí grafického editoru GIMP
; a specifikace proměnných nastavitelných uživatelem,
; které se posléze přenesou jako parametry skriptu.
(script-fu-register "script-fu-stars-4"
                    "<Image>/Filters/Render/Pattern/Stars4"
                    "Vytvori obrazek s hvezdnou oblohou."
                    "Pavel Tisnovsky"
                    "Pavel Tisnovsky"
                    "2017-03-16"
                    ""
                    SF-ADJUSTMENT "Image width"  '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Image height" '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Stars1"       '(200 10 1000 10 20 0 1)
                    SF-ADJUSTMENT "Stars2"       '(50  10 1000 10 20 0 1)
                    SF-ADJUSTMENT "Stars3"       '(5   10 1000 10 20 0 1)
)

; finito

