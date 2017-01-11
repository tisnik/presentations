; Článek "Tvoříme skripty pro grafický editor GIMP (2)"
; Demonstrační příklad číslo 2

; Tato funkce musí akceptovat takový počet parametrů,
; aby odpovídal počtu ovládacích prvků zobrazených
; na dialogu.
(define (demo-box
        value
        adj1
        adj2
        image
        drawable
        toggle
        pattern
        string
        font
        color
        option
        gradient)
    (print "Do nothing")
)

; základní informace o skriptu a současně i definice obsahu dialogu
(script-fu-register "demo-box"
                    "Demo Box..."
                    "Do nothing, just show all input widgets available"
                    "Joe User"
                    "Joe User"
                    "August 2000"
                    ""
                    SF-ADJUSTMENT "SF-ADJUSTMENT (slider)" '( 30 1 2000 1 10 1 0)
                    SF-ADJUSTMENT "SF-ADJUSTMENT"         '(400 1 2000 1 10 1 1)
                    SF-COLOR      "SF-COLOR" '(255 0 255)
                    SF-DRAWABLE   "SF-DRAWABLE" 0
                    SF-FONT       "SF-FONT" ""
                    SF-GRADIENT   "SF-GRADIENT"  "Golden"
                    SF-IMAGE      "SF-IMAGE" 0
                    SF-OPTION     "SF-OPTION" '("Option 1" "Option 2" "Option 3")
                    SF-PATTERN    "SF-PATTERN" "Wood"
                    SF-STRING     "SF-STRING" "Test String"
                    SF-TOGGLE     "SF-TOGGLE" TRUE
                    SF-VALUE      "SF-VALUE" "0"
                    SF-FILENAME   "SF-FILENAME" "/"
)

; registrace skriptu do menu
(script-fu-menu-register "demo-box"
                         "&lt;Toolbox&gt;/Root.cz")

; finito
