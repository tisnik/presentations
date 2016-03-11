// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 9
//                         Pouziti funkce partition()
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

// rozdelime pole na zaklade podminky
var partitioned = _.partition(array1, isEven);

// vytvorime nove pole jen se sudymi cisly
var array2 = partitioned[0];

// vytvorime nove pole jen s lichymi cisly
var array3 = partitioned[1];

// vypis informaci o vsech trech polich
printArrayInfo("array1");
printArrayInfo("array2");
printArrayInfo("array3");



// priklad s rozdelenim pole retezcu
var names = ["Perl", "Python", "Java", "JavaScript", "C", "C++", "Lua", "Clojure", "Forth", "APL", "BASIC"];

// rozdeleni pole retezcu podle toho, jak jsou jednotlive retezce dlouhe
var longAndShortNames = _.partition(names, function(str) {return str.length <= 4;});

// pro lepsi citelnost vytvorime samostatne pole kratkych
// a samostatne pole dlouhych retezcu
var shortNames = longAndShortNames[0];
var longNames = longAndShortNames[1];

// vypis informaci o vsech trech polich s retezci
printArrayInfo("names");
printArrayInfo("shortNames");
printArrayInfo("longNames");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

