package require Itcl

itcl::class Person {
    variable name
    variable surname

    constructor {person_name person_surname} {
        set name $person_name
        set surname $person_surname
    }

    method getname {} {
        return $name
    }

    method getsurname {} {
        return $surname
    }
}

set p1 [Person person1 Chuck Norris]
set p2 [Person person2 Alan Kay]

puts ------------------
puts $p1
puts [$p1 getname]
puts [$p1 getsurname]

puts ------------------
puts $p2
puts [$p2 getname]
puts [$p2 getsurname]

puts ------------------
puts [person1 getname]
puts [person1 getsurname]

puts ------------------
puts [person2 getname]
puts [person2 getsurname]

