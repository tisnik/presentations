; Skriptování v GIMPu (4)
; Demonstrační příklad číslo 2

(define (script-fu-filter-samples2
                             selected-image
                             selected-layer)

  ; pomocná funkce která vytvoří kopii vybrané vrstvy
  (define (create-new-layer selected-layer)
    (car (gimp-layer-copy selected-layer FALSE))
  )

  (let* (
      ; vytvoření nových vrstev
      (new-layer-sobel   (create-new-layer selected-layer))
      (new-layer-sobel-h (create-new-layer selected-layer))
      (new-layer-sobel-v (create-new-layer selected-layer))
      (new-layer-roberts (create-new-layer selected-layer FALSE))
      (new-layer-prewitt (create-new-layer selected-layer FALSE))
      (new-layer-laplace (create-new-layer selected-layer FALSE))
    )

    ; pojmenování nově vytvořených vrstev
    (gimp-layer-set-name new-layer-sobel "Sobel filter in both directions")
    (gimp-layer-set-name new-layer-sobel-h "Sobel filter in horizontal direction")
    (gimp-layer-set-name new-layer-sobel-v "Sobel filter in vertical direction")
    (gimp-layer-set-name new-layer-roberts "Roberts filter")
    (gimp-layer-set-name new-layer-prewitt "Prewitt filter")
    (gimp-layer-set-name new-layer-laplace "Laplace filter")

    ; vrstvy je zapotřebí přidat do obrázku
    (gimp-image-add-layer selected-image new-layer-sobel 0)
    (gimp-image-add-layer selected-image new-layer-sobel-h 0)
    (gimp-image-add-layer selected-image new-layer-sobel-v 0)
    (gimp-image-add-layer selected-image new-layer-roberts 0)
    (gimp-image-add-layer selected-image new-layer-prewitt 0)
    (gimp-image-add-layer selected-image new-layer-laplace 0)

    ; aplikace filtrů na jednotlivé vrstvy
    (plug-in-sobel 1 selected-image new-layer-sobel   1 1 0)
    (plug-in-sobel 1 selected-image new-layer-sobel-h 1 0 0)
    (plug-in-sobel 1 selected-image new-layer-sobel-v 0 1 0)
    (plug-in-edge  1 selected-image new-layer-roberts 10 0 3)
    (plug-in-edge  1 selected-image new-layer-prewitt 10 0 1)
    (plug-in-edge  1 selected-image new-layer-laplace 10 0 5)
  )

  ; přinutíme GIMP, aby finální obrázek překreslil
  (gimp-displays-flush)
)

; základní informace o skriptu a definice dialogu
; zobrazeného uživateli
(script-fu-register
    "script-fu-filter-samples2"
    "Make samples of basic filters (2)"
    "Makes "
    "Pavel Tisnovsky"
    "Pavel Tisnovsky"
    "2010-05-25"
    "RGB*, GRAY*"
    SF-IMAGE    "Image"         0
    SF-DRAWABLE "Layer"         0)

; registrace skriptu do menu
(script-fu-menu-register "script-fu-filter-samples2"
                         "<Image>/Root.cz")

; finito

