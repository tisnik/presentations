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
