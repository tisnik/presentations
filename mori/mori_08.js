// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 8
//
// Otestovani funkce mori.partitionBy(), mori.takeWhile()
// a mori.filter().
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

function f0(n) {
    return "konstanta"
}

function f1(n) {
    return n < 6;
}

function f2(n) {
    return n % 2 == 1;
}

function f3(n) {
    return n % 4 == 3;
}

function f4(n) {
    return Math.random() < 0.5;
}

var seq = mori.range(0,12);

printSequenceInfo("mori.partitionBy(f0, seq)");
printSequenceInfo("mori.partitionBy(f1, seq)");
printSequenceInfo("mori.partitionBy(f2, seq)");
printSequenceInfo("mori.partitionBy(f3, seq)");
printSequenceInfo("mori.partitionBy(f4, seq)");

printSequenceInfo("mori.takeWhile(f1, seq)");
printSequenceInfo("mori.takeWhile(f2, seq)");
printSequenceInfo("mori.takeWhile(f3, seq)");

printSequenceInfo("mori.filter(f1, seq)");
printSequenceInfo("mori.filter(f2, seq)");
printSequenceInfo("mori.filter(f3, seq)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

