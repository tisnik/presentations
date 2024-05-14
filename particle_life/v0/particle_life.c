#include <SDL2/SDL.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "gfx.h"

/* graphics options */
#define WIDTH 640
#define HEIGHT 480
#define TITLE "Life simulator"

/* model options */
#define BORDER 50

/* total number of particles */
#define MAX_PARTICLES 1000

#define DAMPING_FACTOR 0.5

typedef struct {
    float x;
    float y;
} Particle;

typedef struct Color {
    unsigned char r;
    unsigned char g;
    unsigned char b;
} Color;

typedef struct {
    Particle *particles;
    int max;
    Color color;
} ParticleSystem;

typedef struct {
    ParticleSystem particle_system;
} Model;

float random_x() {
    return (WIDTH - BORDER * 2) * (float)rand() / RAND_MAX + BORDER;
}

float random_y() {
    return (HEIGHT - BORDER * 2) * (float)rand() / RAND_MAX + BORDER;
}

void create_particles(int max, Particle *particles) {
    int i;
    for (i = 0; i < max; i++) {
        particles[i].x = random_x();
        particles[i].y = random_y();
    }
}

void redraw(GraphicsState *graphicsState, SDL_Surface *pixmap, Model *model) {
    int i;

    ParticleSystem particle_system = model->particle_system;

    SDL_FillRect(pixmap, NULL, 0x00);
    for (i = 0; i < particle_system.max; i++) {
        Particle particle = particle_system.particles[i];
        Color color = particle_system.color;
        putpixel(pixmap, particle.x, particle.y, color.r, color.g, color.b);
        putpixel(pixmap, particle.x - 1, particle.y, color.r, color.g, color.b);
        putpixel(pixmap, particle.x + 1, particle.y, color.r, color.g, color.b);
        putpixel(pixmap, particle.x, particle.y - 1, color.r, color.g, color.b);
        putpixel(pixmap, particle.x, particle.y + 1, color.r, color.g, color.b);
    }

    show_pixmap(graphicsState, pixmap);
}

static void main_event_loop(GraphicsState *graphicsState, SDL_Surface *pixmap,
                            Model *model) {
    SDL_Event event;
    int done = 0;

    do {
        while (SDL_PollEvent(&event)) {
            switch (event.type) {
            case SDL_QUIT:
                done = 1;
                break;
            case SDL_KEYDOWN:
                switch (event.key.keysym.sym) {
                case SDLK_ESCAPE:
                case SDLK_q:
                    done = 1;
                    break;
                default:
                    break;
                }
                break;
            default:
                break;
            }
        }
        redraw(graphicsState, pixmap, model);
        SDL_Delay(10);
    } while (!done);
}

Model init_model(void) {
    Color color = {255, 255, 80};
    Model model;

    model.particle_system.color = color;

    model.particle_system.particles =
        (Particle *)malloc(MAX_PARTICLES * sizeof(Particle));
    model.particle_system.max = MAX_PARTICLES;

    create_particles(MAX_PARTICLES, model.particle_system.particles);

    return model;
}

int main(int argc, char **argv) {
    GraphicsState graphicsState;
    Model model;
    SDL_Surface *pixmap;

    init_sdl(&graphicsState, TITLE, WIDTH, HEIGHT);

    pixmap = create_pixmap(WIDTH, HEIGHT);

    model = init_model();

    main_event_loop(&graphicsState, pixmap, &model);

    finalize(&graphicsState, pixmap);

    return 0;
}
