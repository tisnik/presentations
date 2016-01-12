// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 9
//
// Zakladni vlastnosti mnozin
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

var set1 = mori.set([1,2,3,4]);
var set2 = mori.set([4,3,2,1]);
var set3 = mori.set([1,100,1,1]);
var set4 = mori.set(["C", "C++", "Java", "JavaScript", "D", "Lua", "C"])

var set5 = mori.sortedSet(1,2,3,4);
var set6 = mori.sortedSet(4,3,2,1);
var set7 = mori.sortedSet(1,100,1,1);
var set8 = mori.sortedSet("C", "C++", "Java", "JavaScript", "D", "Lua", "C")

var hugeSet = mori.set(mori.range(0,100))

printSequenceInfo("set1");
printSequenceInfo("set2");
printSequenceInfo("set3");
printSequenceInfo("set4");
printSequenceInfo("set5");
printSequenceInfo("set6");
printSequenceInfo("set7");
printSequenceInfo("set8");
printSequenceInfo("hugeSet");



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

