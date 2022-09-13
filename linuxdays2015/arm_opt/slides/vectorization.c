void add_offset_to_vector(int *__restrict px,
                          int *__restrict py, int n, int offset)
{
    unsigned int i;
    for (i = 0; i < (n & ~3); i++) {
        px[i] = py[i] + offset;
    }
}
