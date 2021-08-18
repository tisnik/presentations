# Tracing in Linux

## Native apps tracing

* ltrace
* strace
* DTrace
* SystemTap
* GNU Debugger
* BPF (Berkeley Packet Filter)
* eBPF
* bpftrace

## Structure

```
╔══════════╗
║          ║
║ app.bin. ║
║          ║
╚══════════╝
     │
     │
     ↓
╔══════════╗
║          ║
║  glibc   ║
║          ║
╚══════════╝
     │
     │
     ↓
╔══════════╗
║          ║
║  kernel  ║
║          ║
╚══════════╝
```

## What to trace?

* Syscalls
    - strace
* Applications and libraries
    - ltrace
    - GNU Debugger
* Application state
    - SystemTap
* Front-end to kernel data
    - SystemTap
    - ftrace
    - perf
    - catapult
    - bpftrace
    - ...

```
╔══════════╗
║          ║..... gdb
║ app.bin. ║
║          ║..... SystemTap
╚══════════╝
     │
     │...... ltrace
     ↓
╔══════════╗
║          ║..... gdb
║  glibc   ║
║          ║..... SystemTap
╚══════════╝
     │
     │...... strace
     ↓
╔══════════╗
║          ║..... SystemTap, bpftrace
║  kernel  ║
║          ║..... KGDB
╚══════════╝
```

## Utility `ltrace`

* calling functions from native libraries
* able to detect problematic and/or slow parts of code
* memory allocation and deallocation
* and of course just simple tracing is possible

### Examples

* [Hello world](tracing_examples/example01.md)
* [Random bitmap](tracing_examples/example02.md)
* [Fractal renderer](tracing_examples/example03.md)

### Usage

* Basic usage
    - `ltrace --help`
    - `ltrace binary_app_name`
    - `ltrace binary_app_name app_arguments`
* Timing
    - `ltrace -t` - seconds precision
    - `ltrace -tt` - more precise
    - `ltrace -tt` - Unix time
    - `ltrace -r` - relative offsets
* Filters
    - `ltrace -e malloc+free+open+close ./example03`
    - `ltrace -e -free ./example03` (beware of `-`)
* Statistic
    - `ltrace -c`
* Connect to already running process
    - `ltrace -p 12345`



## Utility `strace`

* Detect all syscalls
* Independently from where it comes
    - application code
    - library
    - (typically from glibc)
* Similar CLI flags as `ltrace`
* Semi-intelligent replace of magic number to symbolic constants
* Also return value is printed
    - (semi-intelligent too if possible)
    - message is printed if return value is known
    - "No such file or directory"

### Usage

* Filtering
    - `strace -e trace=open,close whoami`
* Timings
    - `strace -t whoami`
    - `strace -tt whoami`
    - `strace -ttt whoami`
    - `strace -r whoami`
* Table of syscalls
    - `strace -c whoami`
* Sorting by column
    - `strace -c -S calls whoami`

### Next time

* DTrace
* SystemTap
* GNU Debugger
