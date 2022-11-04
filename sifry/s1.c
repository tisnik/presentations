#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_roman(n)
{
    while (n > 0) {
        if (n >= 10) {
            putchar('X');
            n -= 10;
        } else if (n == 9) {
            printf("IX");
            n -= 9;
        } else if (n >= 5) {
            putchar('V');
            n -= 5;
        } else if (n == 4) {
            printf("IV");
            n -= 4;
        } else {
            putchar('I');
            n--;
        }
    }
}

char *s = "ABCDEFGHJKMNOPQRSTUWYZ";
char *t = "chteli byste zjistit jak to cele funguje ze";

void main(void)
{
    int i;
    char *c;
    for (c = t; *c; c++) {
        print_roman(*c - 'a' + 1);
        int x = rand() % strlen(s);
        putchar(s[x]);
        /*putchar(' '); */
    }
}
