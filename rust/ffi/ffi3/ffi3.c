int string_length(const char *str)
{
    int len = 0;
    for (; *str; str++, len++)
        ;
    return len;
}

