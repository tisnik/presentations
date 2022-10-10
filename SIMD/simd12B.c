typedef float v260f __attribute__((vector_size(260)));

int main(void)
{
    v260f x = { 1.0 };
    v260f y = { 1.0 };
    v260f z = x + y;

    return 0;
}
