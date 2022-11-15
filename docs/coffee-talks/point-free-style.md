# Point-free style programming

* Programming paradigm in which function definitions do not identify the arguments
* Definitions just compose other functions by combining them
* Combinators
     - manipulate the arguments
* Introduced in J
* Now part of APL

## Feel of APL

* Vectors
* Functions
    - monadic
    - dyadic
* Operators
    - reduce
    - scan
    - inner product
    - outer product
* Combinators ("trains")
    - atop
    - fork

## Operators in APL

```
      monadic               dyadic
+     identity              addition
-     negation              subtraction
×     sign                  multiplication
÷     1/x                   division
ι     counter
|     absolute value        magnitude
```

##  Monadic functions

```apl
      -10
¯10

      ÷10
0.1

      |10
10

      |¯10
10
```

## Passing result to other monadic function

```apl
      |(÷(-3))
0.3333333333
```

* Can be shortened to

```apl
      |÷-3
0.3333333333
```

* Btw APL is an array language, so

```apl
      -÷⍳10
¯1 ¯0.5 ¯0.3333333333 ¯0.25 ¯0.2 ¯0.1666666667 ¯0.1428571429 ¯0.125 ¯0.1111111111 ¯0.1
```

## From functions to trains

* Function defined using classic style

```apl
      bar ← {-÷|⍵}

      bar 3
¯0.3333333333
```

* Point-free style

```apl
      baz ← -(÷|)

      baz 3
¯0.3333333333
```

## S-combinator

* Commonly used pattern in algorithms:

```apl
(⍺ f ⍵) g (⍺ h ⍵)
```

* **⍺** - parameter passed to function **f** and **h**
* **⍵** - parameter passed to function **f** and **h**
* **f** is dyadic function 
* **h** is dyadic function 
* **g** is dyadic function

* It's possible to shorten it to

```apl
(f g h)
```

- or even to

```apl
fgh
```

## Example

* Initial expression:

```apl
(⍳10) ∘.× (⍳10)

 1  2  3  4  5  6  7  8  9  10
 2  4  6  8 10 12 14 16 18  20
 3  6  9 12 15 18 21 24 27  30
 4  8 12 16 20 24 28 32 36  40
 5 10 15 20 25 30 35 40 45  50
 6 12 18 24 30 36 42 48 54  60
 7 14 21 28 35 42 49 56 63  70
 8 16 24 32 40 48 56 64 72  80
 9 18 27 36 45 54 63 72 81  90
10 20 30 40 50 60 70 80 90 100
```

* Can be shortened to:

```apl
(⍳∘.×⍳)10
```

* Put it into the function:

```apl
multiplicationTable ← ⍳∘.×⍳
```

- that's really it!

* Check it:

```apl
multiplicationTable 10
```
