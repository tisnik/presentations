# Rust programming language

* Pavel Tišnovský, Red Hat
    - `ptisnovs@redhat.com`
* Presentation:
    - [https://tisnik.github.io/presentations/summer_camp_2021/rust.html](https://tisnik.github.io/presentations/summer_camp_2021/rust.html)
* Presentation source:
    - [https://github.com/tisnik/presentations/blob/master/docs/summer_camp_2021/rust.md](https://github.com/tisnik/presentations/blob/master/summer_camp_2021talks/rust.md)

![images/rust_logo.png](images/rust_logo.png)

---

## Table of content

* Requirements to production-ready programming language
* Rust popularity and expansion
* Rust characteristics
* Rust versus C/C++
* Rust versus Go
* Communication with compiler
* Data types
* Other interesting parts of Rust
* Object oriented programming in Rust
* Memory management
* Threads
* Testing
* Package manager (Cargo)
* Selected useful packages
* Deployment
* Interface to Python
* Documentation

---

## Requirements to production-ready programming language

* Program correctness
* Maintainability
* Safety
* Stability of language ecosystem
* Enough developers
* Resource requirements
    - More RAM needed -> more expenses in containerized world
* API and ability to communicate with (micro)services

![images/real_world.jpg](images/real_world.jpg)

---

## Rust popularity and expansion

### Popularity of Rust

* More metrics how to measure popularity
    - Tiobe index
    - PYPL (PopularitY of Programming Languages)
    - OpenHub (for registered repositories only)
    - StackOverflow (yearly interrogatory)

![images/so1.png](images/so1.png)

![images/so2.png](images/so2.png)

![images/so3.png](images/so3.png)

### Rust expansion

* Again, many statistic available
    - should we trust them?

![images/stat_pypl.png](images/stat_pypl.png)

![images/stat_openhub.png](images/stat_openhub.png)

![images/rust_tiobe_index.png](images/rust_tiobe_index.png)

---

## Rust characteristics

![images/rust_tree.png](images/rust_tree.png)

* Goals
    - safe applications
    - parallelization/concurrency
    - performance comparable with C and C++ (even for new features)
    - [https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust.html)
    - good compiler messages
    - low level and at the same time high level features
* Don't repeat the same mistakes made in C/C++ and in Java
    - macrosystem
    - pointers
    - NPE
    - strings

![images/npe.jpg](images/npe.jpg)

