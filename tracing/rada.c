int main(void)
{
    float x, y;
    int i;
    x = 1.0f;
    y = 0.0f;
    for (i=0; i<20; i++) {
        y += x;
        x = x / 2.0;
    }
}

