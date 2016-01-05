// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 1
// ------------------------------------------------------------

// vytvoreni perzistentniho seznamu
var moriList = mori.list(1,2,3);

// vypocet delky perzistentniho seznamu
var listSize = mori.count(moriList);

// prevod perzistentniho seznamu na "normalni" JavaScriptove pole
var jsList = mori.toJs(moriList);

// vypis zakladnich informaci o perzistentnim seznamu i o jeho
// JavaScriptove variante
console.log("List size: " + listSize);
console.log("List to JavaScript: " + jsList);



// ------------------------------------------------------------
// Vypis typu objektu moriList a jsList - prvni varianta
// ------------------------------------------------------------
console.log("Using typeof:");
// operator typeof nam moc nepomuze v pripade objektovych typu
console.log("jsList type:   " + typeof jsList);
console.log("moriList type: " + typeof moriList);



// ------------------------------------------------------------
// Vypis typu objektu moriList a jsList - druha varianta
// ------------------------------------------------------------
console.log("Using Object.toString():");
// ziskame referenci na toString a ulozime do promenne toClass
var toClass = {}.toString

// vypis informace o typech objektu
console.log("jsList type:   " + toClass.call(jsList));
console.log("moriList type: " + toClass.call(moriList));



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

