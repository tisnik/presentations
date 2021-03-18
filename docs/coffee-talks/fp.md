## Floating Point Arithmetic

* Numbers represented in a form:

<p><strong>X<sub>FP</sub> = (-1)<sup>s</sup>&nbsp;&times;&nbsp;b<sup>exp-bias</sup>&nbsp;&times;&nbsp;m</strong></p>

* XFP - final numeric value
* b - base (positive integer)
* exp - exponent (positive integer)
* bias - a constant
* m - mantissa (always positive for IEEE754)
* s - signum bit (positive/negative)

###

<table>
<tr><th>Computer/system</th><th>Width (b)</th><th>Base</th><th>Exponent (b)</th><th>Mantissa (b)</th></tr>
<tr><td>IEEE 754 half</td><td>16</td><td>2</td><td>5</td><td>10+1</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>IEEE 754 single</td><td>32</td><td>2</td><td>8</td><td>23+1</td></tr>
<tr><td>IEEE 754 double</td><td>64</td><td>2</td><td>11</td><td>52+1</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>IEEE 754 double extended</td><td>80</td><td>2</td><td>15</td><td>64</td></tr>
<tr><td>IEEE 754 quadruple</td><td>128</td><td>2</td><td>15</td><td>112+1</td></tr>
<tr><td>IEEE 754 octuple</td><td>256</td><td>2</td><td>19</td><td>236+1</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>IBM 7xx series</td><td>36</td><td>2</td><td>8</td><td>27</td></tr>
<tr><td>IBM 360 single</td><td>32</td><td>16</td><td>7</td><td>24</td></tr>
<tr><td>IBM 360 double</td><td>64</td><td>16</td><td>7</td><td>56</td></tr>
<tr><td>HP 3000 single</td><td>32</td><td>2</td><td>9</td><td>22</td></tr>
<tr><td>HP 3000 double</td><td>64</td><td>2</td><td>9</td><td>54</td></tr>
<tr><td>CDC 6000, 6600</td><td>60</td><td>2</td><td>11</td><td>48+1</td></tr>
<tr><td>Cray-1</a></td><td>64</td><td>2</td><td>15</td><td>48</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>Strela</a></td><td>43</td><td>2</td><td>7</td><td>35</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>Apple II</td><td>40</td><td>2</td><td>8</td><td>31+1</td></tr>
<tr><td>ZX Spectrum</td><td>40</td><td>2</td><td>8</td><td>31+1</td></tr>
<tr><td>Atari (FP rutiny)</td><td>48</td><td>10</td><td>7</td><td>40</td></tr>
<tr><td>Turbo Pascal real</td><td>48</td><td>2</td><td>8</td><td>39</td></tr>
</table>

### IEEE 754

* William "Velvel" Morton Kahan, University of California
* Designed to avoid many common errors in production code
    - and this is problem as many developers just don't care
* 1977
* 1980, the Intel 8087 chip
* Later Intel i80287, Intel i80387, Intel i80487, Motorola M68881, Motorola M68882
* Now supported by most CPUs in the world

#### Basic characteristic

* Binary exponent (i.e. some decimal values can't be represented properly)
* Focus to developers (less errors) than to performance
* Distinguish between +0 and -0 (very nice!) 
* Supports +∞:	yes
* Supports -∞:	yes
* Supports NaN:	yes
* Rules for working with NaNs and infinity
* Normalized values
* Denormalized values (less precision)
* Not to be used in banks etc.

#### IEEE 754 formats

<table>
<tr><th>Oficial name</th><th>Basic (must be supported)</th><th>a.k.a.</th><th>Sign</th><th>Exponent</th><th>Mantissa</th><th>Sum (bits)</th><th>Decimal numbers</th></tr>
<tr><td>binary16</td><td>&times;</td><td>half precision</td><td>1b</td><td> 5b</td><td>10b</td><td>16b</td><td>cca 3,3</td></tr>
<tr><td>binary32</td><td>&#x2713;</td><td>single precision/float</td><td>1b</td><td> 8b</td><td>23b</td><td>32b</td><td>cca 7,2</td></tr>
<tr><td>binary64</td><td>&#x2713;</td><td>double precision</td><td>1b</td><td>11b</td><td>52b</td><td>64b</td><td>cca 15,9</td></tr>
<tr><td>binary128</td><td>&#x2713;</td><td>quadruple precision</td><td>1b</td><td>15b</td><td>112b</td><td>128b</td><td>cca 34,0</td></tr>
<tr><td>binary256</td><td>&times;</td><td>octuple precision</td><td>1b</td><td>19b</td><td>236b</td><td>256b</td><td>cca 71,3</td></tr>
</table>

### Problems with IEE 754

* Can represents "real numbers"
* FP (double for example) is "precise"
* All algebraic rules are supported
* Conversion from int to float is w/o losing data
* Conversion from long to double is w/o losing data
* Ariane 5 Explosion | A Very Costly Coding Error: https://www.youtube.com/watch?v=5tJPXYA0Nec

### An example

```python
step = 0.1
x = 0.0
while x!= 1.0:
    x += step
    print(x)
```

```go
package main

import "fmt"

func main() {
        step := 0.1
        x := 0.0
        for x != 1.0 {
                x += step
                fmt.Printf("%f\n", x)
        }
}
```
### Beyond IEEE 754

* Usually smaller formats
    - for schools
    - for GPUs (16bit FP)
    - for AI/NN (16bit FP)

### Microfloat

* 8 bits values
* 1 bit for signum
* 4 bits for exponent
* 3 bits for mantissa
* BIAS=7
* Precision: 2-3 decimal digits
* Smallest non-zero value: 1/512
* Used in schools
* Possible to represent NaN, +∞, -∞

### Mini-FP

* 5 bits values
* 1 bit for sign
* 3 bits for exponent
* 2 bits for mantissa
* Only 64 values
* Possible to draw all of them on numeric axis

### Bfloat16 - Brain Floating Point

* For NN
* Now supported by many libraries and some Intel chips
* Basic characteristic
    - 16 bits values
    - 1 bit for sign
    - 5 bits for exponent
    - 10 bits for mantissa
    - BIAS=127
    - Precision: 3-4 decimal digits
    - Maximum value: 3.38953139 × 10^38
    - Minimum value: -3.38953139 × 10^38
    - Minimum positive value (non zero): 9.2 × 10^−41
    - Minimum normalized value: 1.18 × 10^-38
    - Supports +∞:	yes
    - Supports -∞:	yes
    - Supports NaN:	yes


# FP problems?

```
Equality                 Is it true?
x == (int)(float) x      yes/no
x == (int)(double) x     yes/no
f == (float)(double) f   yes/no
d == (float) d           yes/no
f == -(-f);              yes/no
2/3 == 2/3.0             yes/no
d < 0.0 ⇒ ((d*2) < 0.0)  yes/no
d > f ⇒ -f > -d          yes/no
d * d >= 0.0             yes/no
(d+f)-d == f             yes/no
(x+y)-y == x             yes/no
(x-y)+y == x             yes/no
```

