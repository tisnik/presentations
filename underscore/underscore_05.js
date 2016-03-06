// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 5
//                         Operace zip a flatten.
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
        // nyni pracujeme s 2D poli, takze si postupne vypiseme jeho radky
        // (console.log totiz vypise i 2D pole jako jeden vektor)
        for (var i=0; i < anArray.length; i++) {
            console.log("row #" + i + " = " + anArray[i]);
        }
    }
    // jiny typ objektu, nemame zde jistotu, ze existuje atribut length
    else {
        console.log("type:    " + typeof anArray);
        console.log("content: " + anArray);
    }
}



// pole s prvky 1..10
var array1 = _.range(1, 11);

// pole s prvky "A".."J"
var array2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];

printArrayInfo("array1");
printArrayInfo("array2");


// kombinace prvku ze dvou poli
printArrayInfo("_.zip(array1, array2)");
printArrayInfo("_.zip(array2, array1)");

// kombinace prvku ze stejneho vstupniho pole
printArrayInfo("_.zip(array2, array2)");

// i toto je povoleno, posledni pole je kratsi
printArrayInfo("_.zip(array1, array2, [100,200,300])");



// otestovani funkce flatten()
var array3 = [_.range(1, 6), _.range(5,10), _.range(9,15)];
printArrayInfo("array3");
printArrayInfo("_.flatten(array3)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

