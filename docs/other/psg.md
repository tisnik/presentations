# Sound chips for 8-bit machines
* Pavel Tisnovsky

--------------------

## Sound chip

* Integrated circuit
* Designed to produce sound

--------------------

## Sound chip

* Used in 8-bit era
    - home computers
    - game consoles
    - arcade games
    - consumer electronics

--------------------

## Sound chips types

* Digital
* Analog
* Digital+Analog

--------------------

## Sound chip families

* PSG
* FM synthesizers
* PCM (play samples)

--------------------

## PSG

* Programmable sound generator
    - Generates various sound waves

--------------------

## PSG

* Multiple waveforms
    - Square
    - Triangle
    - Noise generator
    - Envelope generator

* Filters
    - analog
    - digital

--------------------
## Triangle wave(s)

    Only on some PSGs

    Usually 4bit
    samples
    - 16 levels

--------------------

## Envelope

    Only on some PSGs

    *Shaping amplitude*
    - Attack
    - Decay
    - Sustatin
    - Release
--------------------
Noise generator

    On almost all PSGs

    Based on LFSR
    - Linear Feedback
    - Shift Register

    a.k.a.
    - Poly counter
--------------------
Typical LSFRs

    4 bit TIA, POKEY
    5 bit TIA, POKEY
    9 bit TIA, POKEY
    15 bit SN76489,2A03
    17 bit POKEY
--------------------
List of PSGs (#1)

    ULA pin#28 :-)
    Atari TIA
    Atari POKEY
    HuC6280
    Ricoh 2A03/2A07
--------------------
List of PSGs (#1)

    AY-3-8910 (YM2149)
    TI SN76477
    TI SN76489 (DCSG)
    TI SN76496
    MOS SID
--------------------

*******************
    ULA pin#28
*******************

--------------------
ULA

    ZX Spectrum 48k
    one bit I/O
    variable freq.
    can be controlled
    by software
    - (many tricks)
--------------------
***load rutina***
--------------------

*******************
       TIA
*******************

--------------------
TIA

    Television
    Interface
    Adaptor

Graphics and sound
chip for Atari 2600

    Jay Miner
--------------------
TIA sound subsystem

    Two oscillators
    Freq. dividers
    LFSR (poly counter)
    Audio volume ctrl
--------------------
TIA sound

    Oscillators
    - 30kHz reference
    - clock signal

    - 5 bit frequency
    - divider
--------------------
TIA sound

    Oscillators (cont.)
    - + additional
    - frequency divide
    - is possible
    - /2 /6 /31 /93

    - (detuned notes)
--------------------
TIA sound

    Sound control
    - 4 bit volume
    - LFSR control
--------------------
TIA LFSR

    9bit LFSR with
    selectable feedback
    taps:
       4bit LFSR
       5bit LFSR
       5+4bit LFSRs
--------------------

*******************
      POKEY
*******************

--------------------
POKEY

    Audio +
    Keyboard +
    Paddles +
    Serial I/O +
    PRNG generator
    chip

    - Doug Neubauer
--------------------
POKEY
    4 audio channels
    - Can be combined
    - selectable channels
    -     4x8 bit channels
    -     2x16 bit channels
    -     1x16 bit + 2x8 bit

    Digital hi-pass
    filter
--------------------
POKEY

    4 audio channels

    Each channel
    - Freqeuncy
    - Volume
    - Waveform
    -     Square wave
    -     LFSR noise
--------------------
POKEY

    Noise generators
    - Sample and Hold

    Unique *pokey* sound
gr.0----------------
    -       ,----------.
,------------}|4 bit poly|}---------}
|         ,--}|          |
|         |   \--------**'
|         \----------{-''
|
|             ,------------.
*------------}| 5 bit poly |}-------}
|         ,--}|            |
|         |   \---------*-*'
|         \-----------{-'-'
|
|         ,--------------------.
*--------}|    17 bit poly     |}---}
|     ,--}|                    |
|     |   \---------------*---*'
|     \--------*--------{-'-{-'
|              |
vstup      prepnuti 9/17bit
gr.0----------------
    -     ,------.
    -     |      |
5 bit -----}| D  Q |------}
    -     |      |
clock -----}| C    |
    -     |      |
    -     \------'
--------------------
POKEY sound control
registers

    9x8 bit registers

    - AUDF1-AUDF4
    - AUDC1-AUDC4
    - AUDCTL
--------------------
POKEY sound control
registers

    AUDF1-AUDF4
    - Frequency
    - divider
    - Fosc/1..256

    (detuned notes!)
--------------------
POKEY sound control
registers

    AUDC1-AUDC4
    - 4 bit volume
    - 1 bit direct
    -   control
--------------------
POKEY sound control
registers
    AUDC1-AUDC4
    - 3 bit LFSR
    -     no poly
    -     4 bit poly
    -     5 bit poly
    -     5+4
    -     17 bit poly
    -     5+17
--------------------
POKEY sound control
registers

    AUDCTL
       join two channels
       into 16 bit one

       Fosc selection
--------------------

*******************
AY-3-8910 (YM2149)
*******************

--------------------
AY-3-8910

    YM 2149
    - ZX Spectrum 128
    - MSX
    - Vectrex
    - Atari ST
    - Video game cabs.
--------------------
Three AY variants

    AY-3-8910
    - 40 pins, 2xI/O
    AY-3-8912
    - 28 pins, 1xI/O
    AY-3-8913
    - 24 pins, no I/O
--------------------
AY sound synthesis

    3 sound channels
    separate outputs
    square waves
    noise generator
    envelope generator
    mixer
    D/A convertor
--------------------
AY square wave gen.

    12bit freq. divider
    4bit amplitude
    or env.generator
--------------------
AY noise generator

    5bit freq. divider
--------------------
AY envelope gen.

    16bit freq. divider
    envelope shape

    8 shapes
    - triangles
    - sawtooth
    - attack only
    - decay only
--------------------
AY D/A

    16 levels
    - digital signal

    Logarithmic DAC
--------------------

*******************
      HuC6280
*******************

--------------------

*******************
  Ricoh 2A03/2A07
*******************

--------------------
Ricoh 2A03/2A07

    Ricoh 2A03 CPU
    NES/Gameboy

    2A03 - NTSC
    2007 - PAL
--------------------
Ricoh 2A03/2A07

    Based on MOS 6502

    2A03 vs MOS 6502
    - - BCD mode
    - + timer
    - + DMA
    - + sound system
--------------------
2A03 sound system

    5 channels
    2 square waves
    1 triangle wave
    1 noise generator
    1 D/A converter

    22 control registers
--------------------
2A03 square waves

    54.6 Hz - 12,4 kHz
    4 bit amplitude
    variable duty
    - 1:8
    - 1:4
    - 1:2
    - 3:4
--------------------
2A03 triangle wave

    27.3 Hz - 55.9 kHz
    4 bit amplitude
    (automatic control)
--------------------
2A03 noise generator

    15 bit LFSR
    29.3 Hz - 447 kHz
    two modes
    - long
    -     32767 bit cycle
    - short
    -     93 bit cycle
--------------------
2A03 D/A converter

    DMC
    - delta modulation

    7 bit
    4.2 kHz - 33.5 kHz
    semi automatic DMA
    non-linear D/A
--------------------

*******************
 TI SN76489 (DCSG)
*******************

--------------------
TI SN76489 (DCSG)

    DCSG
    - Digital
    - Complex
    - Sound
    - Generator

--------------------
TI SN76489 used in

    Sega Game 1000
    Sega Master System
    Sega Gamegear
    Sega Megadrive
    Acorn BBC
    Tomy Tutor
    8bit Sharp
--------------------
TI SN76489 (DCSG)

    Minimalistic design

    16pin DIL
    Three square wave
    generators
    One noise generator

    8 control registers
--------------------
TI SN76489 (DCSG)

    16pin DIL
    - +5V + GND
    - D0-D7
    - CE + WE
    - CLO (in)
    - AUD (out)
    - OUT (out)
    - REY (out)
--------------------
TI SN76489 (DCSG)

    Square wave gen.
    - 10bit freq.divider
    - 4bit amplitude
--------------------
TI SN76489 (DCSG)

    Noise generator
    - 15 bit LFSR
    - Only 3 freq.
    -     Fosc/64
    -     Fosc/128
    -     Fosc/256
gr.0----------------
Rezim 1:
   ,-------------------------------.
/-}|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|}
|  \------------------------------*'
|                                 |
\---------------------------------'

Rezim 2:
   ,-------------------------------.
/-}|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|}
|  \------------------------*-----*'
|                           |     |
|                ,------.   |     |
|                |      |{--'     |
\---------------{| XOR  |         |
    -          |      |{--------'
    -          \------'
--------------------

*******************
    TI SN76494
*******************

--------------------
TI SN76494

    Almost the same
    as SN76489

    Missing f/8 divider
    4 MHz -> 500 kHz

    Arcade games
--------------------

*******************
       SID
*******************

--------------------
SID

    3 oscillators
    each oscillator
    - var. pulse
    - sawtooth
    - triangle
    - noise

    ADSR
--------------------
SID

    filters
    - low pass
    - high pass
    - notch

    ring modulator

    oscillator sync.
gr.0----------------
  ,------------------.    ,---------.
  |Tone oscillator   |    |Amplitude|
-}|Waveform generator|---}|modulator|
  |        #1        | ,-}|    #1   |
  \------------------' |  \---------'
                     |
  ,------------------. |
  |Envelope generator| |
-}|                  |-'  ADRS
  |        #1        |
  \------------------'
--------------------

*******************
* Demonstrations  *
*******************

--------------------

8bit game consoles
2nd generation
Channel F      1976
Atari 2600     1977
Magnavox Odd.  1978
Intellivision  1979
--------------------
16bit game consoles
TurboGrafx-16   1987
Sega Mega Drive 1988
Super NES(SNES) 1990
Neo Geo         1991
Commodore CDTV  1991
Philips CD-i    1991
--------------------
8bit home computers
--------------------
16bit personal comp.
--------------------
NES
    Nintendo
    Entertaiment
    System
--------------------
Super NES (SNES)
    65C816 CPU
    16bit variant 6502
    Sound generated by
    SPC700 coprocessor
--------------------
SPC700
    programmable
    has 64 kB RAM
    8 stereo channels
    16bit samples
--------------------

