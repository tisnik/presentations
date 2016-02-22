/* OpenVG (nejenom) na Raspberry Pi - prvni demonstracni priklad */

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
 * Inicializace EGL.
 */
void initialize_egl(EGL_STATE_T *state)
{
    EGLBoolean result;

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

