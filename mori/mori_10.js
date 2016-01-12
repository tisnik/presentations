// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 10
//
// Operace s mnozinami
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

var set1 = mori.set(mori.range(0,10));
var set2 = mori.set(mori.range(0,6));
var set3 = mori.set(mori.range(4,10));

printSequenceInfo("set1");
printSequenceInfo("set2");
printSequenceInfo("set3");
printSequenceInfo("mori.union(set2, set3)");
printSequenceInfo("mori.intersection(set2, set3)");
printSequenceInfo("mori.difference(set2, set3)");
printSequenceInfo("mori.difference(set3, set2)");
printSequenceInfo("mori.difference(set1, set2)");
printSequenceInfo("mori.difference(set1, set3)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

