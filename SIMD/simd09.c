typedef double v16d __attribute__((vector_size(16)));

int main(void)
{
    v16d x = { 1, 2, 3, 4 };
    v16d y = { 0.1, 0.1, 0.1, 0.1 };
    v16d z = x + y;

    return 0;
}
