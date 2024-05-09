#ifndef _GFX_H_
#define _GFX_H_

typedef struct GraphicsState {
    SDL_Window *window;
    SDL_Surface *screen_surface;
} GraphicsState;

void init_sdl(GraphicsState * graphicsState, const char *title, const int width, const int height);

void finalize(GraphicsState * graphicsState, SDL_Surface * pixmap);

void show_pixmap(GraphicsState * graphicsState, SDL_Surface * surface);

SDL_Surface *create_pixmap(const int width, const int height);

void putpixel(SDL_Surface * surface,
              int x, int y,
              unsigned char r, unsigned char g, unsigned char b);

void smooth_scene(SDL_Surface * pixmap);

#endif
