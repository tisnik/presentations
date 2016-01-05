// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 4
// ------------------------------------------------------------

// konstrukce nekonecne lazy sekvence
var sequence1 = mori.range();

// z nekonecne lazy sekvence ziskame linou sekvenci s 10 prvky
var sequence2 = mori.take(10, sequence1);

// realizace druhe sekvence + jeji vypis
console.log("sequence2=" + sequence2);

// funkce pouzita ve funkcich map
function twice(element) {
    console.log('processing:', element);
    return 2 * element;
}

// mapujeme uzivatelskou funkci na *konecnou* sekvenci
var sequence3 = mori.map(twice, sequence2);

// mapujeme uzivatelskou anonymni funkci na *konecnou* sekvenci
var sequence4 = mori.map(function(element) {
    console.log('processing:', element);
    return -2 * element
}, sequence2);

// obe nove vytvorene sekvence vypiseme
// (tim se 'realizuji')
console.log("sequence3=" + sequence3);
console.log("sequence4=" + sequence3);

// nyni mapujeme uzivatelskou funkci na *nekonecnou* sekvenci
var sequence5 = mori.map(twice, sequence1);

// nyni mapujeme uzivatelskou anonymni funkci na *nekonecnou* sekvenci
var sequence6 = mori.map(function(element) {
    console.log('processing:', element);
    return -1 * element
}, sequence1);

// obe nove vytvorene sekvence vypiseme
// (tim se 'realizuji')
console.log("sequence5 begins with: " + mori.take(10, sequence5));
console.log("sequence6 begins with: " + mori.take(10, sequence6));

// mapovani muze mit nekolik "vrstev", stale se vsak jedna o lazy
// sekvence, ktere se prozatim nerealizuji
var sequence7 = mori.map(twice, mori.map(twice, sequence1));

// sekvence vypiseme
// (tim se 'realizuje')
console.log("sequence7 begins with: " + mori.take(10, sequence7));



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

