#ifdef __EMSCRIPTEN__
#include <emscripten.h>
#endif

#include <SDL2/SDL.h>

#define TITLE "SDL2 demo #1"
#define WIDTH  256
#define HEIGHT 256

typedef struct State {
    SDL_Window *window;
    SDL_Surface *screen_surface;
} State;

static void init_sdl(State * state, const int width, const int height)
{
    state->window = NULL;
    state->screen_surface = NULL;

    /* vlastni inicializace SDL */
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        fprintf(stderr, "Error initializing SDL: %s\n", SDL_GetError());
        exit(1);
    } else {
        puts("SDL_Init ok");
    }

    /* inicializace okna pro vykreslovani */
    state->window =
        SDL_CreateWindow(TITLE, SDL_WINDOWPOS_UNDEFINED,
                         SDL_WINDOWPOS_UNDEFINED, width, height,
                         SDL_WINDOW_SHOWN);

    if (!state->window) {
        puts("Error creating window");
        puts(SDL_GetError());
        exit(1);
    } else {
        puts("SDL_CreateWindow ok");
    }

    /* ziskani kreslici plochy okna */
    state->screen_surface = SDL_GetWindowSurface(state->window);

    if (!state->screen_surface) {
        fprintf(stderr, "Error setting video mode: %s\n", SDL_GetError());
        exit(1);
    } else {
        puts("SDL_GetWindowSurface ok");
    }
}

static void show_pixmap(State * state, SDL_Surface * surface)
{
    /* vykresleni pixmapy do plochy okna */
    SDL_BlitSurface(surface, NULL, state->screen_surface, NULL);
    SDL_UpdateWindowSurface(state->window);
}

static void draw_palette(SDL_Surface * surface)
{
    Uint8 *pixel;
    int x, y;

    if (SDL_MUSTLOCK(surface)) {
        SDL_LockSurface(surface);
    }

    /* nyni jiz muzeme pristupovat k pixelum pixmapy */
    pixel = (Uint8 *) surface->pixels;

    for (y = 0; y < surface->h; y++) {
        for (x = 0; x < surface->w; x++) {
            /* nastaveni barvy pixelu, ignorovani pruhlednosti */
            *pixel++ = x;
            *pixel++ = y;
            *pixel++ = 128;
            pixel++;
        }
    }

    if (SDL_MUSTLOCK(surface))
        SDL_UnlockSurface(surface);

}

static void main_event_loop(void)
{
    SDL_Event event;

    while (1) {
        /*SDL_WaitEvent(&event); */
        while (SDL_PollEvent(&event)) {
            switch (event.type) {
            case SDL_QUIT:
                return;
                break;          /* zbytecne, ale musime uchlacholit linter */
            case SDL_KEYDOWN:
                switch (event.key.keysym.sym) {
                case SDLK_ESCAPE:
                case SDLK_q:
                    return;
                    break;      /* zbytecne, ale musime uchlacholit linter */
                default:
                    break;
                }
                break;
            default:
                break;
            }
        }
    }
}

static void finalize(State * state, SDL_Surface * pixmap)
{
    /* uvolneni vsech prostredku */
    SDL_FreeSurface(pixmap);
    SDL_FreeSurface(state->screen_surface);
    SDL_DestroyWindow(state->window);
}

static SDL_Surface *create_pixmap(const int width, const int height)
{
    SDL_Surface *pixmap;
    pixmap =
        SDL_CreateRGBSurface(SDL_SWSURFACE, WIDTH, HEIGHT, 32, 0x00ff0000,
                             0x0000ff00, 0x000000ff, 0x00000000);
    if (!pixmap) {
        puts("Can not create pixmap");
        exit(1);
    } else {
        puts("Off screen pixmap created");
    }
    return pixmap;
}

int main(int argc, char **argv)
{
    State state;
    SDL_Surface *pixmap;

    /* inicializace SDL, vytvoreni okna a ziskani kreslici plochy okna */
    init_sdl(&state, WIDTH, HEIGHT);

    /* vytvoreni offscreen pixmapy */
    pixmap = create_pixmap(WIDTH, HEIGHT);

    /* vykresleni palety */
    draw_palette(pixmap);

    /* zobrazeni palety */
    show_pixmap(&state, pixmap);

#ifndef __EMSCRIPTEN__
    /* cekani na stisk klavesy */
    main_event_loop();

    /* uvolneni prostredku */
    finalize(&state, pixmap);
#endif

    return 0;
}
