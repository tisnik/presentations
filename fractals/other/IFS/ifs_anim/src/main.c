#include <stdio.h>
#include <math.h>
#include <SDL/SDL.h>

SDL_Surface *screen;
SDL_Surface *pixmap;

int histogram[240][320];

const int IFS_PIXELS = 320*240;

static float data[][7]={
    { 0.500000, 0.000000, 0.000000, 0.500000,-2.563477,-0.000003, 0.333333},
    { 0.500000, 0.000000, 0.000000, 0.500000, 2.436544,-0.000003, 0.333333},
    { 0.000000,-0.500000, 0.500000, 0.000000, 4.873085, 7.563492, 0.333333},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.307692,-0.531469,-0.461538,-0.293706, 5.401953, 8.655175, 0.400000},
    { 0.307692,-0.076923, 0.153846,-0.447552,-1.295248, 4.152990, 0.150000},
    { 0.000000, 0.545455, 0.692308,-0.195804,-4.893637, 7.269794, 0.450000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.696970,-0.481061,-0.393939,-0.662879, 2.147003,10.310288, 0.747826},
    { 0.090909,-0.443182, 0.515152,-0.094697, 4.286558, 2.925762, 0.252174},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.824074, 0.281482,-0.212346, 0.864198,-1.882290,-0.110607, 0.787473},
    { 0.088272, 0.520988,-0.463889,-0.377778, 0.785360, 8.095795, 0.212527},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.824074, 0.281481,-0.212346, 0.864197,-1.772710, 0.137795, 0.771268},
    {-0.138580, 0.283951,-0.670062,-0.279012, 2.930991, 7.338924, 0.228732},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.870370, 0.074074,-0.115741, 0.851852,-1.278016, 0.070331, 0.798030},
    {-0.162037,-0.407407, 0.495370, 0.074074, 6.835726, 5.799174, 0.201970},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.850000, 0.040000,-0.040000, 0.850000, 0.000000, 1.600000, 0.850000},
    { 0.200000,-0.260000, 0.230000, 0.220000, 0.000000, 1.600000, 0.070000},
    {-0.150000, 0.280000, 0.260000, 0.240000, 0.000000, 0.440000, 0.070000},
    { 0.000000, 0.000000, 0.000000, 0.160000, 0.000000, 0.000000, 0.010000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.307692, 0.000000, 0.000000, 0.294118, 4.119164, 1.604278, 0.151515},
    { 0.192308,-0.205882, 0.653846, 0.088235,-0.688840, 5.978916, 0.253788},
    { 0.192308, 0.205882,-0.653846, 0.088235, 0.668580, 5.962514, 0.253788},
    { 0.307692, 0.000000, 0.000000, 0.294118,-4.136530, 1.604278, 0.151515},
    { 0.384615, 0.000000, 0.000000,-0.294118,-0.007718, 2.941176, 1.000000},

    { 0.787879,-0.424242, 0.242424, 0.859848, 1.758647, 1.408065, 0.895652},
    {-0.121212, 0.257576, 0.151515, 0.053030,-6.721654, 1.377236, 0.052174},
    { 0.181818,-0.136364, 0.090909, 0.181818, 6.086107, 1.568035, 0.052174},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.000000, 0.000000, 0.000000, 0.500000, 0.000000, 0.000000, 0.050000},
    { 0.420000,-0.420000, 0.420000, 0.420000, 0.000000, 0.200000, 0.400000},
    { 0.420000, 0.420000,-0.420000, 0.420000, 0.000000, 0.200000, 0.400000},
    { 0.100000, 0.000000, 0.000000, 0.100000, 0.000000, 0.200000, 0.150000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

    { 0.500000, 0.000000, 0.000000, 0.500000,-0.500000, 0.000000, 0.333333},
    { 0.500000, 0.000000, 0.000000, 0.500000, 0.500000, 0.000000, 0.333333},
    { 0.500000, 0.000000, 0.000000, 0.500000, 0.000000, 0.860000, 0.333334},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},
    { 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000},

};
static void init_sdl(void)
{
    if (SDL_Init(SDL_INIT_VIDEO) < 0)
    {
        fprintf(stderr, "Error initializing SDL: %s\n", SDL_GetError());
        exit(1);
    }
#ifdef FULLSCREEN
    screen = SDL_SetVideoMode(640, 480, 32, SDL_HWSURFACE | SDL_DOUBLEBUF | SDL_FULLSCREEN | SDL_ANYFORMAT);
#else
    screen = SDL_SetVideoMode(640, 480, 32, SDL_HWSURFACE | SDL_DOUBLEBUF | SDL_ANYFORMAT);
#endif
    if (!screen)
    {
        fprintf(stderr, "Error setting video mode: %s\n", SDL_GetError());
        exit(1);
    }
}

void finalize(void)
{
    SDL_FreeSurface(screen);
    SDL_Quit();
}

void gfx_bitblt(SDL_Surface *surface, const int x, const int y)
{
    SDL_Rect dst_rect;
    dst_rect.x = x;
    dst_rect.y = y;
    SDL_BlitSurface(surface, NULL, screen, &dst_rect);
}

void gfx_flip(void)
{
    SDL_Flip(screen);
}

static void putpixel(SDL_Surface *surface, int x, int y, Uint32 pixel)
{
    int bpp = surface->format->BytesPerPixel;
    /* Here p is the address to the pixel we want to set */
    Uint8 *p = (Uint8 *)surface->pixels + y * surface->pitch + x * bpp;

    switch(bpp) {
    case 1:
        *p = pixel;
        break;

    case 2:
        *(Uint16 *)p = pixel;
        break;

    case 3:
        if (SDL_BYTEORDER == SDL_BIG_ENDIAN)
        {
            p[0] = (pixel >> 16) & 0xFF;
            p[1] = (pixel >> 8) & 0xFF;
            p[2] = pixel & 0xFF;
        }
        else
        {
            p[0] = pixel & 0xFF;
            p[1] = (pixel >> 8) & 0xFF;
            p[2] = (pixel >> 16) & 0xFF;
        }
        break;

    case 4:
        *(Uint32 *)p = pixel;
        break;
    }
}

static void gfx_putpixel(int x, int y, Uint32 pixel)
{
    putpixel(screen, x, y, pixel);
}

static void main_loop(void)
{
    SDL_Event event;
    int done = 0;
    do
    {
        while(SDL_PollEvent(&event))
        {
            switch (event.type)
            {
                case SDL_QUIT:
                    done = 1;
                    break;
                case SDL_KEYDOWN:
                    switch (event.key.keysym.sym)
                    {
                        case SDLK_ESCAPE:
                        case SDLK_q:
                            done = 1;
                            break;
                        default:
                            break;
                    }
            }
        }
        SDL_Delay(100);
    } while (!done);
}

void recalcIFS(int max_iter, int start_iter, float morph_ratio, int first_ifs, int second_ifs)
{
    const float scale_factor=12.0;
    const float scale_factor_x = pixmap->w / scale_factor;
    const float scale_factor_y = pixmap->h / scale_factor;
    const float xmin=-6.0;
    const float ymin=-1.0;

    /* division is slow operation even in float mode */
    const float rand_max_inv = 1.0 / RAND_MAX;

    float x1=0, y1=0, x2, y2;
    int   i, j, k;
    float maxp=0;
    int  *ip;
    Uint8 *pixel = (Uint8 *)pixmap->pixels;

    float a[5][7];

    /* compute all five transformation matrices */
    for (j=0; j<5; j++)
    {
        for (i=0; i<7; i++)
        {
            a[j][i]=(1.0-morph_ratio)*data[j+first_ifs*5][i]
                       +(morph_ratio)*data[j+second_ifs*5][i];
        }
    }

    /* IFS computation */
    for (i=0; i<max_iter; i++)
    {
        float pp = rand()*rand_max_inv;
        float sum=0;
        for (k=0; sum<=pp; k++)
            sum+=a[k][6];
        k--;
        x2 = x1*a[k][0] + y1*a[k][1] + a[k][4];
        y2 = x1*a[k][2] + y1*a[k][3] + a[k][5];
        x1 = x2;
        y1 = y2;
        if (i > start_iter)
        {
            int x = (int) ((x1 - xmin) * scale_factor_x);
            int y = (int) ((y1 - ymin) * scale_factor_y);
            if (x >= 0 && y >=0 && x < pixmap->w && y < pixmap->h)
            {
                histogram[y][x]++;
            }
        }
    }

    /* maxp computation */
    ip = &histogram[0][0];
    for (i=0; i<IFS_PIXELS; i++)
    {
        if (maxp<*ip) maxp=*ip;
        ip++;
    }
    /* we need to compute log(x)/maxp*255.0 -> small optimalization is possible here */
    maxp = 255.0 / log(maxp);

    /* final rendering */
    ip = &histogram[0][0];
    for (i=0; i<IFS_PIXELS; i++)
    {
        int color = 0xFF & (int)(log(*ip)*maxp);
        color = ~color;
        ip++;
        *pixel++ = color;
        *pixel++ = color;
        *pixel++ = color;
    }
}

int main(int argc, char **argv)
{
    int    max_iter=50000;
    int    start_iter=100;
    int    frames=100;
    int    i,j;
    int    zac[]={0, 3, 6, 7, 8};
    int    kon[]={3, 6, 7, 8, 0};
    SDL_Event event;
    int done=0;

    pixmap = SDL_CreateRGBSurface(SDL_SWSURFACE, 320, 240, 24, 0x000000FF, 0x0000FF00, 0x00FF0000, 0x00000000);
    init_sdl();
    for (j=0; j<5; j++) {
        for (i=0; i<frames; i++) {
            memset(histogram, 0, IFS_PIXELS * sizeof(float));
            SDL_LockSurface(pixmap);
            recalcIFS(max_iter, start_iter, (float)i/(frames-1.0), zac[j], kon[j]);
            SDL_UnlockSurface(pixmap);
            gfx_bitblt(pixmap, (640-320)/2, (480-240)/2);
            SDL_Delay(10);
            gfx_flip();
            SDL_PollEvent(&event);
            switch (event.type)
            {
                case SDL_QUIT:
                    done = 1;
                    break;
                case SDL_KEYDOWN:
                    switch (event.key.keysym.sym)
                    {
                        case SDLK_ESCAPE:
                        case SDLK_q:
                            done = 1;
                            break;
                        default:
                            break;
                    }
            }
            if (done) {finalize();return 0;}
        }
        SDL_Delay(100);
    }
    finalize();
    return 0;
}

