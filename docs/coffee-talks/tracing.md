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
