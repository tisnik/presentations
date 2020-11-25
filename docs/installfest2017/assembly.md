# Assembler

```
   _____                              ___.   .__                
  /  _  \   ______ ______ ____   _____\_ |__ |  |   ___________ 
 /  /_\  \ /  ___//  ___// __ \ /     \| __ \|  | _/ __ \_  __ \
/    |    \\___ \ \___ \\  ___/|  Y Y  \ \_\ \  |_\  ___/|  | \/
\____|__  /____  >____  >\___  >__|_|  /___  /____/\___  >__|   
        \/     \/     \/     \/      \/    \/          \/       
```

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz>`
* Datum: 2017-02-28
* Prezentace:
    - [https://tisnik.github.io/presentations/installfest2017/assembly.html](https://tisnik.github.io/presentations/installfest2017/assembly.html)
* Zdrojový kód prezentace ve formátu Markdown:
    - [https://github.com/tisnik/presentations/blob/master/installfest2017/assembly.md](https://github.com/tisnik/presentations/blob/master/installfest2017/assembly.md)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/installfest2017/Assembly/asm.txt](https://github.com/tisnik/presentations/blob/master/installfest2017/Assembly/asm.txt)

## Proč assembler?

1. Větší efektivita využití CPU
1. Rychlejší (a predikovatelné) přerušovací rutiny
1. Efektivita při práci s pamětí (cache+RAM)
1. Kompaktní kód
    - Některé požadavky se mohou vzájemně vylučovat!
1. (Lepší pochopení práce s gdb a dalšími debuggery)

## Role assembleru

* Několik úrovní abstrakce (vrstev nad HW)
    - 5   uživatelské aplikace
    - 4½  (skriptovací engine)
    - 4   vyšší programovací jazyk
    - 3   assembler
    - 2   strojový kód
    - 1   syscalls
    - 0   HW

## Závislost na platformě

* Nezávislý
    - 5   uživatelské aplikace
    - 4½  (skriptovací engine)
    - 4   vyšší programovací jazyk
* Závislý
    - 3   assembler
    - 2   strojový kód
    - 1   syscalls
    - 0   HW

## Použití assembleru v minulosti

* První generace mainframů
    - vývojové diagramy v roli „vyššího jazyka“
    - assembler
    - strojový kód (zpočátku ruční překlad!)
* Mainframy a později minipočítače
    - přechod k vyšším programovacím jazykům
    - levnější vývoj, šance na přenositelnost
* Osmibitové herní konzole
    - assembler jediná rozumná volba
* Domácí mikropočítače
    - návrat „ke kořenům“
    - prakticky jediná volba pro profesionální aplikace
* Osobní mikropočítače
    - Motorola 68000
    - 8086/80286...
    - specifické použití assembleru (hry, dema, ...)
* DSP
    - výpočetní subrutiny (FFT...)
    - přerušovací rutiny

## Použití assembleru v současnosti

1. Firmware
2. Kód pracující přímo s HW (senzory, CPU+FPGA)
3. DSP a MCU - rychlé přerušovací rutiny!
4. Instrukce nedostupné ve vyšším programovacím jazyce
5. Specifické subrutiny (SIMD, SSE, rotace, hledání vzorků...)
6. Zpracování signálů
7. Kodeky
8. Virtuální stroje generující strojový kód
9. Reverse engineering :-)
10. Samomodifikující se kód
11. DSP
12. Fingerprints (A86)

## Instrukce nedostupné ve vyšším programovacím jazyce

* GCC nabízí ve formě „builtins“
    - `__builtin_clz`
    - `__builtin_parity`
    - `__builtin_bswap64`
    - a desítky dalších

## Použití assembleru v současnosti

* Většinou velmi SPECIFICKÉ pro určitou oblast
* Naprostá většina aplikací není psána pouze v assembleru
    - Coreboot: většinou C, jen zhruba 1% asm
    - Důvod: výhody vyšších programovacích jazyků + snadnější audit kódu

## Příklad

x264 naprogramovaný v assembleru
http://git.videolan.org/?p=x264.git;a=tree;f=common/x86;hb=HEAD

## Hodnocení „popularity“ assembleru ½

OpenHub
cca 0,5% projektů, <0,2% commitů

## Hodnocení „popularity“ assembleru 

TIOBE index
```
02/2017 02/2016 Jazyk            Hodnocení Změna
1       1       Java                16,6%  -4,4%
2       2       C                    8,4%  -7,1%
3       3       C++                  5,4%  -1,4%
4       4       C#                   4,9%  +0,5%
5       5       Python               4,0%  -0,1%
6       6       PHP                  3,0%  +0,3%
7       9       JavaScript           2,8%  +0,6%
8       7       Visual Basic .NET    2,8%  +0,3%
9       10      Delphi/Object Pascal 2,4%  +0,3%
10      8       Perl                 2,1%  -0,0%
11      11      Ruby                 2,1%  +0,1%
12      16      Swift                2,1%  +0,7%
13      13      Assembler ********   2,1%  +0,3%
```

## Kdy/proč psát v assembleru

* Seřazeno podle důležitosti a podle specificity
    1. Použití lepšího algoritmu (vyšší programovací jazyk)
        - čas/použití paměti
    2. Použití překladače, ne intepretru (či mixu typu JVM)
    3. Optimalizace nabízené překladačem + jejich kombinace
        - některé optimalizace se ovšem částečně vylučují (-Os, -O3)
    4. Hinty pro překladač (nutno odzkoušet, zda mají význam)
        - `const`, `const *`, `register`
    5. Profilování (!)
    6. Speciální vlastnosti konkrétního překladače (nepřenositelné!)
        - `__builtin_expect`, `__builtin_unreachable`, `__builtin_prefetch`...
        - `hot` atribut u funkcí, `pure` atribut, `simd` apod.
        - https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html#Common-Function-Attributes
    7. Přepis RELEVANTÍHO kódu do assembleru

## Assembler a Linux

* as    (*GNU Assembler*, *GAS*)
* NASM  (*Netwide Assembler*)
* Yasm  ()
* FASM  (*Flat Assembler*)

## GNU Assembler

* Součást klasického toolchainu
  `cpp → gcc → as → ld → spustitelný_soubor`
    - Překlad do asm: `gcc -S source.c`
* Původně jen AT&T syntaxe
* Dnes i „Intel“ syntaxe (na x86/x86-64)
* Různý způsob zápisu podle platformy!
    - Jména registrů
    - Konstanty
    - Adresování
    - Komentáře

## NASM

* Netwide Assembler
    - Syntaxe inspirována TASM a MASM
* Původní autor *Simon Tatham* (PuTTY...)
* Generuje objektový kód pro platformu x86 (16bit, 32bit, 64bit)
    - Zjednodušený toolchain
        - `nasm` → flat file (.COM, bootloader...)
        - `nasm` → `ln` → spustitelný_soubor

## FASM

* Flat Assembler
* Autor *Tomasz Grysztar*
* Backend pro PureBasic, BlitzMax a HLA

## Syscally a GNU Assembler

* Ukončení procesu funkcí `exit`
    - i386, syntaxe AT&T
    - i386, syntaxe Intel
    - ARM (32bit)
    - AArch64

## Kostra programu v assembleru

```gas
# Linux kernel system call table
sys_exit=1

.section .text
        .global _start          # tento symbol ma byt dostupny i linkeru

_start:
        movl  $sys_exit,%eax    # cislo sycallu pro funkci "exit"
        movl  $0,%ebx           # exit code = 0
        int   $0x80             # volani Linuxoveho kernelu
```

```
# Linux kernel system call table
sys_exit=60

.section .text
        .global _start          # tento symbol ma byt dostupny i linkeru

_start:
        movl  $sys_exit,%eax    # cislo sycallu pro funkci "exit"
        movl  $0,%edi           # exit code = 0
        syscall                 # volani Linuxoveho kernelu
```

## „Hello world“ v assembleru


```gas
# Linux kernel system call table
sys_exit=1
sys_write=4


.section .data

hello_lbl:
        .string "Hello World!\n"


.section .text
        .global _start          # tento symbol ma byt dostupny i linkeru

_start:
        mov   $sys_write, %eax  # cislo syscallu pro funkci "write"
        mov   $1,%ebx           # standardni vystup
        mov   $hello_lbl,%ecx   # adresa retezce, ktery se ma vytisknout
        mov   $13,%edx          # pocet znaku, ktere se maji vytisknout
        int   $0x80             # volani Linuxoveho kernelu

        movl  $sys_exit,%eax    # cislo sycallu pro funkci "exit"
        movl  $0,%ebx           # exit code = 0
        int   $0x80             # volani Linuxoveho kernelu
```

## Volání funkcí ze standardní céčkové knihovny

## `puts`

```gas
.intel_syntax noprefix


.section .data
hello_world_message:
        .asciz "Hello world!\n"    # zprava, ktera se ma vytisknout na standardni vystup


.section .text
        .global main               # tento symbol ma byt dostupny i linkeru

main:
        sub  rsp, 8                # zajistit zarovnani RSP na adresu delitelnou 16

                                   # jedinym parametrem je adresa zpravy
        mov  rdi, offset hello_world_message
        call puts                  # volani funkce 'puts' ze standardni knihovny

        add  rsp, 8                # obnoveni puvodni hodnoty RSP

        xor  eax, eax              # navratova hodnota (exit status)
        ret                        # ukonceni aplikace
```

## `printf`

```gas
.intel_syntax noprefix


.section .data
hello_world_message:
        .asciz "Hello world!\n"    # zprava, ktera se ma vytisknout na standardni vystup


.section .text
        .global main               # tento symbol ma byt dostupny i linkeru

main:
        sub  rsp, 8                # zajistit zarovnani RSP na adresu delitelnou 16

                                   # jedinym parametrem je adresa zpravy
        mov  rdi, offset hello_world_message
        xor  al, al                # pocet parametru predanych ve vektorovych registrech
        call printf                # volani funkce 'printf' ze standardni knihovny

        add  rsp, 8                # obnoveni puvodni hodnoty RSP

        xor  eax, eax              # navratova hodnota (exit status)

        ret                        # ukonceni aplikace
```

## Assembler v C

* Podporováno většinou překladačů
   Ovšem není součástí standardu
* Blok nebo „makro“ asm popř. __asm__
   ```C
   asm {
       add RAX, RBX
       nop
   }
   asm("add RAX, RBX \n\t"
       "nop");
   ```

## Zápis v GCC

```C
int main()
{
    __asm__ __volatile__(
        "nop   \n\t"
        : /* zadne vystupni registry */
        : /* zadne vstupni operandy */
        : /* zadne registry pouzivane uvnitr kodu */
    );
    return 0;
}
```

## Specifikace výstupních operandů

Expl## icitní registry pro výstupní operandy
    a   →   %rax, %eax, %ax, %al
    b   →   %rbx, %ebx, %bx, %bl
    c   →   %rcx, %ecx, %cx, %cl
    d   →   %rdx, %edx, %dx, %dl
    S   →   %rsi, %esi, %si
    D   →   %rdi, %edi, %di

## Specifikace vstupních operandů

## Explicitní určení registru pro výstupní operand

## Vliv optimalizací na generovaný kód

## Použití syntaxe používané firmou Intel

## Assembler a C pro procesory ARM

## gdb

* CLI
    - Ovládán interaktivně
    - Popř. lze spustit i skript s příkazy pro gdb
* TUI
    - gdbtui
* Velké možnosti nastavení
- Použití
    - Původně pro GNU CC
        - Compiler Collections
    - Dnes různé nástavby
        - Python...

## Ladicí informace ve vytvářených programech

* `gcc -g -O0 test.c`
    `-g`
        - přidání ladicích informací (symbolů)
    `-O0`
        - vypnutí optimalizací (usnadní ladění)

## Spuštění gdb

* Tři základní metody
    `gdb program_name`
    `gdb program_name PID`
    `gdb program_name core`

## Základní příkazy gdb

```
r      run
start            start+zastaví na mian
c      cont      continue
s      step      step into
n      next      step over
bt     backtrace print stacktrace
l      list      výpis zdrojového kódu (fce)
p      print     výpis výrazu
q      quit
h      help
```

## Breakpointy

```
b          breakpoint na aktuálním řádku
b#         breakpoint na řádku #
b fce      breakpoint na funkci
b file:fce specifikace souboru s funkcí
b file:#   specifikace souboru a čísla řádku

info b     informace o všech breakpointech
delete #   vymazání breakpointu s daným indexem
```

## Breakpointy s podmínkou

* `b fce if cond`
    - `cond` může být například `x<10`
* `ignore # count`
    - `#` je index (číslo) breakpointu
    - `count` je počet opakování

## Watchpointy

* `watch expr`
    - zastaveno při zápisu
* `rwatch expr`
    - zastaveno při čtení
* `awatch expr`
    - watch+rwatch
* `info watchpoints`

## Demo

* `as -g hello_world.s -o hello_world.o`
* `ld hello_world.o -o hello_world `
* `gdb hello_world`
```
    b _start
    display $eax
    display $ebx
    r
    Breakpoint 1, _start () at hello_world.s:32
    2: $ebx = 0
    1: $eax = 0
    n
    2: $ebx = 0
    1: $eax = 4
    c
```
