// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 11
//                         Pouziti funkce each spolecne s funkci
//                         reduce.
// ------------------------------------------------------------



// alternativni zpusob vypoctu faktorialu
function factorial(n)
{
    // vytvori se posloupnost 1..n
    // postupne se jednotlive prvky poslouposti nasobi
    // a vrati se vysledek
    return _.reduce(_.range(1,n+1), function(x,y) {return x*y;});
}

// tisk nekolika faktorialu pro vstupni hodnoty 1..10
// (vime jiz, ze funkce range nezahrnuje mezni hodnotu)

// funkce each pracuje jako smycka foreach
// (neni to tedy cista funkce, protoze ma a musi mit vedlejsi efekt)
_.each(_.range(1,11), function(n) {console.log(n + "! = " + factorial(n));});



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

