package require Itcl

itcl::class Person {
    variable name
    variable surname

    constructor {person_name person_surname} {
        set name $person_name
        set surname $person_surname
    }

    method getname {}
    method getsurname {}
    method setname {new_name}
    method setsurname {new_surname}
}

itcl::body Person::getname {} {
    return $name
}

itcl::body Person::getsurname {} {
    return $surname
}

itcl::body Person::setname {new_name} {
    set name $new_name
}

itcl::body Person::setsurname {new_surname} {
    set surname $new_surname
}

set p1 [Person person1 Chuck Norris]

puts ------------------
puts $p1
puts [$p1 getname]
puts [$p1 getsurname]

puts ------------------
$p1 setname "Alan"
$p1 setsurname "Kay"
puts [$p1 getname]
puts [$p1 getsurname]
