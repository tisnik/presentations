# Mikroprocesory ARM

* Pavel Tišnovský
    - `tisnik 0x40 centrum 0x2e cz>`
* Datum: 2015-02-07
* Prezentace:
    - [https://tisnik.github.io/presentations/installfest2015/arm.html](https://tisnik.github.io/presentations/installfest2015/arm.html)
* Zdrojový kód prezentace ve formátu Markdown:
    - [https://github.com/tisnik/presentations/blob/master/installfest2015/arm.md](https://github.com/tisnik/presentations/blob/master/installfest2015/arm.md)
* Zdrojový kód prezentace v plain textu:
    - [https://github.com/tisnik/presentations/blob/master/installfest2015/arm/arm.txt](https://github.com/tisnik/presentations/blob/master/installfest2015/arm/arm.txt)


## Obsah přednášky

* Základní informace o mikroprocesorech ARM
* Stručná historie vývoje architektury ARM
* Původní instrukční sada ARM (ARM-32)
* Instrukční sada Thumb
* Instrukční sada Thumb-2
* Příklady využití ARM
* Mikroprocesory ARM ve funkci mikrořadičů
* AArch64

## Základní informace o ARM CPU

* Název ARM
    - 1983 - Acorn RISC Machine
    - 1990 - Advanced RISC Machines
    - V současnosti označení pravděpodobně nejpopulárnější architektury procesorů RISC

## Jádro ARM

* Součástí mnoha historických i současných čipů
    - „Od topinkovačů po servery“
    - Výkonné mikrořadiče
    - Herní konzole
    - Tablety
    - Netbooky
    - Mobilní telefony
    - Postupná adaptace i na serverech

## ARM + další rozšiřující moduly

* Klasické procesory ARM
    - 32bitová instrukční sada RISC
* Další rozšíření
    - Instrukční sada Thumb (16 bitů)
    - Instrukční sada Thumb-2
    - Jazelle DBX (pro bajtkód JVM)
    - AArch64
* MMU
* Vektorový FPU
* GPU

## Obchodní model ARM vs.Intel/AMD

* Tradiční model mainstreamových výrobců
    - „Jedna velikost padne všem“
    - Relativně malé množství současně nabízených modelů CPU (10?)
* Jedna společnost (Intel či AMD)
    - Návrh architektury čipu
    - Výroba
    - Distribuce
* ARM
    - Vlastní know-how a IP
    - Nevyrábí vlastní procesory
    - Namísto toho prodává IP dalším společnostem
        - Samsung
        - Qualcomm
        - NVidia
        - Nintendo
        - Texas Instruments
        - dalších cca 15 důležitých zákazníků

## Přednosti architektury ARM

* Relativně malý počet tranzistorů
* Malá spotřeba (MIPS/Watt)
* Možnost získat licenci a zařadit jádro ARM do vlastního čipu
    - NVidia Tegra
    - OMAP
    - ...
* Dobrá podpora překladači
    - Dnes i dobrá podpora ve VM (JIT)
* Linux & ARM
    - Ekonomicky výhodné spojení technologií

## Stručná historie vývoje architektury ARM

* Projekt Acorn RISC Machine
    - Acorn Computers Ltd.
    - Původní počítače založeny na MOS 6502
* Potřeba výkonnějšího a levnějšího CPU
    - Konkurence k PC (1981)
    - Později též konkurence k dalším počítačům
        - Atari ST
        - Amiga
        - Apple Macintosh

## Výpočetní výkon čipů s architekturou CISC

* Intel 80286 @ 8 MHz
    - ~1,2 MIPS pro 16bitové operace
* Motorola 68000 @ 8MHz
    - ~1 MIPS pro 16bitové operace
    - ~1/2 MIPS pro 32bitové operace
    - ~2 MIPS maximum v syntetických testech

## Projekt Acorn RISC Machine

* Steve Furber a Sophie Wilson
* Studie architektury Berkeley RISC
    - „Pokud skupinka studentů dokáže vytvořit plnohodnotný 32bitový procesor, nebude mít společnost Acorn vůbec žádný problém“
* RISC = nejenom „studentský CPU“

## Jádra ARM1/ARM2

* CPU bez mikrokódu a mikrořadiče
* Architektura Load/Store
    - 32bit datová sběrnice
    - 26bit adresová sběrnice
    - PC jen 24 bitů
        - proto kód v 64MB prostoru
        - (později 26b, nakonec 32b)
* 27 (později 37) 32bitových registrů
    - Některé mají speciální funkci
* Fixní délka operačních kódů 32bitů
* 1 instrukce/takt
    - (kromě skoků a MUL)

## Výsledek - analýza+benchmarky

* Intel 80286 @ 8 MHz
    - ~1,2 MIPS pro 16bitové operace
* Motorola 68000 @ 8MHz
    - ~1 MIPS pro 16bitové operace
    - ~1/2 MIPS pro 32bitové operace
    - ~2 MIPS maximum pro syntetické testy
* ARM2 @ 8MHz
    - ~4,5 MIPS pro 32bitové operace
* ARM3
    - výkonnostně překonal Intel 80286 a to i nejvyšší model @ 25 MHz

## Výpočetní výkon však není vše

* Intel 80286
    - 134 000 tranzistorů
* Motorola 68000
    - 68000 tranzistorů
* ARM2
    - 30000 tranzistorů

## Důsledky použití architektury RISC

* Počítače s ARM(2) se spoléhaly na hrubou výpočetní sílu CPU
* Orientace na 3D operace
    - x Amiga + Atari ST potřeba koprocesorů
    - BLITTER, Agnus, Denise...
        - Orientace na rastrové 2D operace

## ARM family, architecture, core

* Rodina
    - Nejhrubší dělení
    - Dnes označuje určení čipů
        - Cortex-M
        - Cortex-R
        - Cortex-A (32/64)
        - SecurCore
* Architektura
    - Určuje vlastnosti jádra CPU
* Core (jádro)
    - Společné moduly (cache, MMU, ...)
    - Pro jednu architekturu odlišné
      vlastnosti (velikost cache atd.)

## ARM family, architecture, core

* Příklad
    - ARM11
        - ARMv6
        - ARMv6T2
        - ARMv6Z
        - ARMv6K
    - Cortex-M
        - ARMv6-M
            - Cortex-M0
            - Cortex-M0+
            - Cortex-M1
        - ARMv7-M
            - Cortex-M3
        ...

## Architektury a čipy ARM

```
ARMv1     26/32 bitů  ARM1
ARMv2     26/32 bitů  ARM2, ARM3
ARMv3     26/32 bitů  ARM6, ARM7
ARMv4     26/32 bitů  ARM8
ARMv5     32 bitů     ARM7EJ, ARM9E, ARM10E
ARMv6     32 bitů     ARM11
ARMv6-M   32 bitů     Cortex-M0, Cortex-M0+, Cortex-M1
ARMv7-M   32 bitů     Cortex-M3
ARMv7E-M  32 bitů     Cortex-M4, Cortex-M7
ARMv7-R   32 bitů     Cortex-R4, Cortex-R5, Cortex-R7
ARMv7-A   32 bitů     Cortex-A5, Cortex-A7, Cortex-A8,
                      Cortex-A9, Cortex-A12,
                      Cortex-A15, Cortex-A17
ARMv8-A   32/64 bitů  Cortex-A53, A57 a A72
```

## Architektury a čipy ARM - využití

```
ARMv1      proof of concept, funkční hned první "várka"
ARMv2      Acorn Archimedes, 1982
ARMv3     
ARMv4      StrongARM
ARMv5     
ARMv6      Starší (univerzální) čipy, dnes RPI apod.
ARMv6-M    Mikrořadič
ARMv7-M    Mikrořadič
ARMv7E-M   Mikrořadič
ARMv7-R    Real-time aplikace
ARMv7-A    netbooky, smartphony, tablety, čtečky, desktop
ARMv8-A    servery
```

## Rodina ARM1

* Architektura ARMv1
    - Jádro ARM1
    - První implementace jádra ARM
    - Bez HW násobičky
    - Bez MMU a bez cache
    - Proof of concept
        - Nebyl použit v žádném komerčním produktu

## Rodina ARM2

* Architektura ARMv2
    - Jádro ARM2
    - První komerčně používané čipy ARM
* Novinky architektury ARMv2
    - Oproti ARM1 byla přidána HW násobička
* Základní parametry
    - Typická frekvence 8 MHz
    - Výkon přibližně 4 MIPS

## Rodina ARM2 (pokr.)

* Architektura ARMv2a
    - Založeno na ARMv2 (původně jádro ARM2)
    - Nyní jádro A250
* Novinky architektury ARMv2a
    - Jádro A250
    - Integrovaná jednotka MMU
    - Nové instrukce
    - Grafický I/O procesor
* Základní parametry
    - Frekvence až 12 MHz
    - Výkon průměrně 7 MIPS

## Rodina ARM3

* Stále architektura ARMv2a
* Jádro ARM3
* Postupně rostoucí hodinová frekvence
    - ARM250: 12 MHz
    - ARM3: 25 MHz
* Operační paměť se stává úzkým hrdlem architektury
    - Řešení typické pro RISC: použití cache
    - 4 kB cache v případě jádra ARM3 (D+I)
* Základní parametry
    - Frekvence až 25 MHz
    - Výkon průměrně 12 MIPS

## Rodina ARM6

* Architektura ARMv3
* Novinky rodiny ARM6
    - Podpora pro plně 32bitové adresování
      (dříve 24, 26 bitů)
    - Volitelná cache podle jádra (0, 4 kB)
* Základní parametry
    - Frekvence až 33 MHz
    - Výkon průměrně 28 MIPS
* V některých zařízeních stále používán

## Rodina ARM7

* Velmi úspěšná rodina čipů ARM
* Novinky rodiny ARM7
    - JTAG (ARM7DI)
        - Snazší ladění, hw breakpointy...
    - Thumb 16bit (u čipů s „T“ v názvu)
        - ARM7-TDMI
    - MMU (v závislosti na čipu)
    - Cache 8 kB (v závislosti na čipu)

## Rodina StrongARM

* Architektura ARMv4
* Společnost DEC + Adv. ARM Machines
    - Později prodáno firmě Intel
        - Náhrada za i860 a i960
    - StrongARM → XScale
* Zaměření čipu
    - PDA
    - Set-top boxy
    - (Apple MessagePad 2000)
    - (Acorn Computers RISC PC)
* Hodinové frekvence 100..233 MHz

## ARM ve funkci mikrořadiče

* Cortex-M0
* Cortex-M0+
* Cortex-M1
* Cortex-M3
    - Arduino Due
* Cortex-M4
* Cortex-M7

## Jádra v řadě Cortex-Mx

```
Jádro       Architektura
Cortex-M0   ARMv6-M    Von Neumann
Cortex-M0+  ARMv6-M    Von Neumann
Cortex-M1   ARMv6-M    Von Neumann
Cortex-M3   ARMv7-M    Harvardská
Cortex-M4   ARMv7E-M   Harvardská
Cortex-M7   ARMv7E-M   Harvardská
```

## Jádra v řadě Cortex-Mx (pokr.)

```
Jádro       Dělička DSP Thumb             Thumb-2
Cortex-M0     ne    ne  kromě 3 instrukcí částecně
Cortex-M0+    ne    ne  kromě 3 instrukcí částecně
Cortex-M1     ne    ne  kromě 3 instrukcí částecně
Cortex-M3     ano   ne  kompletně         kompletně
Cortex-M4     ano   ano kompletně         kompletně
Cortex-M7     ano   ano kompletně         kompletně
```

## Cortex-M0

* Jádro "naprogramované" ve Verilogu
* ARM čipy s nejnižší cenou, rozměry, výkonem, příkonem
    - Malá plocha čipu
    - Nejmenší čip má rozměry 1,6x2 mm
    - Pipeline se třemi řezy
* Instrukční sada
    - Thumb (chybí jen tři instrukce)
    - částečně Thumb-2
    - Nikoli A32!
* M0 je skutečný mikrořadič
    - Náhrada za některé 8bitové a 16bitové MCU
    - von Neumannova architektura
    - Násobička
        - jednocyklová (high perf. čipy)
        - 32cyklová (čipy s nižší cenou a příkonem)
    - Power management
        - Režim sleep (CLK=0 Hz)
        - Režim deep sleep (vypnutí flash paměti apod.)

## Cortex-M0+

* Kompatibilní s M0
* Ještě menší spotřeba
* Pipeline se dvěma řezy (tři v M0)

## MCU a Thumb?

* Je strojový kód RISCových procesorů skutečně prostorově neefektivní?
    - PIC16 a PIC18
        - 14bitové a 16bitové instrukce
        - osmibitové operandy
    - 8051
        - 8, 16, 24 bitů/instrukci
        - většinou jen osmibitové operandy
    - Thumb
        - 16 a 32 bitů/instrukci
        - 32bitové operandy

## Cortex-M7

* Nejvýkonnější řada DSP
    - Superskalární, 6řezová pipeline
    - Prediktor skoků
    - MAC s 16/32bitovými operandy v jednom cyklu
    - HW dělička (2-12 cyklů)
* Floating point
    - single
    - double
* SIMD
* D-cache až 64kB
* I-cache až 64kB
* TCM
    - Tightly Coupled Memory
* ECC
* Režimy Sleep a Deep Sleep

## ARM pro spotřební elektroniku

* Cortex-A
    - 32bitové CPU
        - 2005    Cortex-A8
        - 2007    Cortex-A9
        - 2009    Cortex-A5
        - 2010    Cortex-A15
        - 2011    Cortex-A7
        - 2013    Cortex-A12
        - 2014    Cortex-A17
    - 64bitové CPU
        - 2012    Cortex-A53
        - 2012    Cortex-A57
        - 2015    Cortex-A72

## ARM pro real-time aplikace

* Cortex-R4
* Cortex-R5
* Cortex-R7
* Poměrně výkonná jádra
    - Cortex-R4 1,4 GHz
* DSP
* HW dělička
* SIMD
* FPU

## Mikroprocesory ARM s 64bitovou architekturou

* 32bitů -> 64bitů
* Pravděpodobně největší změna v architektuře procesorů ARM v celé jejich historii
* Velké odlišnosti, nutnost překladu pro novou architekturu

## Změna označování

* Původní architektura: AArch32 (málokdy využíváno)
* Nová architektura: AArch64

## Proč AArch64?

* Nové možnosti nasazení těchto procesorů
     - "Od topinkovačů po superpočítače" :-)
* Požadavky zákazníků
     - Nutnost dobrého načasování
     - Konec roku 2011
* Větší virtuální paměťový prostor
* Nativní práce s 64bitovými hodnotami
* Zjednodušení pro vývojáře i autory překladačů/VM
     - Čistý návrh load/store RISC
     - Jen několik instrukcí obsahuje podmínku
     - Větší množina dostupných registrů

## Rodina ARMv8-A

* Zaručena zpětná kompatibilita s ARMv7-A
* Podporuje AArch32 i AArch64
* Současné čipy ARMv8-A
     - Cortex-A53
     - Cortex-A57
     - Cortex-A72

## ARM32 z pohledu programátora

* Architektura typu Load-Store
    - Pro efektivní práci nutný velký počet registrů
    - Omezení přístupů do pomalé paměti
    - Alokace registrů → optimalizující překladač
* Řešení
    - 27/37 registrů
        - 30 pracovních, `PC`, `CPSR`, 5x`SPSR`
        - 15 registrů viditelných `r0`..`r14`
        - `r13` Stack Pointer
        - `r14` Link Register
    - Šířka registrů 32 bitů
    - Rozdělení do banků, které se překrývají
    - Pro každý stav procesoru zvláštní bank

## Instrukční sady procesorů ARM

* A32
    - 32bitové instrukce, 32bitové operandy
* Thumb (T32)
    - 16bitové instrukce
* Thumb-2
    - Mix 16 a 32bitových instrukcí
* A64
    - 32bitové instrukce, 64bitové operandy

## Instrukční sada A32

* Původní instrukční sada procesorů ARM
* Konstantní šířka instrukcí 32bitů
* Šířka zpracovávaných dat taktéž 32 bitů
    - Problém s načítáním konstant
    - Musí se řešit na každé architektuře RISC

## Typy instrukcí

* Load-store (jeden registr)
* Load-store (více registrů)
* Aritmetické operace
* Logické a bitové operace
* Skoky a změna režimu procesoru
* Práce se stavovými registry `CPSR` a `SPSR`
* Práce se semafory
* Instrukce koprocesoru(ů)

## Vlastnosti ISA typické pro ARM

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

## Velmi často používaný příklad

```C
int gcd(int a, int b) {
   while (a != b) {
      if (a > b) a = a - b;
      else       b = b - a;
   }
   return a;
}
```

## Klasický přístup

```
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

## Využití příznaků

```
 gcd
        CMP      r0, r1
        SUBGT    r0, r0, r1
        SUBLT    r1, r1, r0
        BNE      gcd
```

## Výsledky

* Klasický přístup
    - 7 instrukcí
    - 28 bajtů
    - 13 taktů (branch=vyprázdnění cache=3 takty)
* Využití podmíněných instrukcí
    - 4 instrukce
    - 16 bajtů
    - 10 taktů (pouze jeden branch)
* Thumb (viz další slajdy)
    - 7 instrukcí
    - 14 bajtů (16bit/instrukci)

## Instrukční sada Thumb (T32)

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

## Instrukční sada Thumb (T32)

* Thumb neumožňuje podmníněné provádění instrukcí
* Jen podmíněné skoky
* Skoky
    - Branch
    - Branch and link
* Aritmetické a logické operace
    - `OP Rd, Rn, Rm`
        - omezení na `r0`..`r7`
        - tři bity pro výběr registru v instr.slovu
    - Výjimky
        - `ADD Rd, Rn`, konstanta
        - `ADD Rd, Rm` - jeden z registrů `r8`..`r15`
        - `CMP Rm, Rn` - dtto
        - `MOV Rd, Rm` - dtto

## Instrukční sada Thumb (T32)

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
    - `B`,   `BL`,   `BX`,  `BLX` (link, exchange)
* Přesuny dat
    - `MOV`, `MVN` - move (not)
    - `POP`, `PUSH`
* Operace typu LOAD a STORE
    - `LDR`, `LDRH`, `LRRB`
        - load (word, halfword, byte)
    - `LDRSH`, `LDRSB`
        - sign extend (na word)
    - `STR`, `STRH`, `STRB`
        - store (word, halfword, byte)
    - `LDMIA`, `STMIA`
        - vektor registrů 
    - `STXH`, `STXB`, `UXTH`, `UXTB`
        - sign/zero extend

## Instrukční sada Thumb-2

* 2003
* ARMv7
* Povoluje kombinace instrukcí o šířce 16 a 32 bitů
* Zpětná kompatibilita s Thumb
* Větší složitost čipů
* Větší „hustota“ strojového kódu
    - Srovnatelná s Thumb
* Má smysl ve světě rychlých CPU, pomalých DRAM a drahých cache
* Výkonnost srovnatelná s ARM režimem

## Instrukční sada Thumb-2

* Bitové operace
    - Bit Field Clear
    - Bit Field Insert
* `IT`
    - Instrukce odpovídající konstrukci if-then-else
    - (viz následující slajd)
* `CBZ`
    - Compare and Branch on Zero
* `CBNZ`
    - Compare and Branch on Non-Zero

## IT

* `IT{pattern} {condition}`
    - až čtyři instrukce provedené na základě testu
    - (pozitivní/negativní výsledek)
* {pattern}
    - `T`-then
    - `E`-else
* první instrukce
    - provedena při splnění podmínky {condition}
* druhá instrukce
    - `T`-podmínka
    - `E`-inverze podmínky
* třetí a čtvrtá instrukce
    - dtto
* {condition}
    - `EQ` `NE` `GT` `GE` `LT` `LE`
    - `CS` `CC`  carry
    - `PL` `MI` `HI` `LS`

## IT

```
CMP r0, r1
ITE EQ
MOVEQ r0, r2 ; větev "then"
MOVNE r0, r3 ; větev "else"
```

## Instrukční sada A64

* 32bitů -> 64bitů
* Pravděpodobně největší změna v architektuře procesorů ARM v celé jejich historii
* Velké odlišnosti, nutnost překladu pro novou architekturu

## AArch64 z pohledu programátora

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

## Operace

* 32bitové
    - horních 32 bitů zdrojových registrů ignorováno
    - horních 32 bitů cílového registru vynulováno
* 64bitové

## Multiply/divide

* signed
* unsigned
* 32x32 -> 32
* 64x64 -> 64
* 64+32x32 -> 64 (multiply and accumulate)
* 64x64 -> 64+64 (registrový pár)

## Skoky a rozeskoky

* +- 1MB pro podmíněné skoky
* +- 128MB pro nepodmíněné skoky

## Instrukce s podmínkou

* Již nejsou podporovány
    - Založeno na výsledcích benchmarků
    - Více bitů v instrukčním slově použitelných pro jiné účely
    - Současné prediktory skoků jsou již velmi kvalitní
    - Podmínky mohou být použity jen u některých instrukcí

## Podpora pro operace s FP

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
## SIMD

* Režim kompatibility s IEEE 754

## Crypto

* AES
* SHA-1
* SHA-256

## Rozšíření instrukčních sad

* FPA
* VFP
* Advanced SIMD Architecture
* NEON (Advanced SIMD)
* Jazelle
    - Podpora pro spouštění většiny instrukcí JVM (bajtkód)
        - Proměnná délka instrukcí s osmibitovým opkódem a proměnným počtem operandů
    - Musí existovat podpora v JVM
        - Jazelle Java Technology Enabling Kit (JTEK)

## FPA (ARM Floating Point Accelerator)

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

## VFP

* Vector Floating Point (VFP)
* Podpora pro typy half, single a double
    - IEEE 754
* Registry
    - `d0`..`d15`
    - `s0`..`s31` (stínové registry pro single)
* SIMD operace (s vektory)
    - 8*single
    - 4*double
    - mohou se provádět na jediné FP jednotce
    - stále však rychlejší než skalární operace

## VFP

* VPFv1
    - Dnes již nepoužívaná
* VPFv2
    - Podpora v ARM instrukcích
* VPFv3
    - Podpora v Thumb a ThumbEE
    - Rozšíření FP registrů na 32

## Advanced SIMD Architecture

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

## NEON

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

## NEON Intrinsic

```
gcc   -mcpu=cortex-a9 -mfpu=neon ...
clang -mcpu=cortex-a9 -mfpu=neon ...
-mtune=cortex-a5 (a8, a9)
```

```C
#include <arm_neon.h>
(typ)x(lanes)_t - uint8x4_t
(typ)x(lanes)x(počet_registrů)_t - uint8x2x4_t
...
uint16x4_t vadd_u16(uint16x4_t x, uint16x4_t y);
uint16x2_t vmlal_u32(uint64x2_t x, uint32x2_t, uint32x2_t);
```

## NEON Intrinsic

* Naměřený výpočetní výkon
    - Funkce rgb2gray
    - Čisté céčko - 48 sekund
    - Intrinsics  - 8.8 sekund (cca 5x rychlejší)

## Raspberry Pi

* Model B+
    - SoC BCM2835
        - CPU + GPU
    - 512 MB RAM
        - "nasazena" na SoC
    - 4xUSB konektor
    - Ethernet
    - HDMI + TV výstup
    - Audio výstup
    - MicroSD + Externí HDD (over USB)

## Raspberry Pi: SoC

* CPU
    - Rodina ARM11
    - Instrukční sada ARMv6
    - 700 MHz
    - Lze snadno přetaktovat až na 1 GHz
    - Poměrně slabý výkon pro desktopové aplikace
* GPU
    - HVS - Hardware Video Scaler
    - 24 GFLOPS
    - silný zejména v GPU výpočtech (x desktop)

