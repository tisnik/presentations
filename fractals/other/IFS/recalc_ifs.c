void recalcIFS(int width, int height, int maxIter, int startIter, double morphRatio, int firstIFS, int secondIFS)
{
    double x1=0, y1=0, x2=0, y2=0;              // generovane souradnice
    double xmin=1e10, xmax=-1e10;               // obdelnik opsany IFS fraktalu
    double ymin=1e10, ymax=-1e10;
    int    x, y, k;
    double pp, sum;
    double delitel=12.0;
    int i,j;

    double a[5][7];
    xmin=-7.0; xmax=10.0; ymin=-1.0; ymax=00.0;

    for (j=0; j<5; j++) {                       // prenos koeficientu IFS systemu
        for (i=0; i<7; i++) {                   // a smichani prvniho a druheho systemu
            a[j][i]=(1.0-morphRatio)*data[j+firstIFS*5][i]
                   +(morphRatio)*data[j+secondIFS*5][i];
        }
    }
    for (i=0; i<maxIter; i++) {                 // pro vsechny iterace
        pp=((float)rand())/RAND_MAX;            // p lezi v rozsahu 0.0-1.0
        sum=0;                                  // na zaklade nahodneho cisla
        for (k=0; sum<=pp; k++)                 // najit transformaci
            sum+=a[k][6];
        k--;
        x2=x1*a[k][0] + y1*a[k][1] + a[k][4];   // aplikovat transformaci
        y2=x1*a[k][2] + y1*a[k][3] + a[k][5];
        x1=x2; y1=y2;
        if (i>startIter) {                      // pokud byl prekrocen pocet
            x2=(x1-xmin)*(double)(width)/delitel; // startovnich iteraci
            y2=(y1-ymin)*(double)(height)/delitel;
            x=(int)x2; y=(int)y2;               // vypocitat a zobrazit pozice pixelu
            addfloat(x, y);
        }
    }
