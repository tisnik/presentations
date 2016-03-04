// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 2
// ------------------------------------------------------------



// funkce pro vypis informaci o vybranem poli (ci jinem objektu)
function printArrayInfo(expression) {
    var anArray = eval(expression);
    console.log("---------------------------------");
    console.log(expression);

    // zjisteni typu objektu (a pripadne delky pole)
    if (anArray instanceof Array) {
        console.log("type:    array");
        console.log("length:  " + anArray.length);
    }
    // jiny typ objektu, nemame zde jistotu, ze existuje atribut length
    else {
        console.log("type:    " + typeof anArray);
    }
    console.log("content: " + anArray);
}



// informace o polich vytvorenych funkci range
printArrayInfo("_.range(10)");
printArrayInfo("_.range(-10)");
printArrayInfo("_.range(0, 10)");
printArrayInfo("_.range(10, 0)");
printArrayInfo("_.range(10, 0, -1)");
printArrayInfo("_.range(0, 10, 2)");
printArrayInfo("_.range(0, 10, -2)");
printArrayInfo("_.range(10, 0, 2)");
printArrayInfo("_.range(10, 0, -2)");
printArrayInfo("_.range(0, 10, 100)");

// lze pouzit i desetinna cisla
printArrayInfo("_.range(10, 15, 0.5)");
printArrayInfo("_.range(10,  5,-0.5)");

// stara znama chyba se zde projevuje jen castecne
printArrayInfo("_.range(0, 10, 0.1)");


// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

