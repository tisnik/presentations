/* OpenVG (nejenom) na Raspberry Pi - dvacaty demonstracni priklad */
/* Vytvoreni screenshotu obrazovky - pouziti formatu BMP (BitMap) s 24bpp. */
/* Pouziti funkce vgReadPixels pro nacteni obsahu bufferu do operacni pameti */

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
    EGLint     num_config;
    EGLConfig  config;

    /* nutne pro RPi */
    bcm_host_init();

    /* pro jistotu vymazeme datovou strukturu nesouci stav EGL */
    memset(state, 0, sizeof(*state));

    static EGL_DISPMANX_WINDOW_T nativewindow;

    DISPMANX_ELEMENT_HANDLE_T dispman_element;
    DISPMANX_DISPLAY_HANDLE_T dispman_display;
    DISPMANX_UPDATE_HANDLE_T dispman_update;
    VC_RECT_T dst_rect;
    VC_RECT_T src_rect;

    static VC_DISPMANX_ALPHA_T alpha = {
        DISPMANX_FLAGS_ALPHA_FIXED_ALL_PIXELS,
        255, 0
    };

    static const EGLint attribute_list[] = {
        EGL_RED_SIZE, 8,
        EGL_GREEN_SIZE, 8,
        EGL_BLUE_SIZE, 8,
        EGL_ALPHA_SIZE, 8,
        EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
        EGL_NONE
    };

    /* vychozi displej */
    state->display = eglGetDisplay(EGL_DEFAULT_DISPLAY);

    /* inicializace displeje */
    result = eglInitialize(state->display, NULL, NULL);

    /* kontrola, zda operace probehla v poradku */
    if (result == EGL_FALSE) {
        puts("EGL init failed");
        exit(1);
    }

    /* navazani EGL na OpenVG */
    eglBindAPI(EGL_OPENVG_API);

    /* ziskani konfigurace framebufferu */
    result = eglChooseConfig(state->display, attribute_list, &config, 1, &num_config);

    /* kontrola, zda operace probehla v poradku */
    if (result == EGL_FALSE) {
        puts("EGL choose config failed");
        exit(1);
    }

    /* vytvoreni kontextu */
    state->context = eglCreateContext(state->display, config, EGL_NO_CONTEXT, NULL);

    /* kontrola, zda operace probehla v poradku */
    if (state->context == EGL_NO_CONTEXT) {
        puts("EGL create context failed");
        exit(1);
    }

    /* vytvoreni surface */
    int32_t success = graphics_get_display_size(0, &state->screen_width, &state->screen_height);

    /* kontrola, zda operace probehla v poradku */
    if (success < 0) {
        puts("get display size failed");
        exit(1);
    }

    if ((state->window_width == 0) || (state->window_width > state->screen_width))
        state->window_width = state->screen_width;
    if ((state->window_height == 0) || (state->window_height > state->screen_height))
        state->window_height = state->screen_height;

    dispman_display = vc_dispmanx_display_open(0);
    dispman_update = vc_dispmanx_update_start(0);

    dispman_element = vc_dispmanx_element_add(dispman_update, dispman_display, 0 /*layer */ , &dst_rect, 0 /*src */ ,
                          &src_rect, DISPMANX_PROTECTION_NONE, &alpha, 0 /*clamp */ ,
                          0 /*transform */ );

    nativewindow.element = dispman_element;
    nativewindow.width = state->window_width;
    nativewindow.height = state->window_height;
    vc_dispmanx_update_submit_sync(dispman_update);

    /* vytvoreni surface */
    state->surface = eglCreateWindowSurface(state->display, config, &nativewindow, NULL);

    /* kontrola, zda operace probehla v poradku */
    if (state->surface == EGL_NO_SURFACE) {
        puts("no surface!");
        exit(1);
    }

    /* nastaveni chovani bufferu pri operaci swap */
    result = eglSurfaceAttrib(state->display, state->surface, EGL_SWAP_BEHAVIOR, EGL_BUFFER_PRESERVED);

    /* kontrola, zda operace probehla v poradku */
    if (result == EGL_FALSE) {
        puts("can not set surface attributes!");
        exit(1);
    }

    /* propojeni kontextu se surface */
    result = eglMakeCurrent(state->display, state->surface, state->surface, state->context);

    /* kontrola, zda operace probehla v poradku */
    if (result == EGL_FALSE) {
        puts("can not connect context with the surface!");
        exit(1);
    }
}



/*
 * Ukonceni prace s EGL.
 */
void finalize_egl(EGL_STATE_T *state)
{
    eglSwapBuffers(state->display, state->surface);
    eglMakeCurrent(state->display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
    eglDestroySurface(state->display, state->surface);
    eglDestroyContext(state->display, state->context);
    eglTerminate(state->display);
}



/*
 * Vykresleni nekolika usecek a Bezierovych krivek.
 */
void draw(EGL_STATE_T *state)
{
    /* vymazani pozadi cernou barvou */
    VGfloat color1[4] = {0.0f, 0.0f, 0.0f, 1.0f};
    vgSetfv(VG_CLEAR_COLOR, 4, color1);
    vgClear(0, 0, state->window_width, state->window_height);

    /* sirka a styl stetce */
    vgSetf(VG_STROKE_LINE_WIDTH, 1);
    vgSeti(VG_STROKE_CAP_STYLE, VG_CAP_ROUND);
    vgSeti(VG_STROKE_JOIN_STYLE, VG_JOIN_ROUND);

    /* barva stetce prvni polycary */
    {
        VGfloat color2[4] = {0.25f, 0.25f, 0.75f, 1.0f};
        VGPaint strokePaint = vgCreatePaint();
        vgSetParameteri(strokePaint, VG_PAINT_TYPE, VG_PAINT_TYPE_COLOR);
        vgSetParameterfv(strokePaint, VG_PAINT_COLOR, 4, color2);
        vgSetPaint(strokePaint, VG_STROKE_PATH);
        vgDestroyPaint(strokePaint);
    }

    {
        /* vykresleni prvni cesty slozene z usecek */
        VGPath path = vgCreatePath(VG_PATH_FORMAT_STANDARD, VG_PATH_DATATYPE_F, 1.0f, 0.0f, 0, 0, VG_PATH_CAPABILITY_APPEND_TO);

        /* deklarace useckoveho segmentu */
        VGubyte commands[] = {VG_MOVE_TO_ABS,        /* pocatecni bod */
                              VG_LINE_TO_REL,        /* prvni useckovy segment */
                              VG_LINE_TO_REL,
                              VG_LINE_TO_REL,
                              VG_LINE_TO_REL};       /* dalsi useckove segmenty */

        VGfloat coordinates[] = {(state->window_width >> 1) - 400, state->window_height >> 1,
                                 100,  200,
                                 100,    0,
                                 100, -200};

        /* pridani vsech useckovych segmentu */
        vgAppendPathData(path, 5, commands, coordinates); 

        /* usecka nema "vnitrek", proto se pouzije pouze VG_STROKE_PATH */
        vgDrawPath(path, VG_STROKE_PATH);
        vgDestroyPath(path);
    }

    /* sirka a styl stetce */
    vgSetf(VG_STROKE_LINE_WIDTH, 3);
    vgSeti(VG_STROKE_CAP_STYLE, VG_CAP_ROUND);
    vgSeti(VG_STROKE_JOIN_STYLE, VG_JOIN_ROUND);

    /* barva stetce Bezierovych krivek */
    {
        VGfloat color2[4] = {0.75f, 0.25f, 0.25f, 1.0f};
        VGPaint strokePaint = vgCreatePaint();
        vgSetParameteri(strokePaint, VG_PAINT_TYPE, VG_PAINT_TYPE_COLOR);
        vgSetParameterfv(strokePaint, VG_PAINT_COLOR, 4, color2);
        vgSetPaint(strokePaint, VG_STROKE_PATH);
        vgDestroyPaint(strokePaint);
    }

    {
        /* vykresleni druhe cesty slozene z kubickychBezierovych krivek */
        VGPath path = vgCreatePath(VG_PATH_FORMAT_STANDARD, VG_PATH_DATATYPE_F, 1.0f, 0.0f, 0, 0, VG_PATH_CAPABILITY_APPEND_TO);

        /* deklarace useckoveho segmentu */
        VGubyte commands[] = {VG_MOVE_TO_ABS,        /* pocatecni bod */
                              VG_CUBIC_TO_REL,       /* Bezierova kubicka krivka */
                              VG_SCUBIC_TO_REL};     /* Bezierova kubicka krivka s hladkym napojenim */

        VGfloat coordinates[] = {(state->window_width >> 1) - 400, state->window_height >> 1,
                                 100, 200,           /* prvni ridici bod Bezierovy krivky */
                                 200, 200,           /* druhy ridici bod Bezierovy krivky */
                                 300, 000,           /* koncovy bod prvni Bezierovy krivky */
                                 200, 300,           /* ridici bod druhe Bezierovy krivky s hladkym napojenim */
                                 300, 000};          /* koncovy bod druhe Bezierovy krivky s hladkym napojenim */

        /* pridani vsech segmentu */
        vgAppendPathData(path, 3, commands, coordinates); 

        /* Bezierova krivka nema "vnitrek", proto se pouzije pouze VG_STROKE_PATH */
        vgDrawPath(path, VG_STROKE_PATH);
        vgDestroyPath(path);
    }

    /* barva stetce polycary */
    {
        VGfloat color2[4] = {0.75f, 0.75f, 0.25f, 1.0f};
        VGPaint strokePaint = vgCreatePaint();
        vgSetParameteri(strokePaint, VG_PAINT_TYPE, VG_PAINT_TYPE_COLOR);
        vgSetParameterfv(strokePaint, VG_PAINT_COLOR, 4, color2);
        vgSetPaint(strokePaint, VG_STROKE_PATH);
        vgDestroyPaint(strokePaint);
    }

    /* sirka a styl stetce */
    vgSetf(VG_STROKE_LINE_WIDTH, 20);
    vgSeti(VG_STROKE_CAP_STYLE, VG_CAP_BUTT);    /* siroke stopy konci presne na stanovenych souradnicich */
    vgSeti(VG_STROKE_JOIN_STYLE, VG_JOIN_BEVEL); /* vnejsi okraje spoju jsou "oseknute" */

    {
        /* vykresleni polycary */
        VGPath path = vgCreatePath(VG_PATH_FORMAT_STANDARD, VG_PATH_DATATYPE_F, 1.0f, 0.0f, 0, 0, VG_PATH_CAPABILITY_APPEND_TO);

        /* deklarace useckoveho segmentu */
        VGubyte commands[] = {VG_MOVE_TO_ABS,                  /* pocatecni bod */
                              VG_LINE_TO_REL,                  /* prvni usecka (vodorovna) */
                              VG_LINE_TO_REL,                  /* druha usecka (svisla) */
                              VG_LINE_TO_REL,                  /* treti usecka (vodorovna) */
                              VG_CLOSE_PATH};                  /* uzavreni cesty */

        VGfloat coordinates[] = {20, 20,                       /* pocatecni bod */
                                 state->window_width-40, 0,    /* prvni usecka (vodorovna) */
                                 0, state->window_height-40,   /* druha usecka (svisla) */
                                 -state->window_width+40, 0};  /* treti usecka (vodorovna) */

        /* pridani useckoveho segmentu */
        vgAppendPathData(path, 5, commands, coordinates); 

        /* usecka nema "vnitrek", proto se pouzije pouze VG_STROKE_PATH */
        vgDrawPath(path, VG_STROKE_PATH);
        vgDestroyPath(path);
    }

    /* prohozeni predniho a zadniho bufferu (pokud je to zapotrebi) */
    eglSwapBuffers(state->display, state->surface);
}



/*
 * Hlavicka souboru BMP (BitMap)
 */
unsigned char bmp_header[] =
{
    0x42, 0x4d,             /* magicke cislo */
    0x46, 0x00, 0x00, 0x00, /* velikost hlavicky=70 bajtu */
    0x00, 0x00,             /* nepouzito */
    0x00, 0x00,             /* nepouzito */
    0x36, 0x00, 0x00, 0x00, /* 54 bajtu - offset na zacatek vlastnich dat */
    0x28, 0x00, 0x00, 0x00, /* 40 bajtu - velikost hlavicky DIB */
    0x00, 0x00, 0x00, 0x00, /* sirka bitmapy */
    0x00, 0x00, 0x00, 0x00, /* vyska bitmapy */
    0x01, 0x0,              /* 1 pixel plane */
    0x18, 0x00,             /* 24 bpp */
    0x00, 0x00, 0x00, 0x00, /* bez komprese */
    0x00, 0x00, 0x00, 0x00, /* velikost pole pixelu */
    0x13, 0x0b, 0x00, 0x00, /* 2835 pixels/meter (vetsina SW ignoruje) */
    0x13, 0x0b, 0x00, 0x00, /* 2835 pixels/meter (vetsina SW ignoruje)  */
    0x00, 0x00, 0x00, 0x00, /* barvova paleta */
    0x00, 0x00, 0x00, 0x00, /* pocet dulezitych barev v palete (v 24 bpp ignorujeme) */
};



/*
 * Ulozeni pixmapy do externiho souboru
 */
void savePixmap(const unsigned int width, const unsigned int height,
                const unsigned char *pixels, const char *fileName)
{
    FILE *fout;
    unsigned int i;

    /* sirka bitmapy je zapsana ve ctverici bajtu */
    bmp_header[18] =  width & 0xff;
    bmp_header[19] = (width >> 8) & 0xff;
    bmp_header[20] = (width >> 16) & 0xff;
    bmp_header[21] = (width >> 24) & 0xff;

    /* vyska bitmapy je taktez zapsana ve ctverici bajtu */
    bmp_header[22] =  height & 0xff;
    bmp_header[23] = (height >> 8) & 0xff;
    bmp_header[24] = (height >> 16) & 0xff;
    bmp_header[25] = (height >> 24) & 0xff;

    fout=fopen(fileName, "wb");
    if (fout) {
                                           /* zapis hlavicky */
        fwrite(bmp_header, sizeof(bmp_header), 1, fout);
        unsigned char *p=pixels+1;         /* adresa prvniho pixelu (preskocime alfa slozku) */

        /* nyni zapiseme celou bitmapu do souboru, */
        /* z formatu 32bpp se jednoduchou konverzi vytvori format 24bpp */
        for (i=0; i<width*height; i++) {   /* projit celou zdrojovou bitmapou */
            fwrite(p, 3, 1, fout);         /* zapisujeme po cele trojici RGB */
            p+=4;                          /* posun na dalsi pixel ve zdrojovych datech */
        }
        fclose(fout);
    }
}



/*
 * Vytvoreni screenshotu obrazovky.
 */
void makeScreenshot(EGL_STATE_T *state, const char *filename)
{
    unsigned int width  = state->window_width;
    unsigned int height = state->window_height;
    unsigned char *data = (unsigned char*)malloc(width*height*4);

    /* precteni obsahu cele obrazovky do pametove oblasti 'data' */
    /* format je 32bitovy */
    vgReadPixels(data, width * 4, VG_sRGBX_8888, 0, 0, width, height);

    /* ulozeni obsahu obrazovky */
    savePixmap(width, height, data, filename);

    /* uvolneni jiz nepotrebne oblasti pameti */
    free(data);
}



/*
 * Vstupni bod do programu.
 */
int main(int argc, char *argv[])
{
    EGL_STATE_T egl_state;

    initialize_egl(&egl_state);
    puts("initialize_egl OK");

    /* vykresleni cele sceny */
    draw(&egl_state);

    /* vytvoreni screenshotu obrazovky */
    makeScreenshot(&egl_state, "example20.bmp");
    getchar();

    finalize_egl(&egl_state);
    puts("finalize_egl OK");

    return 0;
}

