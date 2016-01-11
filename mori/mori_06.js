// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 6
//
// Otestovani funkce mori.repeat()
// ------------------------------------------------------------



// vypis informaci o vybrane sekvenci
function printSequenceInfo(declaration) {
    var sequence = eval(declaration);
    console.log("---------------------------------");
    console.log(declaration);
    console.log("length:  " + mori.count(sequence));
    console.log("content: " + sequence);
}

printSequenceInfo("mori.repeat(1, 10)");
printSequenceInfo("mori.repeat(10, 1)");
printSequenceInfo("mori.repeat(10, 'hello')");
printSequenceInfo("mori.take(42, mori.repeat('*'))");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

