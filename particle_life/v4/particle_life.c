#include <SDL2/SDL.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "gfx.h"

/* graphics options */
#define WIDTH 640
#define HEIGHT 480
#define TITLE "Life simulator"

/* constants used by model */
#define RED 0
#define GREEN 1
#define YELLOW 2
#define BLUE 3

/* model options */
#define BORDER 50

/* number of particles of different colors/attributes */
#define MAX_RED 3000
#define MAX_GREEN 200
#define MAX_BLUE 100
#define MAX_YELLOW 100

/* total number of particles */
#define MAX_PARTICLES (MAX_RED + MAX_GREEN + MAX_BLUE + MAX_YELLOW)

#define MAX_DISTANCE 50

#define DAMPING_FACTOR 0.5

#define SCALE_FACTOR 1

/* integration constant */
#define DT 1.0

typedef struct {
    float x;
    float y;
    float vx;
    float vy;
    int type;
} Particle;

typedef struct Color {
    unsigned char r;
    unsigned char g;
    unsigned char b;
} Color;

typedef struct {
    Particle *particles;
    int max;
    Color colors[4];
} ParticleSystem;

typedef struct {
    float rules[4][4];
    ParticleSystem particle_system;
} Model;

void init_rules(Model *model) {
    int i, j;

    for (j = 0; j < 4; j++) {
        for (i = 0; i < 4; i++) {
            model->rules[i][j] = 2.0 * (float)rand() / RAND_MAX - 1.0;
        }
    }
}

float random_x() {
    return (WIDTH - BORDER * 2) * (float)rand() / RAND_MAX + BORDER;
}

float random_y() {
    return (HEIGHT - BORDER * 2) * (float)rand() / RAND_MAX + BORDER;
}

void create_particles(int max, Particle *particles, int type) {
    int i;
    for (i = 0; i < max; i++) {
        particles[i].x = random_x();
        particles[i].y = random_y();
        particles[i].vx = (float)rand() / RAND_MAX - 0.5;
        particles[i].vy = (float)rand() / RAND_MAX - 0.5;
        particles[i].type = type;
    }
}

void redraw(GraphicsState *graphicsState, SDL_Surface *pixmap, Model *model) {
    int i;

    ParticleSystem particle_system = model->particle_system;

    SDL_FillRect(pixmap, NULL, 0x00);
    for (i = 0; i < particle_system.max; i++) {
        Particle particle = particle_system.particles[i];
        Color color = particle_system.colors[particle.type];
        putpixel(pixmap, particle.x, particle.y, color.r, color.g, color.b);
        putpixel(pixmap, particle.x - 1, particle.y, color.r, color.g, color.b);
        putpixel(pixmap, particle.x + 1, particle.y, color.r, color.g, color.b);
        putpixel(pixmap, particle.x, particle.y - 1, color.r, color.g, color.b);
        putpixel(pixmap, particle.x, particle.y + 1, color.r, color.g, color.b);
    }

    show_pixmap(graphicsState, pixmap);
}

void apply_rules(Model *model) {
    int i, j;

    for (i = 0; i < model->particle_system.max; i++) {
        float fx = 0.0;
        float fy = 0.0;
        Particle *a = &model->particle_system.particles[i];

        /* compute force for selected particle */
        for (j = 0; j < model->particle_system.max; j++) {
            if (i != j) {
                Particle *b = &model->particle_system.particles[j];
                float g = model->rules[a->type][b->type] * SCALE_FACTOR;
                float dx = a->x - b->x;
                float dy = a->y - b->y;
                if (dx != 0.0 || dy != 0.0) {
                    float d = dx * dx + dy * dy;
                    if (d < MAX_DISTANCE * MAX_DISTANCE) {
                        /* repel force */
                        float f = g / sqrt(d);
                        fx += f * dx;
                        fy += f * dy;
                    }
                }
            }
        }

        /* apply force to selected particle */
        a->vx = (a->vx + fx * DT) * DAMPING_FACTOR;
        a->vy = (a->vy + fy * DT) * DAMPING_FACTOR;

        /* move particle */
        a->x += a->vx;
        a->y += a->vy;

        /* check if particle touches scene boundary */
        if (a->x <= 0) {
            a->vx = -a->vx;
            a->x = 0;
        }
        if (a->x > WIDTH) {
            a->vx = -a->vx;
            a->x = WIDTH - 1;
        }
        if (a->y <= 0) {
            a->vy = -a->vy;
            a->y = 0;
        }
        if (a->y > HEIGHT) {
            a->vy = -a->vy;
            a->y = HEIGHT - 1;
        }
    }
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
        apply_rules(model);
        redraw(graphicsState, pixmap, model);
        SDL_Delay(10);
    } while (!done);
}

Model init_model(void) {
    Color redColor = {255, 80, 80};
    Color greenColor = {80, 255, 80};
    Color blueColor = {80, 80, 255};
    Color yellowColor = {255, 255, 80};

    Model model;

    init_rules(&model);
    model.particle_system.colors[RED] = redColor;
    model.particle_system.colors[GREEN] = greenColor;
    model.particle_system.colors[BLUE] = blueColor;
    model.particle_system.colors[YELLOW] = yellowColor;

    model.particle_system.particles =
        (Particle *)malloc(MAX_PARTICLES * sizeof(Particle));
    model.particle_system.max = MAX_PARTICLES;

    create_particles(MAX_RED, model.particle_system.particles, RED);
    create_particles(MAX_GREEN, model.particle_system.particles + MAX_RED, GREEN);
    create_particles(MAX_BLUE, model.particle_system.particles + MAX_RED + MAX_GREEN,
                    BLUE);
    create_particles(MAX_YELLOW,
                    model.particle_system.particles + MAX_RED + MAX_GREEN + MAX_BLUE,
                    YELLOW);

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
