// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 12
//
// Operace s mapami
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

function factorial(n) {
    var fac = 1;
    for (var i = 2; i <= n; i++) {
        fac = fac * i;
    }
    return fac;
}

var seq1 = mori.range(1,11);
var seq2 = mori.map(factorial, seq1);

var map1 = mori.zipmap(seq1, seq2);

printSequenceInfo("seq1");
printSequenceInfo("seq2");
printSequenceInfo("mori.zipmap(seq1, seq2);");


var map2 = mori.sortedMap(1, "first", 2, "second", 3, "third");
printSequenceInfo("map2");
printSequenceInfo("mori.assoc(map2, 4, 'fourth', 5, 'fifth')");
printSequenceInfo("mori.dissoc(map2, 1, 5)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

