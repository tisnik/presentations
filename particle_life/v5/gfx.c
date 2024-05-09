#include <SDL2/SDL.h>

#include "gfx.h"

void init_sdl(GraphicsState *graphicsState, const char *title, const int width,
              const int height) {
    graphicsState->window = NULL;
    graphicsState->screen_surface = NULL;

    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        fprintf(stderr, "Error initializing SDL: %s\n", SDL_GetError());
        exit(1);
    } else {
        puts("SDL_Init ok");
    }

    graphicsState->window = SDL_CreateWindow(title, SDL_WINDOWPOS_UNDEFINED,
                                             SDL_WINDOWPOS_UNDEFINED, width,
                                             height, SDL_WINDOW_SHOWN);

    if (!graphicsState->window) {
        puts("Error creating window");
        puts(SDL_GetError());
        exit(1);
    } else {
        puts("SDL_CreateWindow ok");
    }

    graphicsState->screen_surface = SDL_GetWindowSurface(graphicsState->window);

    if (!graphicsState->screen_surface) {
        fprintf(stderr, "Error setting video mode: %s\n", SDL_GetError());
        exit(1);
    } else {
        puts("SDL_GetWindowSurface ok");
    }
}

void finalize(GraphicsState *graphicsState, SDL_Surface *pixmap) {
    SDL_FreeSurface(pixmap);
    SDL_FreeSurface(graphicsState->screen_surface);
    SDL_DestroyWindow(graphicsState->window);
    SDL_Quit();
}

void show_pixmap(GraphicsState *graphicsState, SDL_Surface *surface) {
    SDL_BlitSurface(surface, NULL, graphicsState->screen_surface, NULL);
    SDL_UpdateWindowSurface(graphicsState->window);
}

SDL_Surface *create_pixmap(const int width, const int height) {
    SDL_Surface *pixmap;
    pixmap = SDL_CreateRGBSurface(SDL_SWSURFACE, width, height, 32, 0x00ff0000,
                                  0x0000ff00, 0x000000ff, 0x00000000);
    if (!pixmap) {
        puts("Can not create pixmap");
        exit(1);
    } else {
        puts("Off screen pixmap created");
    }
    return pixmap;
}

void putpixel(SDL_Surface *surface, int x, int y, unsigned char r,
              unsigned char g, unsigned char b) {
    if (x >= 0 && x < surface->w && y >= 0 && y < surface->h) {
        if (surface->format->BitsPerPixel == 24) {
            Uint8 *pixel = (Uint8 *)surface->pixels;
            pixel += x * 3;
            pixel += y * surface->pitch;
            *pixel++ = b;
            *pixel++ = g;
            *pixel = r;
            return;
        }
        if (surface->format->BitsPerPixel == 32) {
            Uint8 *pixel = (Uint8 *)surface->pixels;
            pixel += x * 4;
            pixel += y * surface->pitch;
            *pixel++ = b;
            *pixel++ = g;
            *pixel = r;
            return;
        }
    }
}

void smooth_scene(SDL_Surface *pixmap) {
    SDL_Surface *tmp =
        SDL_ConvertSurface(pixmap, pixmap->format, SDL_SWSURFACE);
    Uint8 *src;
    Uint8 *dst;
    int x, y;
    int srcc_offset;

    SDL_FillRect(pixmap, NULL, 0x00);
    dst = (Uint8 *)pixmap->pixels + 1 * pixmap->pitch +
          1 * pixmap->format->BytesPerPixel;
    src = (Uint8 *)tmp->pixels;

    srcc_offset = tmp->pitch - 3 * tmp->format->BytesPerPixel;

    for (y = 1; y < tmp->h; y++) {
        for (x = 1; x < tmp->w - 1; x++) {
            Uint8 *srcc = src + (x - 1) * tmp->format->BytesPerPixel;
            int rr = 0, gg = 0, bb = 0;
            int dx, dy;
            for (dy = -1; dy <= 1; dy++) {
                for (dx = -1; dx <= 1; dx++) {
                    bb += *srcc++;
                    gg += *srcc++;
                    rr += *srcc++;
                    if (tmp->format->BytesPerPixel == 4) {
                        srcc++;
                    }
                }
                srcc += srcc_offset;
            }
            rr /= 9;
            gg /= 9;
            bb /= 9;
            *dst++ = bb;
            *dst++ = gg;
            *dst++ = rr;
            if (pixmap->format->BitsPerPixel == 32) {
                dst++;
            }
        }
        dst += 2 * pixmap->format->BytesPerPixel;
        src += tmp->pitch;
    }
}
