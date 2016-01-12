// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 7
//
// Otestovani funkce mori.partition() a mori.interleave()
// ------------------------------------------------------------



// ziskani typu sekvence
function sequenceType(sequence) {
    return mori.isList(sequence)   ? "list" :
           mori.isVector(sequence) ? "vector" :
           mori.isMap(sequence)    ? "map" :
           mori.isSet(sequence)    ? "set" :
           mori.isSeq(sequence)    ? "sequence" :
           "unknown";
}



// vypis informaci o vybrane sekvenci
function printSequenceInfo(declaration) {
    var sequence = eval(declaration);
    var type = sequenceType(sequence);
    console.log("---------------------------------");
    console.log(declaration);
    console.log("type:    " + type);
    console.log("length:  " + mori.count(sequence));
    console.log("content: " + sequence);
}

var seq = mori.range(0,12);

printSequenceInfo("mori.partition(1, seq)");
printSequenceInfo("mori.partition(2, seq)");
printSequenceInfo("mori.partition(3, seq)");
printSequenceInfo("mori.partition(4, seq)");
printSequenceInfo("mori.partition(6, seq)");
printSequenceInfo("mori.partition(20, seq)");

var seq1 = mori.range(0,12);
var seq2 = mori.repeat(12, '*');

printSequenceInfo("seq1");
printSequenceInfo("seq2");
printSequenceInfo("mori.interleave(seq1, seq2)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

