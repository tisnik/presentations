// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 11
//
// Zakladni vlastnosti map
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

var map1 = mori.hashMap  ("k9", 9, "k8", 8, "k7", 7, "k6", 6, "k5", 5, "k4", 4, "k3", 3, "k2", 2, "k1", 1);
var map2 = mori.sortedMap("k9", 9, "k8", 8, "k7", 7, "k6", 6, "k5", 5, "k4", 4, "k3", 3, "k2", 2, "k1", 1);
var map3 = mori.hashMap("first", 1, "second", 2, "third", 3);

printSequenceInfo("map1");
printSequenceInfo("map2");
printSequenceInfo("mori.keys(map1)");
printSequenceInfo("mori.keys(map2)");
printSequenceInfo("mori.vals(map1)");
printSequenceInfo("mori.vals(map2)");
printSequenceInfo("map3");
printSequenceInfo("mori.merge(map1, map3)");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

