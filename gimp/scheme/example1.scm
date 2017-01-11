; Skriptování v GIMPu (4)
; Demonstrační příklad číslo 1

(define (script-fu-filter-samples
                             selected-image
                             selected-layer)

  ; pomocná funkce která vytvoří kopii vybrané vrstvy
  (define (create-new-layer selected-layer)
    (car (gimp-layer-copy selected-layer FALSE))
  )

  (let* (
      ; vytvoření nových vrstev
      (new-layer-blur  (create-new-layer selected-layer))
      (new-layer-mblur (create-new-layer selected-layer FALSE))
      (new-layer-gauss (create-new-layer selected-layer FALSE))
      (new-layer-pixelize (create-new-layer selected-layer FALSE))
      (new-layer-pixelize2h (create-new-layer selected-layer FALSE))
      (new-layer-pixelize2v (create-new-layer selected-layer FALSE))
    )

    ; pojmenování nově vytvořených vrstev
    (gimp-layer-set-name new-layer-blur "Blur filter")
    (gimp-layer-set-name new-layer-mblur "Motion blur filter")
    (gimp-layer-set-name new-layer-gauss "Gauss blur filter")
    (gimp-layer-set-name new-layer-pixelize "Pixelize filter")
    (gimp-layer-set-name new-layer-pixelize2h "Pixelize2 horizontal filter")
    (gimp-layer-set-name new-layer-pixelize2v "Pixelize2 vertical filter")

    ; vrstvy je zapotřebí přidat do obrázku
    (gimp-image-add-layer selected-image new-layer-blur 0)
    (gimp-image-add-layer selected-image new-layer-mblur 0)
    (gimp-image-add-layer selected-image new-layer-gauss 0)
    (gimp-image-add-layer selected-image new-layer-pixelize 0)
    (gimp-image-add-layer selected-image new-layer-pixelize2h 0)
    (gimp-image-add-layer selected-image new-layer-pixelize2v 0)

    ; aplikace filtrů na jednotlivé vrstvy
    (plug-in-blur 1 selected-image new-layer-blur)
    (plug-in-mblur 1 selected-image new-layer-mblur 0 20 45 0 0)
    (plug-in-gauss-rle 1 selected-image new-layer-gauss 10 1 1)
    (plug-in-pixelize 1 selected-image new-layer-pixelize 8)
    (plug-in-pixelize2 1 selected-image new-layer-pixelize2h 10 1)
    (plug-in-pixelize2 1 selected-image new-layer-pixelize2v 1 10)
  )

  ; přinutíme GIMP, aby finální obrázek překreslil
  (gimp-displays-flush)
)

; základní informace o skriptu a definice dialogu
; zobrazeného uživateli
(script-fu-register
    "script-fu-filter-samples"
    "Make samples of basic filters"
    "Makes "
    "Pavel Tisnovsky"
    "Pavel Tisnovsky"
    "2010-05-25"
    "RGB*, GRAY*"
    SF-IMAGE    "Image"         0
    SF-DRAWABLE "Layer"         0)

; registrace skriptu do menu
(script-fu-menu-register "script-fu-filter-samples"
                         "<Image>/Root.cz")

; finito

