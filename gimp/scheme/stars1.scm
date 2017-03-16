; Funkce, která vytvoří nový obrázek o zadané velikosti.
; V obrázku bude jedna hladina nazvaná "Stars" a
; v této hladině bude vykreslena hvězdná obloha.
(define (script-fu-stars-1 width height stars)
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

        (do ((i 0 (+ i 1)))
            ((= i stars))
            (let* (
               (x (rand width))
               (y (rand height)))
               ; vykreslení žlutého pixelu/hvězdy
               (gimp-drawable-set-pixel layer x y 3 pixel))
        ) ; end of loop

        ; zobrazení právě vytvořeného obrázku
        (gimp-display-new image)

        ; povolení ukládání operací do zásobníku
        (gimp-image-undo-enable image)))

; Registrace skriptu do prostředí grafického editoru GIMP
; a specifikace proměnných nastavitelných uživatelem,
; které se posléze přenesou jako parametry skriptu.
(script-fu-register "script-fu-stars-1"
                    "<Image>/Filters/Render/Pattern/Stars1"
                    "Vytvori obrazek s hvezdnou oblohou."
                    "Pavel Tisnovsky"
                    "Pavel Tisnovsky"
                    "2017-02-19"
                    ""
                    SF-ADJUSTMENT "Image width"  '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Image height" '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Stars"        '(250 10 2000 10 20 0 1)
)

; finito

