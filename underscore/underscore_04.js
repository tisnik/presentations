// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 4
//                         Mnozinove operace s poli.
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



// pole s prvky 1..10
var array1 = _.range(1, 11);

// pole s prvky 6..15
var array2 = _.range(6, 16);

// pole s prvky 101..110
var array3 = _.range(101, 111);

printArrayInfo("array1");
printArrayInfo("array2");
printArrayInfo("array3");

// sjednoceni mnozin
printArrayInfo("_.union(array1, array2)");
printArrayInfo("_.union(array2, array1)");
printArrayInfo("_.union(array1, array3)");

printArrayInfo("_.union(array1, array2, array3)");

// prunik mnozin se spolecnymi prvky
printArrayInfo("_.intersection(array1, array2)");
printArrayInfo("_.intersection(array2, array1)");

// mnoziny nemaji spolecne prvky
printArrayInfo("_.intersection(array1, array3)");

// mnoziny nemaji spolecne prvky
printArrayInfo("_.intersection(array1, array2, array3)");

// rozdil mnozin (zde samozrejme zalezi na poradi)
printArrayInfo("_.difference(array1, array2)");
printArrayInfo("_.difference(array2, array1)");
printArrayInfo("_.difference(array1, array3)");
printArrayInfo("_.difference(array3, array1)");

printArrayInfo("_.difference(array1, array2, array3)");

// specialni pripad :)
printArrayInfo("_.difference(array1, array1)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

