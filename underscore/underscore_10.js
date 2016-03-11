// ------------------------------------------------------------
// Knihovna Underscore.js: demonstracni priklad cislo 10
//                         Pouziti funkci reduce a reduceRight
// ------------------------------------------------------------



// pole s prvky 1..10
var array1 = _.range(1, 11);


// bezna neanonymni (pojmenovana) funkce pouzita v reduce
// i v reduceRight
function add(x,y)
{
    return x+y;
}

// vypocet sumy prvku
var sum1 = _.reduce(array1, add);
var sum2 = _.reduceRight(array1, add);

console.log("sum1 = " + sum1);
console.log("sum2 = " + sum2);

// alternativni zpusob s pouzitim anonymnich funkci
console.log("sum1 = " + _.reduce(array1, function(x,y) {return x+y;}));
console.log("sum2 = " + _.reduceRight(array1, function(x,y) {return x+y;}));


// rozdil mezi reduce a reduceRight
var names = ["Perl", "Python", "Java", "JavaScript", "C", "C++", "Lua", "Clojure", "Forth", "APL", "BASIC"];


// bezna neanonymni (pojmenovana) funkce pouzita v reduce
// i v reduceRight
function concat(string1,string2)
{
    return string1 + ", " + string2
}

console.log("reduce: " + _.reduce(names, concat));
console.log("reduceRight: " + _.reduceRight(names, concat));

// alternativni zpusob s pouzitim anonymnich funkci
console.log("reduce: " + _.reduce(names, function(x,y) {return x+", "+y;}));
console.log("reduceRight: " + _.reduceRight(names, function(x,y) {return x+", "+y;}));



// ------------------------------------------------------------
// Finito
// ------------------------------------------------------------

