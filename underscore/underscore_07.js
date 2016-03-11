// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 7
//                         Pouziti funkci filter() a reject()
//                         pri praci s poli ci s kolekcemi.
// ------------------------------------------------------------



// funkce pro vypis informaci o vybranem poli (ci o jinem objektu)
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



// bezna neanonymni (pojmenovana) funkce pouzita ve filter() a reject()
function isEven(value)
{
    return value % 2 == 0;
}



// pole s prvky 1..10
var array1 = _.range(1, 11);

// vytvorime nove pole jen se sudymi cisly
var array2 = _.filter(array1, isEven);
// vytvorime nove pole jen s lichymi cisly
var array3 = _.reject(array1, isEven);

// vypis informaci o vsech trech polich
printArrayInfo("array1");
printArrayInfo("array2");
printArrayInfo("array3");

// alternativni zpusob s vyuzitim anonymnich funkci pro ziskani
// pole cisel mensich nez 6 resp. vetsich nez 5
var array4 = _.filter(array1, function(value) {return value <= 5;});
var array5 = _.reject(array1, function(value) {return value <= 5;});

printArrayInfo("array4");
printArrayInfo("array5");



// priklad s polem retezcu
// puvodni pole
var names = ["Perl", "Python", "Java", "JavaScript", "C", "C++", "Lua", "Clojure", "Forth", "APL", "BASIC"];

// pole obsahujici retezce psane verzalkami
var shortNames = _.filter(names, function(str) {return str.length <= 4;});

// pole obsahujici retezce psane minuskami
var longNames  = _.reject(names, function(str) {return str.length <= 4;});

// vypis informaci o vsech trech polich s retezci
printArrayInfo("names");
printArrayInfo("shortNames");
printArrayInfo("longNames");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

