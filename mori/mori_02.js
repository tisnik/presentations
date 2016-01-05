// ------------------------------------------------------------
// Knihovna Mori: demonstracni priklad cislo 2
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
// Vyzkouseni funkce conj
// ------------------------------------------------------------
console.log("Using conj:");

console.log("conj list1: " + mori.conj(list1, 42));
console.log("conj list2: " + mori.conj(list2, 42));
console.log("conj list3: " + mori.conj(list3, 42));
console.log("conj list4: " + mori.conj(list4, 42));

console.log("conj vector1: " + mori.conj(vector1, 42));
console.log("conj vector2: " + mori.conj(vector2, 42));
console.log("conj vector3: " + mori.conj(vector3, 42));
console.log("conj vector4: " + mori.conj(vector4, 42));



// ------------------------------------------------------------
// Vyzkouseni funkce pop
// ------------------------------------------------------------
console.log("Using pop:");

console.log("pop list1: " + mori.pop(list1));
console.log("pop list2: " + mori.pop(list2));
console.log("pop list3: " + mori.pop(list3));
// nasledujici volani skonci chybou!
//console.log("pop list4: " + mori.pop(list4));

console.log("pop vector1: " + mori.pop(vector1));
console.log("pop vector2: " + mori.pop(vector2));
console.log("pop vector3: " + mori.pop(vector3));
// nasledujici volani skonci chybou!
//console.log("pop vector4: " + mori.pop(vector4));



// ------------------------------------------------------------
// Vyzkouseni funkce peek
// ------------------------------------------------------------
console.log("Using peek:");

console.log("peek list1: " + mori.peek(list1));
console.log("peek list2: " + mori.peek(list2));
console.log("peek list3: " + mori.peek(list3));
console.log("peek list4: " + mori.peek(list4));

console.log("peek vector1: " + mori.peek(vector1));
console.log("peek vector2: " + mori.peek(vector2));
console.log("peek vector3: " + mori.peek(vector3));
console.log("peek vector4: " + mori.peek(vector4));



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
// Vyzkouseni funkce last
// ------------------------------------------------------------
console.log("Using last:");

console.log("last list1: " + mori.last(list1));
console.log("last list2: " + mori.last(list2));
console.log("last list3: " + mori.last(list3));
console.log("last list4: " + mori.last(list4));

console.log("last vector1: " + mori.last(vector1));
console.log("last vector2: " + mori.last(vector2));
console.log("last vector3: " + mori.last(vector3));
console.log("last vector4: " + mori.last(vector4));



// ------------------------------------------------------------
// Vyzkouseni funkce distinct
// ------------------------------------------------------------
console.log("Using distinct:");

console.log("distinct []: " + mori.distinct(mori.list()));
console.log("distinct [1]: " + mori.distinct(mori.list(1)));
console.log("distinct [1 2]: " + mori.distinct(mori.list(1,2)));
console.log("distinct [1 2 1]: " + mori.distinct(mori.list(1,2,1)));
console.log("distinct [1 2 1 2]: " + mori.distinct(mori.list(1,2,1,2)));



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

