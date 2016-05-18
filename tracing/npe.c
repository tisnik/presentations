void set_mem(int *address, int value)
{
    *address = value;
}

int main(int argc, char **argv)
{
    set_mem((int*)0, 42);
    return 0;
}

