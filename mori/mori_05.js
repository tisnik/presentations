// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 5
//
// Otestovani funkce mori.range()
// ------------------------------------------------------------



// vypis informaci o vybrane sekvenci
function printSequenceInfo(declaration) {
    var sequence = eval(declaration);
    console.log("---------------------------------");
    console.log(declaration);
    console.log("length:  " + mori.count(sequence));
    console.log("content: " + sequence);
}

printSequenceInfo("mori.range(1, 10)");
printSequenceInfo("mori.range(1, 10, 2)");
printSequenceInfo("mori.range(10, 1, -2)");
printSequenceInfo("mori.range(10)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

