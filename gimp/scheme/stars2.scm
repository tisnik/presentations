; Funkce, která vytvoří nový obrázek o zadané velikosti.
; V obrázku bude jedna hladina nazvaná "Stars" a
; v této hladině bude vykreslena hvězdná obloha.
(define (script-fu-stars-2 width height stars)
    ; definice lokálních proměnných
    (let*
        (
            ; vytvoření nového obrázku, jehož ID se uloží
            ; do proměnné nazvané "image"
            (image (car (gimp-image-new width height RGB)))
            ; vytvoření nové hladiny, jejíž ID se uloží
            ; do proměnné nazvané "layer"
            (layer (car (gimp-layer-new image width height RGB-IMAGE "Stars" 100 NORMAL-MODE))))

        ; zákaz ukládání operací do zásobníku
        (gimp-image-undo-disable image)
        ; přidání hladiny do vytvořeného obrázku
        (gimp-image-add-layer image layer 0)

        ; změna barvy popředí a pozadí
        (gimp-palette-set-foreground '(255 255 0))
        (gimp-context-set-background '(0 0 40))

        ; vyplnění hladiny konstantní barvou
        (gimp-drawable-fill layer 1)  ;0 FG, 1 BG

        (do ((i 0 (+ i 1)))
            ((= i stars))
            (let* (
               (point (make-vector 2))
               (x (rand width))
               (y (rand height)))
               (vector-set! point 0 x)
               (vector-set! point 1 y)
               ; vykreslení hvězdy aktuálně nastavenou tužkou
               (gimp-pencil layer 2 point))
        ) ; end of loop

        ; zobrazení právě vytvořeného obrázku
        (gimp-display-new image)

        ; povolení ukládání operací do zásobníku
        (gimp-image-undo-enable image)))

; Registrace skriptu do prostředí grafického editoru GIMP
; a specifikace proměnných nastavitelných uživatelem,
; které se posléze přenesou jako parametry skriptu.
(script-fu-register "script-fu-stars-2"
                    "<Image>/Filters/Render/Pattern/Stars2"
                    "Vytvori obrazek s hvezdnou oblohou."
                    "Pavel Tisnovsky"
                    "Pavel Tisnovsky"
                    "2017-03-16"
                    ""
                    SF-ADJUSTMENT "Image width"  '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Image height" '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Stars"        '(250 10 2000 10 20 0 1)
)

; finito

