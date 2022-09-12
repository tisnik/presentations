#include <SDL2/SDL.h>
#ifdef __EMSCRIPTEN__
#include <emscripten.h>
#endif
#include <stdlib.h>

#define TITLE "SDL2 demo #2"
#define WIDTH  256
#define HEIGHT 256

typedef struct State {
    SDL_Window *window;
    SDL_Renderer *renderer;
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

    state->renderer =
        SDL_CreateRenderer(state->window, -1, SDL_RENDERER_ACCELERATED);
    if (!state->renderer) {
        puts("Error creating renderer");
        puts(SDL_GetError());
        exit(1);
    } else {
        puts("SDL_CreateRenderer ok");
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

void draw_snowcrash(SDL_Surface * surface)
{
    Uint8 *pixel;
    int x, y;

    if (SDL_MUSTLOCK(surface)) {
        SDL_LockSurface(surface);
    }

    /* nyni jiz muzeme pristupovat k pixelum pixmapy */
    pixel = surface->pixels;

    for (y = 0; y < surface->h; y++) {
        for (x = 0; x < surface->w; x++) {
            /* nastaveni barvy pixelu, ignorovani pruhlednosti */
            *pixel++ = rand() % 255;
            *pixel++ = rand() % 255;
            *pixel++ = rand() % 255;
            pixel++;
        }
    }

    if (SDL_MUSTLOCK(surface))
        SDL_UnlockSurface(surface);
}

static void show_pixmap(State * state, SDL_Surface * surface)
{
    /* vykresleni pixmapy do plochy okna */
    SDL_Texture *screenTexture =
        SDL_CreateTextureFromSurface(state->renderer, surface);

    SDL_RenderClear(state->renderer);
    SDL_RenderCopy(state->renderer, screenTexture, NULL, NULL);
    SDL_RenderPresent(state->renderer);

    SDL_DestroyTexture(screenTexture);
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

static void main_event_loop(State * state, SDL_Surface * pixmap)
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
        draw_snowcrash(pixmap);
        show_pixmap(state, pixmap);
        SDL_Delay(16);
    }
}

static void finalize(State * state, SDL_Surface * pixmap)
{
    /* uvolneni vsech prostredku */
    SDL_FreeSurface(pixmap);
    SDL_FreeSurface(state->screen_surface);
    SDL_DestroyRenderer(state->renderer);
    SDL_DestroyWindow(state->window);
}

int main(int argc, char *argv[])
{
    State state;
    SDL_Surface *pixmap;

    /* inicializace SDL, vytvoreni okna a ziskani kreslici plochy okna */
    init_sdl(&state, WIDTH, HEIGHT);

    /* vytvoreni offscreen pixmapy */
    pixmap = create_pixmap(WIDTH, HEIGHT);

#ifdef __EMSCRIPTEN__
    emscripten_set_main_loop(drawRandomPixels, 0, 1);
#else
    main_event_loop(&state, pixmap);
#endif

    finalize(&state, pixmap);

    return 0;
}
