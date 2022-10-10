typedef float v1024f __attribute__((vector_size(1024)));

void addVectors(v1024f * x, v1024f * y, v1024f * z)
{
    *z = *x + *y;
}

int main(void)
{
    v1024f x = { 1.0 };
    v1024f y = { 1.0 };
    v1024f z;

    addVectors(&x, &y, &z);

    return 0;
}
