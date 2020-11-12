# installfest-2020-assembler
Materials for assembly language workshop

* Prezentace:
    - [https://tisnik.github.io/presentations/installfest2020/assembler.html](https://tisnik.github.io/presentations/installfest2020/assembler.html)
* Zdrojový kód prezentace:
    - [https://github.com/tisnik/presentations/blob/master/installfest2020/README.md](https://github.com/tisnik/presentations/blob/master/installfest2020/README.md)


```
   _____                              ___.   .__                
  /  _  \   ______ ______ ____   _____\_ |__ |  |   ___________ 
 /  /_\  \ /  ___//  ___// __ \ /     \| __ \|  | _/ __ \_  __ \
/    |    \\___ \ \___ \\  ___/|  Y Y  \ \_\ \  |_\  ___/|  | \/
\____|__  /____  >____  >\___  >__|_|  /___  /____/\___  >__|   
        \/     \/     \/     \/      \/    \/          \/       
```

---

# Úvod

---

## Proč assembler?

1. Větší efektivita využití CPU (čím novější generace, tím více relevantní)
2. Rychlejší (a predikovatelné) přerušovací rutiny
3. Efektivita při práci s pamětí (cache+RAM)
4. Kompaktní kód
5. Lepší pochopení práce s gdb a dalšími debuggery

---

## Role assembleru
Několik úrovní abstrakce (vrstev nad HW)
- 5   uživatelské aplikace
- 4½  (skriptovací engine)
- 4   vyšší programovací jazyk
- 3   assembler
- 2   strojový kód
- 1   syscalls
- 0   HW

---

## Assemblery v minulosti
1. První generace mainframů
    - vývojové diagramy v roli „vyššího jazyka“
    - assembler
    - strojový kód (zpočátku ruční překlad!)
1. Mainframy a později minipočítače
    - přechod k vyšším programovacím jazykům
    - levnější vývoj, šance na přenositelnost
1. Osmibitové herní konzole
    - assembler jediná rozumná volba
1. Domácí mikropočítače
    - návrat „ke kořenům“
    - prakticky jediná volba pro profesionální aplikace
1. Osobní mikropočítače
    - Motorola 68000
    - 8086/80286...
    - specifické použití assembleru (hry, dema, ...)
1. DSP
    - výpočetní subrutiny (FFT...)
    - přerušovací rutiny

---

## Assemblery v současnosti
1. Firmware
1. Kód pracující přímo s HW (senzory, CPU+FPGA)
1. DSP a MCU - rychlé přerušovací rutiny!
1. Instrukce nedostupné ve vyšším programovacím jazyce
1. Specifické subrutiny (SIMD, SSE, rotace, hledání vzorků...)
1. Zpracování signálů
1. Kodeky
1. Virtuální stroje generující strojový kód
1. Reverse engineering :-)
1. Samomodifikující se kód
1. DSP
1. Fingerprints (A86)

---

## Použití assembleru v současnosti
1. Většinou velmi SPECIFICKÉ pro určitou oblast
1. Naprostá většina aplikací není psána pouze v assembleru
   - Coreboot: většinou C, jen zhruba 1% asm
   - Důvod: výhody vyšších programovacích jazyků + snadnější audit kódu

---

# Assembler a Linux
* as    (GNU Assembler, GAS)
* NASM  (Netwide Assembler)
* Yasm
* FASM  (flat assembler)

---

## GNU Assembler
* Součást klasického toolchainu
* cpp → gcc → as → ld → spustitelný_soubor
* Původně jen AT&T syntaxe
* Dnes i „Intel“ syntaxe (na x86/x86-64)
* Různý způsob zápisu podle platformy!
   - Jména registrů
   - Konstanty
   - Adresování
   - Komentáře

---

## Syscally a GNU Assembler

---

### Ukončení procesu funkcí "exit"
* i386, syntaxe AT&T
* i386, syntaxe Intel
* ARM (32bit)
* AArch64

---

### „Hello world“ v assembleru
