# 8 bit glory

## Atari systems

* 64 kB RAM
* 24 kB ROM
    - 16 kB for OS
    - 8 kB for BASIC or cartridge
* Processor
    - MOS 6502
* Text mode
    - 40x24 monochrome
* Graphics modes
    - 320x192 monochrome
    - 160x192 4 colors
    -  80x192 16 colors
* Sound
    - PSG
* Cassette recorder
* Floppy disk support
    - cost!
* SIO
    - serial input/output
    - the same author created USB years after!

## MOS 6502

* 8 bit CPU
* 16 bit address bus (64 kB)
* 1975
* 1.6 MHz
* no multiplier nor divider
* one GP register: an accumulator A
* two index registers: X and Y
* 56 instructions

## Programming Atari

* Atari BASIC
* Other BASICs
    - Turbo BASIC XL
    - Microsoft Basic (ugh!!!)
* Assemblers
    - Atari Assembler Editor
    - Atari Macro Assembler (ATASM)
    - SynAssembler
* Some compilers
    - Pascal

## Atari BASIC

* implemented in 8kB ROM
* circa 37kB available RAM (- video RAM)
* so-called full-screen editor with line numbering
* support for graphics and sound
* tokenization on the fly
* built-in functions with one parameter (every)
* many statements and few control structures
* error checks on the fly
* line numbers
* global variables only (127)
* no user-defined functions
* two primitive data types: number, string
* string arrays, number arrays and matrices
* FOR-loop and GOTO everywhere :)
* computed GOTO
* TRAP for error catching

### Live demo

## SynAssembler

* implemented in 8kB ROM cartridge
* editor/assembler/monitor
* controlled by CLI commands
* no help, no menu, almost no error checks

### Live demo

