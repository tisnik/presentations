#include <stdio.h>
#include <stdfix.h>

_Sat _Fract sat_add3 (_Sat _Fract a, _Sat _Fract b)
{
  return a + b;
}

int main() {
    _Fract unsigned a = 0.1;
    _Fract unsigned b = 0.2;
    _Fract unsigned c = a + b;
    printf("a=%f b=%f\n", (float)a, (float)b);
    printf("c=%f\n", (float)c);
}
