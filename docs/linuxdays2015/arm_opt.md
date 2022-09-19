Optimalizace při překladu na procesorech ARM
==================================================

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz`
* Datum    2015-10-10
* Prezentace:
    - [https://tisnik.github.io/presentations/linuxdays2015/arm_opt.html](https://tisnik.github.io/presentations/linuxdays2015/arm_opt.html)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/linuxdays2015/arm_opt/arm_opt.txt](https://github.com/tisnik/presentations/blob/master/linuxdays2015/arm_opt/arm_opt.txt)

Obsah přednášky
-------------------------------
* ARM32 z pohledu programátora
* Instrukční sady procesorů ARM
    - Původní instrukční sada ARM (A32)
    - Instrukční sada Thumb
    - Instrukční sada Thumb-2
    - A64 (AArch64)
* Další rozšíření instrukční sady procesorů ARM
    - VFP
    - SIMD
    - NEON
* Problematika FP operací
* Omezení některých jader ARM

ARM32 z pohledu programátora
-------------------------------
* Architektura typu Load-Store
    - Pro efektivní práci nutný velký počet registrů
    - Omezení přístupů do pomalé paměti
    - Alokace registrů
        - → optimalizující překladač
* Řešení
    - 27/37 registrů
        - 30 pracovních, `PC`, `CPSR`, 5x`SPSR`
        - 15 registrů viditelných `r0`..`r14`
        - `r13` Stack Pointer
        - `r14` Link Register
    - Šířka registrů 32 bitů
    - Rozdělení do banků, které se překrývají
    - Pro každý stav procesoru zvláštní bank

Instrukční sady procesorů ARM
-------------------------------
* A32
    - 32bitové instrukce, 32bitové operandy
* Thumb (T32)
    - 16bitové instrukce
* Thumb-2
    - Mix 16 a 32bitových instrukcí
* A64
    - 32bitové instrukce, 64bitové operandy

Instrukční sada A32
-------------------------------
* Původní instrukční sada procesorů ARM
* Konstantní šířka instrukcí 32bitů
* Šířka zpracovávaných dat taktéž 32 bitů
    - Problém s načítáním konstant
    - Musí se řešit na každé architektuře RISC

Typy instrukcí
-------------------------------
* Load-store (jeden registr)
* Load-store (více registrů)
* Aritmetické operace
* Logické a bitové operace
* Skoky a změna režimu procesoru
* Práce se stavovými registry CPSR a SPSR
* Práce se semafory
* Instrukce koprocesoru(ů)

Vlastnosti ISA typické pro ARM
-------------------------------
* Vykonání instrukce na základě příznaků
    - `N` - negative
    - `V` - overflow
    - `Z` - zero
    - `C` - carry
    - `Q` - sticky (ARMv5 a výše)
* Lze odstranit některé skoky
* Lze zvolit, které příznaky se mají nastavit
* U mnoha instrukcí lze druhý operand
    - Posunout
    - Zrotovat

Velmi často používaný příklad
-------------------------------
```gcc
int gcd(int a, int b) {
   while (a != b) {
      if (a > b) a = a - b;
      else       b = b - a;
   }
   return a;
}
```

Klasický přístup při překladu
-------------------------------
```asm
 gcd    CMP      r0, r1
        BEQ      end
        BLT      less
        SUB      r0, r0, r1
        B        gcd
 less
        SUB      r1, r1, r0
        B        gcd
 end
```

Využití příznaků
-------------------------------
```asm
 gcd
        CMP      r0, r1
        SUBGT    r0, r0, r1
        SUBLT    r1, r1, r0
        BNE      gcd
```

Výsledky
-------------------------------
* Klasický přístup
    -  7 instrukcí
    - 28 bajtů
    - 13 taktů (branch=vyprázdnění cache=3 takty)
* Využití podmíněných instrukcí
    -  4 instrukce
    - 16 bajtů
    - 10 taktů (pouze jeden branch)
* Thumb (viz další slajdy)
    -  7 instrukcí
    - 14 bajtů (16bit/instrukci)

Instrukční sada Thumb (T32)
-------------------------------
* ARMv4T a další modely
* Šířka instrukcí 16bitů
* Podmnožina původní instrukční sady
* Optimalizováno s ohledem na překladače C a C++
* Přepínání mezi stavem ARM a stavem Thumb
    - Nutno přepínat, protože instrukce nejsou kompatibilní
* Rozdělení registrů
    - Lo registers `r0`-`r7`
    - Hi registers `r8`-`r15`
    - Některé instrukce pracují pouze s jednou skupinou
        - Ušetří se bity v instrukci

Instrukční sada Thumb (T32)
-------------------------------
* Thumb neumožňuje podmníněné provádění instrukcí
* Jen podmíněné skoky
* Skoky
    - `B`: Branch
    - `BL`: Branch and link
* Aritmetické a logické operace
    - `OP Rd, Rn, Rm`
        - omezení na `r0`..`r7`
        - tři bity pro výběr registru v instr.slovu
    - Výjimky
        - `ADD Rd, Rn, konstanta`
        - `ADD Rd, Rm` - jeden z registrů `r8`..`r15`
        - `CMP Rm, Rn` - dtto
        - `MOV Rd, Rm` - dtto

Instrukční sada Thumb (T32)
-------------------------------
* Aritmetické instrukce
    - `ADD`, `ADC`, `SUB`, `SBC`
    - `MUL`, `NEG`
* Logické operace
    - `AND`, `EOR`, `ORR`
* Rotace a posuny
    - `ASR`, `LSL`, `LSR`, `ROR`
* Porovnání a nastavení příznaků
    - `CMP`, `CMN`, `TST`
* Skoky
    - `B`, `BL`, `BX`, `BLX` (link, exchange)
* Přesuny dat
    - `MOV`, `MVN`            - move (not)
    - `POP`, `PUSH`
* Operace typu LOAD a STORE
    - `LDR`, `LDRH`, `LRRB`     - load (word, halfword, byte)
    - `LDRSH`, `LDRSB`   - sign extend (na word)
    - `STR`, `STRH`, `STRB`     - store (word, halfword, byte)
    - `LDMIA`, `STMIA`        - vektor registrů 
    - `STXH`, `STXB`, `UXTH`, `UXTB` - sign/zero extend

Instrukční sada Thumb-2
-------------------------------
* 2003
* ARMv7
* Povoluje kombinace instrukcí o šířce 16 a 32 bitů
* Zpětná kompatibilita s Thumb
* Větší složitost čipů
* Větší „hustota“ strojového kódu
    - Srovnatelná s Thumb
* Má smysl ve světě rychlých CPU, pomalých DRAM a drahých cache
* Výkonnost srovnatelná s ARM režimem

Instrukční sada Thumb-2
-------------------------------
* Bitové operace
    - Bit Field Clear
    - Bit Field Insert
* `CBZ`
    - Compare and Branch on Zero
* `CBNZ`
    - Compare and Branch on Non-Zero
* `IT`
    - Instrukce odpovídající konstrukci if-then-else
    - (viz následující slajd)

RISCové procesory a problém se skoky
-------------------------------------
* RISCová pipeline
    - Nemá smysl nečinně čekat na výsledek skoku
    - → spekulativní provádění instrukcí
    - × Čím delší pipeline, tím větší cena za špatný odhad sekvence instrukcí
* Statická a/nebo dynamická predikce skoků
    - Dynamická
        - Branch Target Address Cache (BTAC) pamatuje si výsledek skoku
    - Statická
        - Použije se, když BTAC neobsahuje informaci "taken" pro podmíněné skoky dozadu
    - Úspěšnost se udává okolo 85%
    - × U dvoubitového prediktoru je to až 93%

IT
-------------------------------
* `IT{pattern} {condition}`
    - až čtyři instrukce provedené na základě testu
    - (pozitivní/negativní výsledek)
* `{pattern}`
    - `T`-then
    - `E`-else
* první instrukce
    - provedena při splnění podmínky `{condition}`
* druhá instrukce
    - `T`-podmínka
    - `E`-inverze podmínky
* třetí a čtvrtá instrukce
    - dtto
* `{condition}`
    `EQ NE GT GE LT LE`
    `CS CC` (carry)
    `PL MI HI LS`

```asm
CMP r0, r1
ITE EQ
MOVEQ r0, r2 ; větev "then"
MOVNE r0, r3 ; větev "else"
```

Výsledky měření: délka kódu
----------------------------------
```
Instrukční sada Délka kódu
==================================
ARM             100%
Thumb            70%
Thumb-2          74%
```

Výsledky měření: rychlost aplikace
----------------------------------
```
Instrukční sada Relativní rychlost
==================================
ARM             100%
Thumb            75%
Thumb-2          98%
```

Instrukční sada A64
-------------------------------
* 32bitů -> 64bitů
* Pravděpodobně největší změna v architektuře procesorů ARM v celé jejich historii
* Velké odlišnosti, nutnost překladu pro novou architekturu

AArch64 z pohledu programátora
-------------------------------
* Instrukční sada A64
* Instrukční slova
    - Konstantní šířka 32 bitů
* Pracovní registry
    - 64bitové
    - 31 univerzálních registrů
    - 32.registr
        - liší se v závislosti na kontextu
        - buď nula (`ZR`)
        - nebo Stack pointer (`SR`)
    - `PC` není přímo dostupný

Operace
-------------------------------
* 32bitové
    - horních 32 bitů zdrojových registrů ignorováno
    - horních 32 bitů cílového registru vynulováno
* 64bitové

Multiply/divide
-------------------------------
* signed
* unsigned
* 32×32    → 32
* 64×64    → 64
* 64+32×32 → 64 (multiply and accumulate)
* 64×64    → 64+64 (registrový pár)

Skoky a rozeskoky
-------------------------------
* +- 1MB pro podmíněné skoky
* +- 128MB pro nepodmíněné skoky

Instrukce s podmínkou
-------------------------------
* Již nejsou podporovány
    - Rozhodnutí založeno na výsledcích benchmarků
    - Více bitů v instrukčním slově použitelných pro jiné účely
    - Současné prediktory skoků jsou již velmi kvalitní
    - Podmínky mohou být použity jen u některých instrukcí

==================
Specifika AArch 64
==================

A57
-------------------------------
Instrukce jsou dekódovány do µops
    - Fetch + Decode:  in order
    - Execute (issue): out of order
* Pro issue: osm samostatných pipeline
    - Integer 0
    - Integer 1
    - Integer Multi-cycle
    - Branch
    - Load
    - Store
    - FP/ASIMD 0
    - FP/ASIMD 1

Osm samostatných pipeline (pokr.)
-------------------------------
* Výpočetní moduly v pipelines
    - Integer Multi-cycle
        - Shift
        - `MUL`
        - `DIV`
        - `CRC`
    - FP/ASIMD 0
        - všechny FP operace
        - crypto
    - FP/ASIMD 1
        - `ADD`, `MUL`

Podpora pro operace s FP
-------------------------------
* "softfloat" nepodporováno
* Podobné VPS
* FP registry
    - 32 pracovních registrů
    - Každý registr až 4x32 bitů
* Použití registrů
    - Skalární hodnoty
        - float
        - double
        - quad
    - Vektory
        - 8x short float
        - 4x float
        - 2x double
SIMD
-------------------------------
* Režim kompatibility s IEEE 754

Crypto
-------------------------------
* AES
* SHA-1
* SHA-256

Rozšíření instrukčních sad
-------------------------------
* FPA
* VFP
* Advanced SIMD Architecture
* NEON (Advanced SIMD)
* Jazelle
    - Podpora pro spouštění většiny instrukcí JVM (bajtkód)
        - Proměnná délka instrukcí s osmibitovým opkódem a proměnným počtem operandů
    - Musí existovat podpora v JVM
        - Jazelle Java Technology Enabling Kit (JTEK)

FPA (ARM Floating Point Accelerator)
-------------------------------
* Podporované formáty hodnot
    - Single
    - Double
    - Extended
* Registry
    - `f0`..`f7`
        - šířka 80bitů
    - `FPSR`
        - Floating Point Status Register
    - `FPCR`
        - Floating Point Control Register
* Podpora pro "rychlé" násobení a dělení
    - Jen pro "single"
    - Nemusí se provést korektní zaokrouhlení

VFP
-------------------------------
* Vector Floating Point (VFP)
* Podpora pro typy half, single a double
    - IEEE 754
* VFPv1
    - Dnes již nepoužívaná
* VFPv2
    - Podpora v ARM instrukcích
* VFPv3
    - Podpora v Thumb a ThumbEE
    - Rozšíření FP registrů na 32

VFP
-------------------------------
* Registry
    - `d0`..`d1`5 (double)
    - `s0`..`s31` (stínové registry pro single)
    - + ve VFPv3 nově i `d16`..`d31` (double)
* SIMD operace (s vektory)
    - 8 x single
    - 4 x double
    - mohou se provádět na jediné FP jednotce
    - stále však rychlejší než skalární operace

VFP
-------------------------------
* Vektory
    - 8 x single (viz předchozí slide)
        - Rozdělení na banky:
         ```
            s0..s7
            s8..s15
            s16..s23
            s24..s31
         ```
    - 4 x double
        - Rozdělení na banky:
         ```
            d0..d3
            d4..d7
            d8..d11
            d12..d15
         ```

VFP
-------------------------------
* Wrapping:
    - vektor s délkou 6 začínající na s5:
        - `[s5, s6, s7, s0, s1, s2]`
* Stride
    - vektor s délkou 3, stride 2 začínající na s1:
        - `[s1, s3, s5]`
    - vektor s délkou 4, stride 2 začínající na s6:
        - `[s6, s0, s2, s4]`
* Wrapping a stride nesmí způsobit, že se registr ve vektoru ocitne 2x!
    
VFP
-------------------------------
* Instrukce
    - Aritmetické 
    - Konverze (single » double, integer » FP atd.)
    - FP MAC (Multiply and Accumulate)
    - √
    - Fixed point (» single, » double a naopak)

VFP
-------------------------------
* VFPv3-FP16
* VFPv3-D16-FP16
* VFPv4
    - Volitelná podpora 16bitových FP (Half precision)

Advanced SIMD Architecture
-------------------------------
* SIMD
    - Jedna instrukce aplikovaná na vektor dat
* Použití
    - Zpracování audia
    - Zpracování obrazu a videa
    - 3D grafika
    - Speech processing
* Banku registrů určených pro SIMD operace
    - Používají se i pro VFP
    - 32bit FP (jednoduchá přesnost)
    - 8bit, 16bit, 32bit, 64bit celá čísla
    - 8bit, 16bit, 32bit, 64bit bitová pole

NEON
-------------------------------
* Instrukce se provádí v jiné jednotce
    - Vlastní fronta instrukcí
    - Nezávislé na hlavní ALU
    - U některých jader více NEON jednotek
* 32 nových registrů
    - `d0`..`d31` (64bitů/registr)
* Sdružení registrů do párů
    - `q0`..`q15` (128 bitů/pár)
* Vektory
    - 8x8 bitů (obrazová data)
    - 4x16 bitů (zvukové vzorky)
    - 2x32 bitů
    - float/single

NEON
-------------------------------
Datové typy
* Unsigned integer
    - 8, 16, 32, 64b
* Signed integer
    - 8, 16, 32, 64b
* Floating point
    - jen 32b

NEON Intrinsic
-------------------------------
```
gcc   -mcpu=cortex-a9 -mfpu=neon ...
clang -mcpu=cortex-a9 -mfpu=neon ...
-mtune=cortex-a5 (a8, a9)
```

```c

#include <arm_neon.h>
(typ)x(lanes)_t - uint8x4_t
(typ)x(lanes)x(počet_registrů)_t - uint8x2x4_t

uint16x4_t vadd_u16(uint16x4_t x, uint16x4_t y);
uint16x2_t vmlal_u32(uint64x2_t x, uint32x2_t, uint32x2_t);
```

* Naměřený výpočetní výkon
    - Funkce rgb2gray
    - Čisté céčko - 48 sekund
    - Intrinsics  - 8.8 sekund (cca 5x rychlejší)

===========================
Omezení některých jader ARM
===========================

FP
--
* FPU je volitelnou součástí
* Cortex-M4
    - jen float (single), nikoli double
    - pozor na to, že překladač může mezivýpočty provádět v double!
        - `-Wdouble-promotion`
        - `-fsingle-precision-constant`
* FP v obsluze přerušení
    - pokud se nepoužije -> Lazy Stacking
* `__FPU_USED` - pokud je definováno:
    - FPU se povolí automaticky ve funkci `SystemInit()`
    - nepatrně větší spotřeba

"Skryté" výpočty s double
-------------------------
```
test.c: In function ‘calcVAT’:
test.c:3:16: warning: implicit conversion from ‘float’ to ‘double’ to match other operand of binary expression [-Wdouble-promotion]
     return 20.0*price;
                     ^
```

Lazy stacking
-------------
* Použito například na Cortex-M4F
* Rutiny pro obsluhu přerušení
* Neprovádí se úschova FP registrů na zásobník, když
    - FPU se nepoužívá v přerušovací rutině
    - nebo
    - FPU se nepoužívá v přerušeném programu

C knihovny
----------
* ARM cc/Keil
    - std.C
        důraz větší výpočetní výkon
    - MicroLib
        důraz na menší paměťové nároky
* gcc
    - NewLib
    - NewLib-Nano

