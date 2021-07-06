# Variable

### Wikipedia

* In computer programming, a variable or scalar is a storage location (identified
by a memory address) paired with an associated symbolic name, which contains
some known or unknown quantity of information referred to as a value. 


## Variable properties

* Lot of unknowns
    - type inference
    - lifetime
    - visibility (threads?)
    - update - does it happen in all times (HW pins...)
    - update - is visible from other threads?
    - update - is atomic?
    - multiple updates - is sequence of operation conserved?
    - hazards
        - RAW, WAR, WAW

## Clojure approach

* Variables are not the best technology (too many properties/unknowns)
    - dtto for objects :)
* Be immutable whenever possible
    - (Rust mimicks this approach btw)
* Let's use four distinct mechanisms instead
    - vars
    - refs
    - atoms
    - agents
* Mutate via functions
* Validators
* Watchers

## Vars/Refs/Atoms/Agents

```
Vars   thread local   sychronous    single identity
Refs   transactional  synchronous   multiple identities
Agents uncoordinated  asynchronous  single identity
Atoms  uncoordinated  synchronous   single identity
```

## Vars

* Mutable storage location
* Mutation on per-thread basis
    - thread isolation

## Refs

* Shared mutable storage
* STM - Software Transactional Memory
* Mutation withing transaction
* Coordinated, synchronous change of multiple locations

```clojure
(dosync
  (alter (ref1 ...))
  (alter (ref2 ...)))
```

## Agents

* Independent, asynchronous change of individual locations
* Mutation done asynchronously (in new thread/goroutine/...)
* It's possible to wait for mutation to finish

## Atoms

* Shared, synchronous, independent state
* All changes are visible to other threads
    - w/o the need to locking etc.

## Validators

* Function called before var/ref/agent/atom is mutated
* Can return `true`/`false` or throw an exception if needed

## Watcher

* Function called automatically with key, reference, old state and new state
* Might be called from multiple threads simultaneously
