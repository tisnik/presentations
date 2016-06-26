double sum(double *array, int length)
{
    double *p = array;
    double result = 0;
    int i;

    for (i=0; i<length; i++) {
        result += *p++;
    }

    return result;
}

