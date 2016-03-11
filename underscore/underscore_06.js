// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 6
//                         Pouziti funkce map() pri praci s poli
//                         ci s kolekcemi.
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



// bezna neanonymni (pojmenovana) funkce pouzita v map()
function doubleValue(value)
{
    return value*2;
}



// pole s prvky 1..10
var array1 = _.range(1, 11);

// vytvorime nove pole se sudymi cisly
var array2 = _.map(array1, doubleValue);

// alternativni zpusob vytvorime nove pole s prevracenymi hodnotami
// a to s pouzitim anonymni funkce
var array3 = _.map(array1, function(value) {return 1.0/value;});

// vypis informaci o vsech trech polich
printArrayInfo("array1");
printArrayInfo("array2");
printArrayInfo("array3");



// pouziti metody objektu Math
var array4 = _.map(array1, Math.sqrt);
printArrayInfo("array4");



// priklad pouziti metod objektu String
// puvodni pole
var names = ["Perl", "Python", "Java", "JavaScript", "C", "C++", "Lua", "Clojure", "Forth", "APL", "BASIC"];

// pole obsahujici retezce psane verzalkami
var upperCaseNames = _.map(names, String.toUpperCase);

// pole obsahujici retezce psane minuskami
var lowerCaseNames = _.map(names, String.toLowerCase);

// vypis informaci o vsech trech polich s retezci
printArrayInfo("names");
printArrayInfo("upperCaseNames");
printArrayInfo("lowerCaseNames");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

