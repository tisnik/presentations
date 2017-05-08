; Tato funkce je zavolána z dialogu vyvolaného uživatelem
; z grafického uživatelského rozhraní GIMPu.
(define (script-draw-circle image-width image-height radius selected-color background-color)
    (let*
        (
            ; vytvoření nového obrázku, jehož ID se uloží
            ; do proměnné nazvané "image"
            (image (car (gimp-image-new image-width image-height RGB)))

            ; vytvoření nové hladiny, jejíž ID se uloží
            ; do proměnné nazvané "layer"
            (layer (car (gimp-layer-new image image-width image-height RGB-IMAGE "Circle" 100 NORMAL-MODE))))

            ; přidání hladiny do vytvořeného obrázku
            (gimp-image-add-layer image layer 0)

            ; volba barvy v paletě
            (gimp-palette-set-background background-color)

            ; vykreslení obrazce - jeho výplň
            (gimp-edit-fill layer BG-IMAGE-FILL)

            ; vytvoření výběru ve tvaru kružnice
            (gimp-image-select-ellipse
                image                         ; obrázek v němž se výběr vytvoří
                CHANNEL-OP-REPLACE            ; přepsání oblasti původního výběru
                (- (/ image-width 2) radius)  ; levý horní roh výběru
                (- (/ image-height 2) radius)
                (* 2 radius) (* 2 radius))    ; rozměry výběru

            ; volba barvy v paletě
            (gimp-palette-set-background selected-color)

            ; vykreslení obrazce - jeho výplň
            (gimp-edit-fill layer BG-IMAGE-FILL)

            ; zrušení výběru (lze vrátit pomocí CTRL+Z)
            (gimp-selection-none image)

            ; zobrazení právě vytvořeného obrázku
            (gimp-display-new image)

            ; přinutíme GIMP, aby finální obrázek vykreslil
            (gimp-displays-flush)))

; základní informace o skriptu a definice dialogu
; zobrazeného uživateli
(script-fu-register "script-draw-circle"
                    "<Image>/Filters/Render/Pattern/Circle"
                    "Vytvori novy obrazek a v nem nakresli kruznici."
                    "Pavel Tisnovsky"
                    "Pavel Tisnovsky"
                    "2017-05-04"
                    ""
                    SF-ADJUSTMENT "Image width"  '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Image height" '(256 16 8192 16 64 0 1)
                    SF-ADJUSTMENT "Radius"       '(50 16 200 16 64 0 1)
                    SF-COLOR      "Color"       "yellow"
                    SF-COLOR      "Background"  "black")

; finito
