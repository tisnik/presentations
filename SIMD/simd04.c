typedef unsigned short int v16us __attribute__((vector_size(16)));

int main(void)
{
    v16us x = { 1, 2, 3, 4, 5, 6, 7, 8 };
    v16us y = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff };
    v16us z = x + y;

    return 0;
}
