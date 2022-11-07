#include <stdio.h>

int main(void) {
    printf("Extension SSE    is %ssupported\n", __builtin_cpu_supports("sse") ? "" : "un");
    printf("Extension SSE2   is %ssupported\n", __builtin_cpu_supports("sse2") ? "" : "un");
    printf("Extension SSE3   is %ssupported\n", __builtin_cpu_supports("sse3") ? "" : "un");
    printf("Extension SSE4.1 is %ssupported\n", __builtin_cpu_supports("sse4.1") ? "" : "un");
    printf("Extension SSE4.2 is %ssupported\n", __builtin_cpu_supports("sse4.2") ? "" : "un");
    printf("Extension AVX    is %ssupported\n", __builtin_cpu_supports("avx") ? "" : "un");
    printf("Extension AVX2   is %ssupported\n", __builtin_cpu_supports("avx2") ? "" : "un");
    printf("Extension FMA    is %ssupported\n", __builtin_cpu_supports("fma") ? "" : "un");
    printf("Extension FMA4   is %ssupported\n", __builtin_cpu_supports("fma4") ? "" : "un");
    putchar('\n');

    printf("Extension AVX512F         is %ssupported\n", __builtin_cpu_supports("avx512f") ? "" : "un");
    printf("Extension AVX512VL        is %ssupported\n", __builtin_cpu_supports("avx512vl") ? "" : "un");
    printf("Extension AVX512BW        is %ssupported\n", __builtin_cpu_supports("avx512bw") ? "" : "un");
    printf("Extension AVX512DQ        is %ssupported\n", __builtin_cpu_supports("avx512dq") ? "" : "un");
    printf("Extension AVX512CD        is %ssupported\n", __builtin_cpu_supports("avx512cd") ? "" : "un");
    printf("Extension AVX512ER        is %ssupported\n", __builtin_cpu_supports("avx512er") ? "" : "un");
    printf("Extension AVX512PF        is %ssupported\n", __builtin_cpu_supports("avx512pf") ? "" : "un");
    printf("Extension AVX512VBMI      is %ssupported\n", __builtin_cpu_supports("avx512vbmi") ? "" : "un");
    printf("Extension AVX512IFMA      is %ssupported\n", __builtin_cpu_supports("avx512ifma") ? "" : "un");
    printf("Extension AVX5124VNNIW    is %ssupported\n", __builtin_cpu_supports("avx5124vnniw") ? "" : "un");
    printf("Extension AVX5124FMAPS    is %ssupported\n", __builtin_cpu_supports("avx5124fmaps") ? "" : "un");
    printf("Extension AVX512VPOPCNTDQ is %ssupported\n", __builtin_cpu_supports("avx512vpopcntdq") ? "" : "un");
    printf("Extension AVX512VBMI2     is %ssupported\n", __builtin_cpu_supports("avx512vbmi2") ? "" : "un");
    printf("Extension AVX512BITALG    is %ssupported\n", __builtin_cpu_supports("avx512bitalg") ? "" : "un");
    return 0;
}

