// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 3
// ------------------------------------------------------------

// vytvoreni ctyr seznamu ruzne delky
var list1 = mori.list(1,2,3);
var list2 = mori.list(1,2);
var list3 = mori.list(1);
var list4 = mori.list();

// vytvoreni ctyr vektoru ruzne delky
var vector1 = mori.vector(1,2,3);
var vector2 = mori.vector(1,2);
var vector3 = mori.vector(1);
var vector4 = mori.vector();



// ------------------------------------------------------------
// Vypis informaci o delkach seznamu a vektoru
// ------------------------------------------------------------
console.log("List1 size: " + mori.count(list1));
console.log("List2 size: " + mori.count(list2));
console.log("List3 size: " + mori.count(list3));
console.log("List4 size: " + mori.count(list4));

console.log("Vector1 size: " + mori.count(vector1));
console.log("Vector2 size: " + mori.count(vector2));
console.log("Vector3 size: " + mori.count(vector3));
console.log("Vector4 size: " + mori.count(vector4));



// ------------------------------------------------------------
// Vyzkouseni funkce first
// ------------------------------------------------------------
console.log("Using first:");

console.log("first list1: " + mori.first(list1));
console.log("first list2: " + mori.first(list2));
console.log("first list3: " + mori.first(list3));
console.log("first list4: " + mori.first(list4));

console.log("first vector1: " + mori.first(vector1));
console.log("first vector2: " + mori.first(vector2));
console.log("first vector3: " + mori.first(vector3));
console.log("first vector4: " + mori.first(vector4));



// ------------------------------------------------------------
// Vyzkouseni funkce rest
// ------------------------------------------------------------
console.log("Using rest:");

console.log("rest list1: " + mori.rest(list1));
console.log("rest list2: " + mori.rest(list2));
console.log("rest list3: " + mori.rest(list3));
console.log("rest list4: " + mori.rest(list4));

console.log("rest vector1: " + mori.rest(vector1));
console.log("rest vector2: " + mori.rest(vector2));
console.log("rest vector3: " + mori.rest(vector3));
console.log("rest vector4: " + mori.rest(vector4));



// ------------------------------------------------------------
// Kombinace rest+first
// ------------------------------------------------------------
console.log("Using rest+first:");

console.log("rest+first list1: " + mori.first(mori.rest(list1)));
console.log("rest+first list2: " + mori.first(mori.rest(list2)));
console.log("rest+first list3: " + mori.first(mori.rest(list3)));
console.log("rest+first list4: " + mori.first(mori.rest(list4)));

console.log("rest+first vector1: " + mori.first(mori.rest(vector1)));
console.log("rest+first vector2: " + mori.first(mori.rest(vector2)));
console.log("rest+first vector3: " + mori.first(mori.rest(vector3)));
console.log("rest+first vector4: " + mori.first(mori.rest(vector4)));



// ------------------------------------------------------------
// Kombinace rest+rest
// ------------------------------------------------------------
console.log("Using rest+rest:");

console.log("rest+rest list1: " + mori.rest(mori.rest(list1)));
console.log("rest+rest list2: " + mori.rest(mori.rest(list2)));
console.log("rest+rest list3: " + mori.rest(mori.rest(list3)));
console.log("rest+rest list4: " + mori.rest(mori.rest(list4)));

console.log("rest+rest vector1: " + mori.rest(mori.rest(vector1)));
console.log("rest+rest vector2: " + mori.rest(mori.rest(vector2)));
console.log("rest+rest vector3: " + mori.rest(mori.rest(vector3)));
console.log("rest+rest vector4: " + mori.rest(mori.rest(vector4)));



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

