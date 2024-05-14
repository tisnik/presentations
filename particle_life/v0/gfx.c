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
