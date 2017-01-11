; Skriptování v GIMPu (3)
; Demonstrační příklad číslo 2

; Tato funkce je zavolána z dialogu vyvolaného uživatelem
; z grafického uživatelského rozhraní GIMPu.
(define (script-draw-selection
                             selected-image
                             selected-layer
                             selected-color
                             use-feather
                             feather-radius)
    ; vytvoření výběru ve tvaru čtverce
    (gimp-rect-select
        selected-image       ; obrázek v němž se výběr vytvoří
        150 150 100 100      ; rozměry výběru
        REPLACE              ; přepsání oblasti původního výběru
        use-feather feather-radius) ; rozmazání hranice výběru
    ; přidání dalšího výběru ve tvaru kružnice
    (gimp-ellipse-select
        selected-image       ; obrázek v němž se výběr vytvoří
        80 80 100 100        ; rozměry výběru
        ADD FALSE            ; přidání oblasti ke stávajícímu výběru
        use-feather feather-radius) ; rozmazání hranice výběru
    ; přidání dalšího výběru ve tvaru kružnice
    (gimp-ellipse-select
        selected-image       ; obrázek v němž se výběr vytvoří
        220 220 100 100      ; rozměry výběru
        ADD FALSE            ; přidání oblasti ke stávajícímu výběru
        use-feather feather-radius) ; rozmazání hranice výběru
    ; volba barvy v paletě
    (gimp-palette-set-background selected-color)
    ; vykreslení obrazce - jeho výplň
    (gimp-edit-fill selected-layer BG-IMAGE-FILL)
    ; zrušení výběru (lze vrátit pomocí CTRL+Z)
    (gimp-selection-none selected-image)
    ; přinutíme GIMP, aby finální obrázek vykreslil
    (gimp-displays-flush)  
)

; základní informace o skriptu a definice dialogu
; zobrazeného uživateli
(script-fu-register "script-draw-selection"
    _"_Draw selection"
    _"Draws geometric shape using selection to current layer"
    "Pavel Tisnovsky"
    "Pavel Tisnovsky"
    "2010-05-18"
    "RGB*, INDEXED*, GRAY*"
    SF-IMAGE       "Image"         0
    SF-DRAWABLE    "Drawable"      0
 
    SF-COLOR      _"Color"          "black"
    SF-TOGGLE     _"Feather"        FALSE
    SF-ADJUSTMENT _"Feather radius" '(10 1 100 1 10 0 0)
)

; registrace skriptu do menu
(script-fu-menu-register "script-draw-selection"
                         "&lt;Image&gt;/Root.cz")

; finito
