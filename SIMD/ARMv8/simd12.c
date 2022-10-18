typedef float v256f __attribute__((vector_size(256)));

int main(void)
{
    v256f x = { 1.0 };
    v256f y = { 1.0 };
    v256f z = x + y;

    return 0;
}
