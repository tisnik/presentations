/* OpenVG (nejenom) na Raspberry Pi - treti demonstracni priklad */

#include <stdio.h>

#include <VG/openvg.h>
#include <VG/vgu.h>
#include <EGL/egl.h>
#include <bcm_host.h>



/*
 * Datova struktura obsahujici cely stav EGL "sezeni".
 */
typedef struct
{
    uint32_t screen_width;
    uint32_t screen_height;

    uint32_t window_x;
    uint32_t window_y;
    int32_t  window_width;
    int32_t  window_height;

    EGLDisplay display;
    EGLSurface surface;
    EGLContext context;
    EGLConfig  config;
} EGL_STATE_T;



/*
 * Vypis konfigurace displeje nabizene pres EGL
 */
void print_egl_configuration(EGLDisplay display, EGLConfig *config)
{
#define yes_no(x) ((x)==EGL_TRUE ? "yes":"no ")

    int red, green, blue, alpha, buffer;
    int depth, stencil;
    int bind_to_rgb, bind_to_rgba;

    eglGetConfigAttrib(display, *config, EGL_RED_SIZE, &red);
    eglGetConfigAttrib(display, *config, EGL_BLUE_SIZE, &green);
    eglGetConfigAttrib(display, *config, EGL_GREEN_SIZE, &blue);
    eglGetConfigAttrib(display, *config, EGL_ALPHA_SIZE, &alpha);
    eglGetConfigAttrib(display, *config, EGL_BUFFER_SIZE, &buffer);
    eglGetConfigAttrib(display, *config, EGL_DEPTH_SIZE, &depth);
    eglGetConfigAttrib(display, *config, EGL_STENCIL_SIZE, &stencil);

    eglGetConfigAttrib(display, *config,  EGL_BIND_TO_TEXTURE_RGB,  &bind_to_rgb);
    eglGetConfigAttrib(display, *config,  EGL_BIND_TO_TEXTURE_RGBA, &bind_to_rgba);

    printf("%1d   %1d   %1d   %1d   %2d     %2d      %2d      %s  %s\n",
            red, green, blue, alpha, buffer,
            depth, stencil,
            yes_no(bind_to_rgb),
            yes_no(bind_to_rgba));
}



/*
 * Inicializace EGL.
 */
void initialize_egl(EGL_STATE_T *state)
{
    EGLBoolean result;
    EGLint     configurations_count;
    EGLConfig *all_configurations;

    /* nutne pro RPi */
    bcm_host_init();

    /* pro jistotu vymazeme datovou strukturu nesouci stav EGL */
    memset(state, 0, sizeof(*state));

    /* propojeni na vychozi displej */
    state->display = eglGetDisplay(EGL_DEFAULT_DISPLAY);

    /* inicializace displeje */
    result = eglInitialize(state->display, NULL, NULL);

    /* kontrola, zda inicializace probehla v poradku */
    if (result == EGL_FALSE) {
        puts("EGL init failed");
        exit(1);
    }

    /* precteni poctu konfiguraci dostupnych pres EGL */
    eglGetConfigs(state->display, NULL, 0, &configurations_count);
    printf("EGL has %d confugurations availabel\n", configurations_count);

    /* nacteni vsech konfiguraci do pripraveneho pole */
    all_configurations = malloc(configurations_count * sizeof(*all_configurations));
    eglGetConfigs(state->display, all_configurations, configurations_count, &configurations_count);

    puts("Configuration  R   G   B   A   bpp   depth stencil bind RGB/RGBA");
    /* postupny vypis vsech konfiguraci */
    int i;
    for (i = 0; i < configurations_count; i++) {
        printf("%3d            ", i);
        print_egl_configuration(state->display, &all_configurations[i]);
    }
    free(all_configurations);
}



/*
 * Ukonceni prace s EGL.
 */
void finalize_egl(EGL_STATE_T *state)
{
    /* nyni jsou tyto kroky prozatim zbytecne, v dalsich prikladech se vsak budou hodit */
    eglSwapBuffers(state->display, state->surface);
    eglMakeCurrent(state->display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
    eglDestroySurface(state->display, state->surface);
    eglDestroyContext(state->display, state->context);
    eglTerminate(state->display);
}



/*
 * Vstupni bod do programu.
 */
int main(int argc, char *argv[])
{
    EGL_STATE_T egl_state;

    initialize_egl(&egl_state);
    puts("initialize_egl OK");

    finalize_egl(&egl_state);
    puts("finalize_egl OK");

    return 0;
}

