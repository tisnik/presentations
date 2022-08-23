# Just In Time compilers



## Three possible modes how to run code

* AOT (Ahead Of Time) compilation
    - a "classic" compiler like in C and Go
* interpretation
    - usually based on bytecode interpretation
    - see our previous presentations about lexer, tokenizer, and compiler in Python
* JIT (Just In Time) compilation
    - compilation during execution (run time)
    - "dynamic" compilation
    - usually preceded by bytecode interpretation



## JIT idea is old

* LISP (McCarthy) 1960
* Smalltalk 1983
* Self
* Later abandoned and replaced by Java
    - James Gosling 1993



## Why Just In Time compilation?

* Combines the speed of compiled code with the flexibility of interpretation
* At cost of overhead of an interpreter and the additional overhead of compilation
* JIT code offers far better performance than interpreters
* In some cases offer better performance than static compilation
    - some optimizations are only feasible at run-time



## JIT types

* Hot-spot based
* Tracing JITs



## Hot-spot based JITs

## Tracing JITs

* Bytecode analysis during *runtime*
    - i.e. bytecode is interpreted
    - and analyzed at the same time
* Analysis
    - *hot calls* detection
    - *hot loops* detection
* Output
    - set of *traces*
* Just these traces are compiled!
    - which means that not all bytecode is JITed



## LuaJIT

* Flow
    - source code
    - Lua bytecode
    - (interpretation+analysis)
    - hot calls and hot loops
    - traces
    - sequence of pseudoinstructions
    - compilation to native code


### Pseudoinstructions

* SSA form
    - Static Single Assignment form
    - two operands basically



## Example

### Source code

```lua
local i
local sum = 0

for i = 1,60 do
    sum = sum + 1
end

print(sum)
```

### Bytecode for hot loop (one trace)

```
---- TRACE 1 start test1.lua:4
0007  ADDVN    1   1   0  ; 1
0008  FORL     2 => 0007
```

### Loop represented as pseudoinstructions

```
---- TRACE 1 IR
0001    int SLOAD  #3    I
0002 >  int SLOAD  #2    T
0003 >+ int ADDOV  0002  +1
0004  + int ADD    0001  +1
0005 >  int LE     0004  +60
0006 ------ LOOP ------------
0007 >+ int ADDOV  0003  +1
0008  + int ADD    0004  +1
0009 >  int LE     0008  +60
0010    int PHI    0004  0008
0011    int PHI    0003  0007
---- TRACE 1 stop -> loop
```

### Machine code

```
---- TRACE 1 mcode 76
55e6545bffa5  mov dword [r14-0xec8], 0x1
55e6545bffb0  movsd xmm0, [r14+0xeba0]
55e6545bffb9  cvttsd2si ebp, [rdx+0x10]
55e6545bffbe  cmp dword [rdx+0xc], 0xfff90000
55e6545bffc5  jnb 0x55e6545b004c        ->0
55e6545bffcb  movsd xmm7, [rdx+0x8]
55e6545bffd0  addsd xmm7, xmm0
55e6545bffd4  add ebp, +0x01
55e6545bffd7  cmp ebp, +0x3c
55e6545bffda  jg 0x55e6545b0050 ->1
->LOOP:
55e6545bffe0  addsd xmm7, xmm0
55e6545bffe4  add ebp, +0x01
55e6545bffe7  cmp ebp, +0x3c
55e6545bffea  jle 0x55e6545bffe0        ->LOOP
55e6545bffec  jmp 0x55e6545b0058        ->3
---- TRACE 1 stop -> loop
```


## Source with multiple branches

```lua
local i
local x = 0
local y = 0
local z = 0

for i = 1,1000 do
    if i > 100 then
        x = x + 1
    end
    if i > 200 then
        y = y + 1
    end
    if i > 300 then
        z = z + 1
    end
end

print(x, y, z)
```

### Four traces are found + compiled

```
---- TRACE 1 start test2.lua:8
0009  KSHORT   8 100
0010  ISGE     8   7
0011  JMP      8 => 0013
0013  KSHORT   8 200
0014  ISGE     8   7
0015  JMP      8 => 0017
0017  KSHORT   8 300
0018  ISGE     8   7
0019  JMP      8 => 0021
0021  FORL     4 => 0009
---- TRACE 1 IR
0001    int SLOAD  #6    CI
0002 >  int LE     0001  +100
0003 >  int LE     0001  +200
0004 >  int LE     0001  +300
0005  + int ADD    0001  +1
0006 >  int LE     0005  +1000
0007 ------ LOOP ------------
0008 >  int LE     0005  +100
0009 >  int LE     0005  +200
0010 >  int LE     0005  +300
0011  + int ADD    0005  +1
0012 >  int LE     0011  +1000
0013    int PHI    0005  0011
---- TRACE 1 mcode 113
5580178cff80  mov dword [r14-0xec8], 0x1
5580178cff8b  cvttsd2si ebp, [rdx+0x20]
5580178cff90  cmp ebp, +0x64
5580178cff93  jg 0x5580178c0050 ->1
5580178cff99  cmp ebp, 0xc8
5580178cff9f  jg 0x5580178c0054 ->2
5580178cffa5  cmp ebp, 0x12c
5580178cffab  jg 0x5580178c0058 ->3
5580178cffb1  add ebp, +0x01
5580178cffb4  cmp ebp, 0x3e8
5580178cffba  jg 0x5580178c005c ->4
->LOOP:
5580178cffc0  cmp ebp, +0x64
5580178cffc3  jg 0x5580178c0064 ->6
5580178cffc9  cmp ebp, 0xc8
5580178cffcf  jg 0x5580178c0068 ->7
5580178cffd5  cmp ebp, 0x12c
5580178cffdb  jg 0x5580178c006c ->8
5580178cffe1  add ebp, +0x01
5580178cffe4  cmp ebp, 0x3e8
5580178cffea  jle 0x5580178cffc0 ->LOOP
5580178cffec  jmp 0x5580178c0070 ->9
---- TRACE 1 stop -> loop

---- TRACE 2 start 1/1 test2.lua:10
0012  ADDVN    1   1   0  ; 1
0013  KSHORT   8 200
0014  ISGE     8   7
0015  JMP      8 => 0017
0017  KSHORT   8 300
0018  ISGE     8   7
0019  JMP      8 => 0021
0021  JFORL    4   1
---- TRACE 2 IR
0001    int SLOAD  #6    PI
0002 >  num SLOAD  #3    T
0003    num ADD    0002  +1
0004 >  int LE     0001  +200
0005 >  int LE     0001  +300
0006    int ADD    0001  +1
0007 >  int LE     0006  +1000
0008    num CONV   0006  num.int
---- TRACE 2 mcode 108
5580178cff0d  mov dword [r14-0xec8], 0x2
5580178cff18  movsd xmm6, [r14-0x312f0]
5580178cff21  cmp dword [rdx+0xc], 0xfff90000
5580178cff28  jnb 0x5580178c004c ->0
5580178cff2e  movsd xmm7, [rdx+0x8]
5580178cff33  addsd xmm7, xmm6
5580178cff37  cmp ebp, 0xc8
5580178cff3d  jg 0x5580178c0050 ->1
5580178cff43  cmp ebp, 0x12c
5580178cff49  jg 0x5580178c0054 ->2
5580178cff4f  add ebp, +0x01
5580178cff52  cmp ebp, 0x3e8
5580178cff58  jg 0x5580178c0058 ->3
5580178cff5e  xorps xmm6, xmm6
5580178cff61  cvtsi2sd xmm6, ebp
5580178cff65  movsd [rdx+0x38], xmm6
5580178cff6a  movsd [rdx+0x20], xmm6
5580178cff6f  movsd [rdx+0x8], xmm7
5580178cff74  jmp 0x5580178cff80
---- TRACE 2 stop -> 1

---- TRACE 3 start 2/1 test2.lua:13
0016  ADDVN    2   2   0  ; 1
0017  KSHORT   8 300
0018  ISGE     8   7
0019  JMP      8 => 0021
0021  JFORL    4   1
---- TRACE 3 IR
0001    num SLOAD  #3    PI
0002    int SLOAD  #6    PI
0003 >  num SLOAD  #4    T
0004    num ADD    0003  +1
0005 >  int LE     0002  +300
0006    int ADD    0002  +1
0007 >  int LE     0006  +1000
0008    num CONV   0006  num.int
---- TRACE 3 mcode 101
5580178cfea1  mov dword [r14-0xec8], 0x3
5580178cfeac  movsd xmm5, [r14-0x30c18]
5580178cfeb5  cmp dword [rdx+0x14], 0xfff90000
5580178cfebc  jnb 0x5580178c004c ->0
5580178cfec2  movsd xmm6, [rdx+0x10]
5580178cfec7  addsd xmm6, xmm5
5580178cfecb  cmp ebp, 0x12c
5580178cfed1  jg 0x5580178c0050 ->1
5580178cfed7  add ebp, +0x01
5580178cfeda  cmp ebp, 0x3e8
5580178cfee0  jg 0x5580178c0054 ->2
5580178cfee6  xorps xmm5, xmm5
5580178cfee9  cvtsi2sd xmm5, ebp
5580178cfeed  movsd [rdx+0x38], xmm5
5580178cfef2  movsd [rdx+0x20], xmm5
5580178cfef7  movsd [rdx+0x10], xmm6
5580178cfefc  movsd [rdx+0x8], xmm7
5580178cff01  jmp 0x5580178cff80
---- TRACE 3 stop -> 1

---- TRACE 4 start 3/1 test2.lua:16
0020  ADDVN    3   3   0  ; 1
0021  JFORL    4   1
---- TRACE 4 IR
0001    num SLOAD  #3    PI
0002    num SLOAD  #4    PI
0003    int SLOAD  #6    PI
0004 >  num SLOAD  #5    T
0005    num ADD    0004  +1
0006    int ADD    0003  +1
0007 >  int LE     0006  +1000
0008    num CONV   0006  num.int
---- TRACE 4 mcode 94
5580178cfe3c  mov dword [r14-0xec8], 0x4
5580178cfe47  movsd xmm4, [r14-0x30a90]
5580178cfe50  cmp dword [rdx+0x1c], 0xfff90000
5580178cfe57  jnb 0x5580178c004c ->0
5580178cfe5d  movsd xmm5, [rdx+0x18]
5580178cfe62  addsd xmm5, xmm4
5580178cfe66  add ebp, +0x01
5580178cfe69  cmp ebp, 0x3e8
5580178cfe6f  jg 0x5580178c0050 ->1
5580178cfe75  xorps xmm4, xmm4
5580178cfe78  cvtsi2sd xmm4, ebp
5580178cfe7c  movsd [rdx+0x38], xmm4
5580178cfe81  movsd [rdx+0x20], xmm4
5580178cfe86  movsd [rdx+0x18], xmm5
5580178cfe8b  movsd [rdx+0x10], xmm6
5580178cfe90  movsd [rdx+0x8], xmm7
5580178cfe95  jmp 0x5580178cff80
---- TRACE 4 stop -> 1
```

## Links

* [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
