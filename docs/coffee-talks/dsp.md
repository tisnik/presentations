## Digital Signal Processors

* General-purpose CPU versus specialized processing units
* Why?
    - signal processing

### Convolution filter
![Convolution filter](images/dsp_filter.png)

### FIR
![FIR](images/dsp_fir.png")

### Discrete Fourier transform
![DFT](images/dsp_dft.png")

### Discrete cosine transform (JPEG, MPEG, ...)
![DFT](images/dsp_dct.png")

### Common operations?

* ADD?
* MULtiply?
* MAC -> Multiply Accumulate

![MAC](images/dsp_mac.png)

### General-purpose vs. specialized

![DC-3](images/dsp_DC-3.jpg)
![A-10](images/dsp_A-10.jpg)

* Thunderbolt is a plane built around gatling gun
![GAU-10](images/dsp_GAU-10.jpg)

* DSP is a chip built around MAC unit
    - multiplier
    - adder
    - accumulator

## TMS32010

* One of 25 most influential chips in human history
    - First OpAmp, 555, CCD, Intel DRAM, MOS 6502, Z80, Intel 8088
* Texas Instruments
* 1982
* Add. Multiply, MAC
* All blocks can run in parallel
* Saturation arithmetic

![TMS32010](images/dsp_tms_320.jpg)

## TMS32010 internals

* ROM/EPROM 1536 kwords
* RAM 144 kwords
* Stack 4x12 bits
* ALU + 32bit accumulator
* Barrel shifter
* Fast multiplier 16b x 16b -> 32b

## TMS32010 registers

* No general purpose registers!
* Accumulator 32bit
* PC 12bit
* DP 1bit as bank register
* ARP 1bit selects AR0 or AR1 for addressing
* AR0 + AR1 (16b) for addressing
* T (16b) + P (32b) registers are connected to multiplier
    - T: temporary
    - P: product

![TMS320_1](images/dsp_tms32010_1.png)
![TMS320_2](images/dsp_tms32010_2.png)
![TMS320_3](images/dsp_tms32010_3.png)
![TMS320_4](images/dsp_tms32010_4.png)

### Addressing
* Addressing
    - auto increment
    - auto decrement
    - shift by x bites (arrays of different types)
    - change AR0 <-> AR1 for next operation

## More advanced DSPs

![TMS320-C54](images/dsp_tms320-c54.png)

## Saturation arithmetic

![Lenna1](images/dsp_lenna1.png)
![Lenna2](images/dsp_lenna2.png)
![Lenna3](images/dsp_lenna3.png)
