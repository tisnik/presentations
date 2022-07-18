# Branchless programming

## Early CPU architectures

* Intel 8080
* common instructions 4, 5, 7, 10, or 11 cycles
* CPU clock frequency 2MHz to 3.125MHz

# How to make such beast faster?

* better MOS technology -> higher CPU clock frequency
* faster execution (fast multiplier), but nothing fancy
* superscalar architecture (multiple execution lines)
* split instruction execution into multiple stages
* classic RISC pipeline - 5 stages

Classic RISC pipeline

- instruction fetch
- instruction decode
- execute (add, for example)
- memory access
- write back (result)

Classic RISC pipeline

- each stage takes precisely one CPU cycle
- interleaved (5 stages runs in parallel)
- possible 5x speedup on the same MOS technology
- with almost no increase in # transistors
- a huge win at the time

Modern architectures

- 14 to 19 stages
- that's a lot!
- for 16 cores: up to 300 instructions in flight at a time!!!)
- allows faster instruction cycles (3GHz...)
- but pipeline stall costs a lot
    - in theory 19x slower program execution in the worst cache

Hazards

Branches
