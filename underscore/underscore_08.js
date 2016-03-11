// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 8
//                         Pouziti funkci some() a every()
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



// test zda pole obsahuje jen suda cisla
function containsOnlyEvenValues(anArray)
{
    return _.every(anArray, isEven);
}

// test zda pole obsahuje alespon jedno sude cislo
function containsEvenValue(anArray)
{
    return _.some(anArray, isEven);
}

console.log("---------------------------------");

console.log("array1 contains only even values: " + containsOnlyEvenValues(array1));
console.log("array2 contains only even values: " + containsOnlyEvenValues(array2));
console.log("array3 contains only even values: " + containsOnlyEvenValues(array3));

console.log("---------------------------------");

console.log("array1 contains at least one even value: " + containsEvenValue(array1));
console.log("array2 contains at least one even value: " + containsEvenValue(array2));
console.log("array3 contains at least one even value: " + containsEvenValue(array3));



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

