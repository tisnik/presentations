#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define A putchar
#define B printf
#define C char
p(n){while(n>0){if(n>=10){A('X');n-=10;}else
if(n==9){B("IX");n-=9;}else if(n>=5){A('V');
n-=5;}else if(n==4){B("IV");n-=4;}else{A('I'
);n--;}}}C*s="ABEFGHJKNOPQRSTUWYZ";C*t="\
chteli byste zjistit jak to cele funguje ze"
;main(){int i;C*c;for(c=t;*c;c++){p(*c-'a'+1
);int x=rand()%strlen(s);putchar(s[x]);}}

