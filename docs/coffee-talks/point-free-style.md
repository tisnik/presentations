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

```
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

```
      |(÷(-3))
0.3333333333
```

* Can be shortened to

```
      |÷-3
0.3333333333
```

* Btw APL is an array language, so

```
      -÷⍳10
¯1 ¯0.5 ¯0.3333333333 ¯0.25 ¯0.2 ¯0.1666666667 ¯0.1428571429 ¯0.125 ¯0.1111111111 ¯0.1
```

## From functions to trains

* Function defined using classic style

```
      bar ← {-÷|⍵}

      bar 3
¯0.3333333333
```

* Point-free style

```
      baz ← -(÷|)

      baz 3
¯0.3333333333
```

## S-combinator
