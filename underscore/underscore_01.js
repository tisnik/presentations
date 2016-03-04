// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 1
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



// vytvoreni bezneho pole, nad kterym se budou provadet nektere operace
var array1 = [1,2,3,4,5];

// informace o samotnem vstupnim poli
printArrayInfo(array1);

// zakladni operace nad polem
printArrayInfo("_.first(array1)");
printArrayInfo("_.last(array1)");
printArrayInfo("_.initial(array1)");
printArrayInfo("_.rest(array1)");


// otestovani funkce uniq
var array2 = [1,2,3,3,2,1];
var array3 = [3,2,1,1,2,3];
var array4 = [1,2,2,3,3,3,4,4,4,4];

// informace o samotnem vstupnim poli
printArrayInfo(array2);
printArrayInfo(array3);
printArrayInfo(array4);

// vytvoreni pole s unikatnimi hodnotami
printArrayInfo("_.uniq(array2)");
printArrayInfo("_.uniq(array3)");

// toto pole je setrideno, muzeme pouzit rychlejsi algoritmus
printArrayInfo("_.uniq(array4, true)");

// plati o pro pole retezcu atd.
var names = ["Perl", "Python", "Java", "JavaScript", "C", "Lua", "Clojure", "Lua", "C"];
printArrayInfo("names");
printArrayInfo("_.uniq(names)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

