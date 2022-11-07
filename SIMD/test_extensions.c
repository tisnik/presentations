#include <stdio.h>

int main(void)
{
    printf("Extension SSE    is %ssupported\n",
           __builtin_cpu_supports("sse") ? "" : "un");
    printf("Extension SSE2   is %ssupported\n",
           __builtin_cpu_supports("sse2") ? "" : "un");
    printf("Extension SSE3   is %ssupported\n",
           __builtin_cpu_supports("sse3") ? "" : "un");
    printf("Extension SSE4.1 is %ssupported\n",
           __builtin_cpu_supports("sse4.1") ? "" : "un");
    printf("Extension SSE4.2 is %ssupported\n",
           __builtin_cpu_supports("sse4.2") ? "" : "un");
    printf("Extension AVX    is %ssupported\n",
           __builtin_cpu_supports("avx") ? "" : "un");
    printf("Extension AVX2   is %ssupported\n",
           __builtin_cpu_supports("avx2") ? "" : "un");
    printf("Extension FMA    is %ssupported\n",
           __builtin_cpu_supports("fma") ? "" : "un");
    printf("Extension FMA4   is %ssupported\n",
           __builtin_cpu_supports("fma4") ? "" : "un");
    return 0;
}
