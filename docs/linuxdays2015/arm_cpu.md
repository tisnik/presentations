Architektury moderních procesorů a mikrořadičů ARM
==================================================
* Autor    Pavel Tišnovský, Red Hat
* Email    <ptisnovs 0x40 redhat 0x2e com>
* Datum    2015-10-10

Obsah přednášky (1)
-------------------------------
* Základní informace o mikroprocesorech ARM
* Rozšíření čipů ARM ve světě
* Přednosti architektury ARM
* Architektury čipů ARM
* Rodiny jader ARM (starší dělení)
    - ARM1
    - ARM2
    - ARM3
    - ARM6
    - ARM7 (+ ARM7T)
    - ARM11
* Rodiny jader ARM podle nového dělení
    - Cortex-A
    - Cortex-R
    - Cortex-M

Obsah přednášky (2)
-------------------------------
* ARM pro mikrořadiče
    - Jádra v řadě Cortex-M
* ARM pro spotřební elektroniku
    - Jádra v řadě Cortex-A
* AArch64 (ARMv8-A)
* Příklady použití čipů s jádrem ARM
    - nRF51822 (Cortex-M0)
      (BBC Micro Bit)
    - Atmel SAM3X8E ARM Cortex-M3
      (Arduino Due)
    - BCM2835 (single core)
      (Raspberry Pi)
    - BCM2836 (quad core)
      (Raspberry Pi 2)
    - Dual-Core ARM11 MPCore + single-core ARM9
      (Nintendo 3DS)

Základní informace o ARM CPU
-------------------------------
* Název ARM
    - 1983 - Acorn RISC Machine
    - 1990 - Advanced RISC Machines
    - 1998 - ARM Holdings
    - V současnosti označení pravděpodobně
      nejpopulárnější architektury procesorů RISC

Jádro ARM
-------------------------------
* Součástí mnoha historických i současných čipů
    - „Od topinkovačů po servery“
    - Výkonné mikrořadiče
    - Herní konzole
    - Tablety
    - Netbooky
    - Mobilní telefony
    - Postupná adaptace i na serverech

ARM + další rozšiřující moduly
-------------------------------
* Klasické procesory ARM
    - 32bitová instrukční sada RISC
    - Nově označovaná A32
* Další rozšíření
    - Instrukční sada Thumb (16 bitů)
    - Instrukční sada Thumb-2
    - Jazelle DBX (pro bajtkód JVM)
    - AArch64
    - SIMD
    - NEON (Advanced SIMD)
* MMU
* MPU (zjednodušená varianta MMU bez virtualizace)
* Vektorový FPU
* GPU

Obchodní model ARM vs.Intel/AMD
-------------------------------
* Tradiční model mainstreamových výrobců
    - „Jedna velikost padne všem“
    - Relativně malé množství současně nabízených modelů CPU (10?)
* Jedna společnost (Intel či AMD)
    - Návrh architektury čipu
    - Výroba
    - Distribuce
* Začátek tohoto modelu:
    - Intel 386
    - Andrew Grove
    - "single source"
    - pouze několik "fabs" vlastněných Intelem
        • Santa Clara
        • Hillsboro
        • Chandler

Obchodní model ARM vs.Intel/AMD
-------------------------------
* ARM
    - Vlastní know-how a IP
    - Nevyrábí vlastní procesory
    - Namísto toho prodává IP dalším společnostem
        • Samsung
        • Qualcomm
        • NVidia
        • Nintendo
        • Texas Instruments
        • dalších cca 15 důležitých zákazníků
          (oficiální seznam není zveřejněn)
    - ⇒ Veškerý zisk je možné investovat do návrhu čipů

Zajímavé akvizice ARM
-------------------------------
2005 Keil software
     překladače pro různé MCU
2006 Falanx (ARM Norway)
     3D akcelerátory
2013 Sensinode
     startup, IoT

Rozšíření čipů s jádrem ARM
-------------------------------
Rok           Čipů
1997        9 000 000
1998       51 000 000
1999      175 000 000
2000      367 000 000
2001      420 000 000
2002      456 000 000
2003      782 000 000
2004    1 272 000 000
2005    1 662 000 000
2006    2 400 000 000
2007    2 900 000 000
2008    4 000 000 000
2009    3 900 000 000
2010    6 100 000 000
2011    7 900 000 000
2012    8 700 000 000
2013   10 000 000 000
2014   12 000 000 000
2015                ?

Rozšíření čipů s jádrem ARM
-------------------------------
Rok 2010
    6 100 000 000 čipů
    95% smartphony
    10% přenosné počítače
    35% TV a set-top boxy
     0% desktopy
     0% servery :-)
Rok 2014
    12 000 000 000 čipů
    predikce pro 23% ARM na PC

Přednosti architektury ARM
-------------------------------
* Relativně malý počet tranzistorů
* Malá spotřeba (MIPS/Watt)
* Možnost získat licenci a zařadit jádro ARM do vlastního čipu
    - NVidia Tegra
    - OMAP
    - ...
* Tři rodiny čipů pro různé aplikace
    - Mikrořadiče
    - Smartphone/tablety/PC/konzole
    - Realtime aplikace (včetně DSP apod.)
    - Servery
* Dobrá podpora překladači
    - Dnes i dobrá podpora ve VM (JIT)
* Linux & ARM
    - Ekonomicky výhodné spojení technologií

ARM family, architecture, core
-------------------------------
* Rodina
    - Nejhrubší dělení
    - Dnes označuje určení čipů
        • Cortex-M
        • Cortex-R
        • Cortex-A (32/64)
        • SecurCore
* Architektura
    - Určuje vlastnosti jádra CPU
* Core (jádro)
    - Společné moduly (cache, MMU, ...)
    - Pro jednu architekturu odlišné
      vlastnosti (velikost cache atd.)

ARM family, architecture, core
-------------------------------
* Příklad
    - ARM1
        - ARMv1
            - ARM1
    - ARM11
        • ARMv6
            • ARM1136
        • ARMv6T2
            • ARM1156
        • ARMv6Z
            • ARM1176
        • ARMv6K
            • ARM11MPcore
    - Cortex-M
        • ARMv6-M
            • Cortex-M0
            • Cortex-M0+
            • Cortex-M1
        • ARMv7-M
            • Cortex-M3
        ...

Architektury a čipy ARM
-------------------------------
Architektura          Jádra
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

Architektury a čipy ARM - využití
-------------------------------
ARMv1      proof of concept, funkční hned první "várka"
ARMv2      Acorn Archimedes, 1982
ARMv3     
ARMv4      StrongARM
ARMv5     
ARMv6      Starší (univerzální) čipy, dnes RPI apod.
ARMv6-M    Mikrořadič, malá spotřeba, malý výkon
ARMv7-M    Mikrořadič, "zlatá střední cesta"
ARMv7E-M   Mikrořadič, vysoký výkon, složitější čip
ARMv7-R    Real-time aplikace
ARMv7-A    netbooky, smartphony, tablety, čtečky, desktop
ARMv8-A    servery

Rodina ARM1
-------------------------------
* Architektura ARMv1
    - Jádro ARM1
    - První implementace jádra ARM
    - Bez HW násobičky
    - Bez MMU a bez cache
    - Proof of concept
        • Nebyl použit v žádném komerčním produktu

Rodina ARM2
-------------------------------
* Architektura ARMv2
    - Jádro ARM2
    - První komerčně používané čipy ARM
* Novinky architektury ARMv2
    - Oproti ARM1 byla přidána HW násobička
* Základní parametry
    - Typická frekvence 8 MHz
    - Výkon přibližně 4 MIPS

ARM1+ARM2 (společné vlastnosti)
-------------------------------------
* CPU bez mikrokódu a mikrořadiče
* Architektura Load/Store
    - 32bit datová sběrnice
    - 26bit adresová sběrnice
    - PC jen 24 bitů
        • proto kód v 64MB prostoru
        • (později 26b, nakonec 32b)
* 27 (později 37) 32bitových registrů
    - Některé mají speciální funkci
* Fixní délka operačních kódů 32bitů
* 1 instrukce/takt
    - (kromě skoků a později MUL)
* Většina instrukcí může být vykonána za určité podmínky
    GT, GE, EQ atd.

Rodina ARM2 (pokr.)
-------------------------------
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

Rodina ARM3
-------------------------------
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

Rodina ARM6
-------------------------------
* Architektura ARMv3
* Novinky rodiny ARM6
    - Podpora pro plně 32bitové adresování
      (dříve 24, 26 bitů)
    - Volitelná cache podle jádra (0, 4 kB)
* Základní parametry
    - Frekvence až 33 MHz
    - Výkon průměrně 28 MIPS
* V některých zařízeních stále používán

Rodina ARM7
-------------------------------
* Velmi úspěšná rodina čipů ARM
* Novinky rodiny ARM7
    - JTAG (ARM7DI)
        • Snazší ladění, hw breakpointy...
    - Thumb 16bit (u čipů s „T“ v názvu)
        • ARM7-TDMI (viz další slide)
    - MMU (v závislosti na čipu)
    - Cache 8 kB (v závislosti na čipu)

ARM7 vs ARM7T
-------------------------------
* ARM7
    - A32
    - ARMv3
* ARM7T
    - A32+Thumb
    - ARMv4T
* ARM7TDMI
    ARM7 +    _T_humb + 
     JTAG     _D_ebug +
     fast     _M_ultiplier + 
     enhanced _I_CE  (debug support)
        (nastaveni podmínek, kdy se aktivuje
         breakpoint či watchpoint)
    Licencováno TI
    Nokia 6110

Rodina StrongARM
-------------------------------
* Architektura ARMv4
* Společnost DEC + Adv. ARM Machines
    - Později prodáno firmě Intel
        • Náhrada za i860 a i960
    - StrongARM → XScale
* Zaměření čipu
    - PDA
    - Set-top boxy
    - (Apple MessagePad 2000)
    - (Acorn Computers RISC PC)
* Hodinové frekvence 100..233 MHz

ARM11
-------------------------------
* Architektura ARMv6
    - Instrukční sady
        - A32
        - Thumb
        - Thumb-2 (později, od ARM1156)
    - Delší pipeline
        - 8 řezů
        - out-of-order
        - branch prediction
    - SIMD
        - paralelní provádění některých operací

ARM11
-------------------------------
* Čtyři jádra
    - ARM1136
    - ARM1156
        - Thumb-2
    - ARM1176
    - ARM11MPcore
        - multicore
(Raspberry PI a podobná zařízení používají ARM11)

ARM ve funkci mikrořadiče
-------------------------------
* Tři architektury
    - ARMv6-M
        - Cortex-M0
        - Cortex-M0+
        - Cortex-M1
    - ARMv7-M
        - Cortex-M3
    - ARMv7E-M
        - Cortex-M4
        - Cortex-M7

Jádra v řadě Cortex-Mx
-------------------------------
Jádro       Architektura            MPU
Cortex-M0   ARMv6-M    Von Neumann  ne
Cortex-M0+  ARMv6-M    Von Neumann  volitelná
Cortex-M1   ARMv6-M    Von Neumann  ne
Cortex-M3   ARMv7-M    Harvardská   volitelná
Cortex-M4   ARMv7E-M   Harvardská   volitelná
Cortex-M7   ARMv7E-M   Harvardská   volitelná

Jádra v řadě Cortex-Mx (pokr.)
-------------------------------
Jádro       Dělička DSP Thumb             Thumb-2
Cortex-M0     ne    ne  kromě 3 instrukcí částecně
Cortex-M0+    ne    ne  kromě 3 instrukcí částecně
Cortex-M1     ne    ne  kromě 3 instrukcí částecně
Cortex-M3     ano   ne  kompletně         kompletně
Cortex-M4     ano   ano kompletně         kompletně
Cortex-M7     ano   ano kompletně         kompletně

Cortex-M0
-------------------------------
* Jádro "naprogramované" ve Verilogu
* ARM čipy s nejnižší cenou, rozměry, výkonem, příkonem
    - Malá plocha čipu
    - Nejmenší čip má rozměry 1,6x2 mm
    - Pipeline se třemi řezy
* Instrukční sada
    - Thumb (chybí jen tři instrukce)
    - částečně Thumb-2 (ale ne již CBZ, CBNZ či IT)
    - Nikoli A32!

Cortex-M0
-------------------------------
* M0 je skutečný mikrořadič
    - Náhrada za některé 8bitové a 16bitové MCU
    - von Neumannova architektura
    - Násobička
        • jednocyklová (high perf. čipy)
        • 32cyklová (čipy s nižší cenou a příkonem)
    - Power management
        • Režim sleep (CLK=0 Hz)
        • Režim deep sleep (vypnutí flash paměti apod.)
        • Instrukce WFI, WFE
    - 12.5µW na každý MHz @ 1,2V
    - 64µW na každý MHz @ 1,8V

Cortex-M0+
-------------------------------
* Novější čipy
    - vylepšení původních jader M0
* Kompatibilní s M0
* Ještě menší spotřeba
    - 9.8µW na MHz
* Pipeline se dvěma řezy (tři v M0)
* MPU

Cortex-M3
-------------------------------
* Obecně výkonnější čipy než Cortex-M0(+)
* MPU
* HW násobička (1 takt)
* HW dělička (2-16 taktů)
* Instrukční sada
    - Thumb
    - Thumb-2
    - Nikoli A32!

Cortex-M3
-------------------------------
* Booleovský processor
    - Dva vybrané paměťové regiony á 1 MB
    - První region: SRAM
    - Druhý region: periferní zařízení
    - Adresové aliasy: blok 32 MB
        - Každé slovo mapováno do jediného bitu
          (LSB)
* Energetické nároky
    1,2V, 25°C 31 µW/MHz
    1,1V, 25°C 11 µW/MHz
    0,9V, 85°C  8 µW/MHz

Cortex-M7
-------------------------------
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

ARM pro spotřební elektroniku
-------------------------------
* Cortex-A
    - 32bitové CPU
        • 2005    Cortex-A8
        • 2007    Cortex-A9
        • 2009    Cortex-A5
        • 2010    Cortex-A15
        • 2011    Cortex-A7
        • 2013    Cortex-A12
        • 2014    Cortex-A17
    - 64bitové CPU
        • 2012    Cortex-A53
        • 2012    Cortex-A57
        • 2015    Cortex-A72

ARM pro spotřební elektroniku
-------------------------------
Čipy v A-profilu mají MMU
Nutnost pro moderní OS
    - 32bitové CPU
        Architektura ARMv7-A
    - 64bitové CPU
        Architektura ARMv8-A

Cortex-A5
-------------------------------
Low end zařízení
* 800 MHz - 2 GHz
* L1 cache: 4-64kB I + 4-64kB D
* 8řezová pipeline
* A32
* Thumb-2
* Jazelle RCT
* NEON SIMD (volitelné)
* VFPv3     (volitelné)
* Typicky 1-4 jádra na čipu

Cortex-A8
-------------------------------
Použito v různých zařízeních
* 600 MHz - 1 GHz
* L1 cache: 32kB I + 32kB D
* L2 cache: 512kB
* Superskalární architektura
* 13řezová pipeline (Integer)
* 10řezová pipeline (NEON)
* A32
* Thumb-2
* Jazelle RCT
* NEON SIMD
* VFPv3
* 1 jádro na čipu

Cortex-A9
-------------------------------
* 800 MHz - 2 GHz
* L1 cache: 32kB I + 32kB D
* L2 cache: 128kB - 8MB
* Superskalární architektura
* 8řezová pipeline
* A32
* Thumb-2
* Jazelle DBX+Jazelle RCT
* NEON SIMD (volitelné)
* VFPv3     (volitelné)
* Typicky 1-4 jádra na čipu

ARM pro real-time aplikace
-------------------------------
* Cortex-R4
* Cortex-R5
* Cortex-R7
* Poměrně výkonná jádra
    - Cortex-R4 1,4 GHz
* DSP
* HW dělička
* SIMD
* FPU

Mikroprocesory ARM s 64bitovou architekturou
-------------------------------
* 32bitů -> 64bitů
* Pravděpodobně největší změna v architektuře
  procesorů ARM v celé jejich historii
* Velké odlišnosti, nutnost překladu pro novou architekturu

Změna označování
-------------------------------
* Původní architektura: AArch32 (málokdy využíváno)
* Nová architektura: AArch64

Proč AArch64?
-------------------------------
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

Rodina ARMv8-A
-------------------------------
* Zaručena zpětná kompatibilita s ARMv7-A
* Podporuje AArch32 i AArch64
* Současné čipy ARMv8-A
     - Cortex-A53
     - Cortex-A57
     - Cortex-A72

A57
-------------------------------
Instrukce jsou dekódovány do µops
    - Fetch + Decode:  in order
    - Execute (issue): out of order
* Pro issue: osm samostatných pipeline
    - Integer 0           (I0)
    - Integer 1           (I1)
    - Integer Multi-cycle (M)
    - Branch              (B)
    - Load                (L)
    - Store               (S)
    - FP/ASIMD 0          (F0)
    - FP/ASIMD 1          (F1)
* Za cyklus max tři µops
* Load balancing FP operací

Osm samostatných pipeline (pokr.)
-------------------------------
    - Integer Multi-cycle
        Shift
        MUL
        DIV
        CRC
    - FP/ASIMD 0
        všechny FP operace
        crypto
    - FP/ASIMD 1
        ADD, MUL

A57
-------------------------------
* Latence a max. průchodnost (integer)
    ADD    1     2         I0/I1
    Shift  1     1         M
    BLR    2-3   1         I0/I1+B (branch and link)
    CCMP   1     2         I0/I1   (conditional compare)
    MUL    3     1         M
    SDIV   4-20  1/20-1/4  M
    LDR    4     1         L
    STR    1     1         S  (nečeká na zápis)

A57
-------------------------------
* Latence a max. průchodnost (FP)
    VADD   5     2         F0/F1
    VMUL   5     2         F0/F1
    VDIV   7-17  2/15-2/5  F0    (single/float)
    VDIV   7-32  1/30-1/5  F0    (double)
    VSQRT  7-17  2/15-2/5  F0    (single/float)
    VSQRT  7-32  1/30-1/5  F0    (double)
    °
    DIV+SQRT - iterativní algoritmus
             - lze přerušit

Příklady použití čipů s jádrem ARM
==================================================

BBC Micro Bit
-------------------------------
* BBC Computer Literacy Programme
* Nordic Semiconductor nRF51822
    - 16 MHz (+ 32768 Hz)
    - ARM Cortex-M0
* 256KB Flash
* 16KB RAM
* Bluetooth
* USB (On-The-Go)
* Displej z 25 LED
* GPIO
  (Akcelerometr + Magnetometr přes I²C)

Arduino Due
-------------------------------
* ARM Freescale Cortex-A9 + ARM Atmel SAM3X8E CP
* HD video, low power, realtime app
    - 84 MHz
    - 2 x 256 kB Flash ROM
    - 64 + 32 kB SRAM
    - 16 kB ROM
      obsahuje především bootloader rutiny pro UART a USB
    - 54 I/O pinů
      12 z nich vyhrazeno pro PWM
    - 16 kanálový ADC (12 bitů)
      jeden rezervován pro vnitřní senzor teploty
    - 2 DAC (taktéž 12bitů)
    - 3 x USART
    - 9 kanálový 32bitový čítač
    - 2 TWI (Two Wire Interface, varianta I²C)
    - USB Device/Mini host
    - Ethernet MAC 10/100 + podpora pro přenos dat přes DMA
    - True Random Number Generator (TRNG)
      dokáže každých 32 taktů vrátit 32bitové náhodné(?) číslo

Raspberry Pi
-------------------------------
* Model B+
    - SoC BCM2835
        • CPU + GPU
    - 512 MB RAM
        • "nasazena" na SoC
    - 4xUSB konektor
    - Ethernet
    - HDMI + TV výstup
    - Audio výstup
    - MicroSD + Externí HDD (over USB)

Raspberry Pi: SoC
-------------------------------
* CPU
    - Rodina ARM11
    - Instrukční sada architektury ARMv6
    - 700 MHz
    - Lze snadno přetaktovat až na 1 GHz
    - Poměrně slabý výkon pro desktopové aplikace
* GPU
    - HVS - Hardware Video Scaler
    - 24 GFLOPS
    - silný zejména v GPU výpočtech (x desktop)

Raspberry Pi 2
-------------------------------
* CPU
    - SoC BCM2836 (Quad core)
        • ARM Cortex-A7
        • CPU + GPU
    - 900 MHz
    - 1 GB RAM

Nintendo DS
-------------------------------
* CPU
    - ARM946E-S
        • 67 MHz
        • Hry, rendering
    - ARM7TDMI
        • 33 MHz
        • Zvukový výstup
        • GBA režim
* 4 MB RAM

Nintendo 3DS
-------------------------------
* CPU
    - Dual-Core ARM11 MPCore
        • První jádro pro hry
        • Druhé pro potřeby OS
    - Single-core ARM9
        • Pro zpětnou kompatibilitu s DS
* 128 MB RAM
* 6 MB VRAM
* 1 GB flash

☕  ☕  ☕

