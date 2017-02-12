; Funkce, která vytvoří nový obrázek o zadané velikosti.
; V obrázku bude jedna hladina nazvaná "Hladina-1" a
; v této hladině bude vykreslena RGB paleta.
(define (script-fu-rgb-colors width height)
    ; definice lokálních proměnných
    (let*
        (
            ; vytvoření nového obrázku, jehož ID se uloží
            ; do proměnné nazvané "image"
            (image (car (gimp-image-new width height RGB)))
            ; vytvoření nové hladiny, jejíž ID se uloží
            ; do proměnné nazvané "layer"
            (layer (car (gimp-layer-new image width height RGB-IMAGE "Hladina-1" 100 NORMAL-MODE)))
            ; počitadla smyček
            (x 0)
            (y 0)
            ; pole s uloženými RGB hodnotami pixelu
            (pixel (cons-array 3 'byte))
        )

        ; zákaz ukládání operací do zásobníku
        (gimp-image-undo-disable image)

        ; přidání hladiny do vytvořeného obrázku
        (gimp-image-add-layer image layer 0)

        ; změna barvy popředí a pozadí
        (gimp-palette-set-foreground '(255 255 255))
        (gimp-context-set-background '(0 0 0))

        ; vyplnění hladiny konstantní barvou
        (gimp-drawable-fill layer 1)  ;0 FG, 1 BG

        ; vnější smyčka pro všechny řádky obrázku
        (while (< y height)
          ; nastavit počitadlo vnitřní smyčky
          (set! x 0)
          ; vnitřní smyčka pro všechny pixely ležící na řádku
          (while (< x width)
              (aset pixel 0 (* 256 (/ x width)))
              (aset pixel 1 (* 256 (/ y height)))
              (aset pixel 2 (* 256 (+ (/ x width) (/ y height))))
              ; vykreslení pixelu
              (gimp-drawable-set-pixel layer x y 3 pixel)
              ; zvýšit hodnotu počitadla vnitřní smyčky
              (set! x (+ x 1))
          )
          ; zvýšit hodnotu počitadla vnější smyčky
          (set! y (+ y 1))
        ) ; end of loop

        ; zobrazení právě vytvořeného obrázku
        (gimp-display-new image)

        ; povolení ukládání operací do zásobníku
        (gimp-image-undo-enable image)
    )
)

; Registrace skriptu do prostředí grafického editoru GIMP
; a specifikace proměnných nastavitelných uživatelem,
; které se posléze přenesou jako parametry skriptu.
(script-fu-register "script-fu-rgb-colors"
                    "<Image>/Filters/Render/Pattern/RGB colors"
                    "Vytvori obrazek s RGB paletou."
                    "Pavel Tisnovsky"
                    "Pavel Tisnovsky"
                    "2017-02-12"
                    ""
                    SF-ADJUSTMENT "Image width"  '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Image height" '(256 16 8192 16 64 0 1)
)

; finito

