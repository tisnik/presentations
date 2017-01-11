; Skriptování v GIMPu (4)
; Demonstrační příklad číslo 3

(define (script-fu-layers-and-filters
                             selected-image
                             selected-layer
                             blur-amount
                             edge-radius
                             apply-blur
                             apply-edge-filter
                             apply-inversion)
  (let* (
      ; vytvoření nové vrstvy
      (new-layer (car (gimp-layer-copy selected-layer FALSE))))

    ; pojmenování nově vytvořené vrstvy
    (gimp-layer-set-name new-layer "Nova hladina")

    ; vrstvu je zapotřebí přidat do obrázku
    (gimp-image-add-layer selected-image new-layer 0)

    ; aplikace prvního filtru - rozmazání obrázku
    (if (= apply-blur TRUE)
        (plug-in-gauss-rle 1 selected-image new-layer blur-amount 1 1))

    ; aplikace druhého filtru - detekce hran
    (if (= apply-edge-filter TRUE)
        (plug-in-edge TRUE selected-image new-layer edge-radius 0 0))

    ; inverze vrstvy
    (if (= apply-inversion TRUE)
        (gimp-invert new-layer))

  )

  ; přinutíme GIMP, aby finální obrázek překreslil
  (gimp-displays-flush)
)

; základní informace o skriptu a definice dialogu
; zobrazeného uživateli
(script-fu-register
    "script-fu-layers-and-filters"
    "Layers and filters"
    "Basic layers and filters manipulation"
    "Pavel Tisnovsky"
    "Pavel Tisnovsky"
    "2010-05-25"
    "RGB*, GRAY*"
    SF-IMAGE    "Image"         0
    SF-DRAWABLE "Layer"         0
    SF-VALUE    "Blur amount"  "5"
    SF-VALUE    "Edge radius"  "5"
    SF-TOGGLE   "Apply blur"   TRUE
    SF-TOGGLE   "Apply edge detection"  TRUE
    SF-TOGGLE   "Apply image inversion" TRUE
)

; registrace skriptu do menu
(script-fu-menu-register "script-fu-layers-and-filters"
                         "<Image>/Root.cz")

; finito

