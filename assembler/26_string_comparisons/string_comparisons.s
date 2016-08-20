# asmsyntax=as

# Ukazka pouziti maker v GNU Assembleru - direktivy pro porovnani retezcu
# - pouzita je "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix



.print ".ifc"

.ifc "Hello", "World"
    .print "Hello == World"
.else
    .print "Hello != World"
.endif

.ifc "Hello", "Hello"
    .print "Hello == Hello"
.else
    .print "Hello != Hello"
.endif

.ifc "", ""
    .print "empty strings are equal"
.else
    .print "empty strings are not equal"
.endif



.print "\n.ifeqs"

.ifeqs "Hello", "World"
    .print "Hello == World"
.else
    .print "Hello != World"
.endif

.ifeqs "Hello", "Hello"
    .print "Hello == Hello"
.else
    .print "Hello != Hello"
.endif

.ifeqs "", ""
    .print "empty strings are equal"
.else
    .print "empty strings are not equal"
.endif



.print "\n.ifnes"

.ifnes "Hello", "World"
    .print "Hello != World"
.else
    .print "Hello == World"
.endif

.ifnes "Hello", "Hello"
    .print "Hello != Hello"
.else
    .print "Hello == Hello"
.endif

.ifnes "", ""
    .print "empty strings are not equal"
.else
    .print "empty strings are equal"
.endif

