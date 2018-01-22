package require Itcl

itcl::class Person {
    variable name
    variable surname

    constructor {{person_name ""} {person_surname ""}} {
        puts "Person:constructor: $person_name $person_surname"
        set name $person_name
        set surname $person_surname
    }

    method getname {} {
        return $name
    }

    method getsurname {} {
        return $surname
    }

    method setname {new_name} {
        set name $new_name
    }

    method setsurname {new_surname} {
        set surname $new_surname
    }
}

itcl::class Employee {
    inherit Person

    variable employee_number

    constructor {employee_name employee_surname number} {
        puts "Employee:constructor: $employee_name $employee_surname $number"
        Person::constructor $employee_name $employee_surname
        set employee_number $number
    }

    method getnumber {} {
        return employee_number
    }

    method setnumber {new_number} {
        set employee_number $new_number
    }
}

set e1 [Employee employee1 Chuck Norris 1]

puts ------------------
puts $e1
puts [$e1 getname]
puts [$e1 getsurname]
puts [$e1 getnumber]

