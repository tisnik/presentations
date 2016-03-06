// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 3
//                         Pouziti funkci pro vyhledani prvku v polich.
// ------------------------------------------------------------



var names = ["C", "C++", "C#", "Java",
             "Perl", "Python", "Ruby", 
             "JavaScript", "CoffeeScript", "Dart", "Wisp",
             // prvky se opakuji
             "C", "C++", "C#", "Java",
             "Lua", "Clojure", "Lisp", "Forth"];



function printArrayItem(anArray, index)
{
    console.log("#" + i + " = " + anArray[i]);
}

var i;



console.log("_.indexOf():");

// bezne vyhledavani prvniho prvku
i = _.indexOf(names, "Java");
printArrayItem(names, i);

// vyhledavani od desateho prvku
i = _.indexOf(names, "Java", 10);
printArrayItem(names, i);

// bezne vyhledavani neexistujiciho prvku
i = _.indexOf(names, "BASIC");
printArrayItem(names, i);

console.log("---------------------------------------");



console.log("_.lastIndexOf():");

// bezne vyhledavani posledniho prvku
i = _.lastIndexOf(names, "Java");
printArrayItem(names, i);

// vyhledavani od desateho prvku
i = _.lastIndexOf(names, "Java", 10);
printArrayItem(names, i);

// bezne vyhledavani neexistujiciho prvku
i = _.lastIndexOf(names, "BASIC");
printArrayItem(names, i);

console.log("---------------------------------------");



/* predikat vracejici true pouze v pripade, ze se v prvku
 * nalezne podretezec odpovidajici regularnimu vyrazu.*/
function predicate(item)
{
    return /.*Java.*/.test(item);
}

/* predikat vracejici vzdy hodnotu true */
function constantTrue(item)
{
    return true;
}

/* predikat vracejici vzdy hodnotu false */
function constantFalse(item)
{
    return false;
}



console.log("_.findIndex():");

i = _.findIndex(names, predicate);
printArrayItem(names, i);

i = _.findIndex(names, constantTrue);
printArrayItem(names, i);

i = _.findIndex(names, constantFalse);
printArrayItem(names, i);

console.log("---------------------------------------");



console.log("_.findLastIndex():");

i = _.findLastIndex(names, predicate);
printArrayItem(names, i);

i = _.findLastIndex(names, constantTrue);
printArrayItem(names, i);

i = _.findLastIndex(names, constantFalse);
printArrayItem(names, i);

console.log("---------------------------------------");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

