//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Autor: Pavel Tisnovsky
//
// Vykresleni trojrozmernych fraktalnich obrazcu pomoci algoritmu pro tvorbu
// systemu iterovanych funkci IFS. Pomoci mysi je mozne vytvorenym trojrozmernym
// modelem natacet a pohybovat s nim. Klavesove zkratky urcene k ovladani
// tohoto programu jsou popsany primo v clanku.
// Ukonceni aplikace se provede klavesou [Esc] nebo klavesou [Q].
//-----------------------------------------------------------------------------
#ifdef __BORLANDC__
#include <windows.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <GL/glut.h>

#define SURFEL_LIST_FLOAT   1
#define FONT          GLUT_BITMAP_8_BY_13
#define WINDOW_WIDTH  620
#define WINDOW_HEIGHT 460
#define WINDOW_LEFT   10
#define WINDOW_TOP    10
#define WINDOW_TITLE  "Fraktaly 40.1 - trojrozmerne IFS    author: Pavel Tisnovsky"

#define MIN(A,B)    ((A)<(B))?(A):(B)
#define MAX(A,B)    ((A)>(B))?(A):(B)

#define PI          3.14159279
#define PI2         PI*2.0

#define MINX        0.0
#define MAXX        100.0
#define MINY        0.0
#define MAXY        100.0
#define MINZ        0.0
#define MAXZ        100.0
#define ORIGIN_X   (MINX+MAXX)/2.0
#define ORIGIN_Y   (MINY+MAXY)/2.0
#define ORIGIN_Z   (MINZ+MAXZ)/2.0
#define RANGE_X    (MAXX-MINX)
#define RANGE_Y    (MAXY-MINY)
#define RANGE_Z    (MAXZ-MINZ)
#define RADIUS_X   (RANGE_X)/2.0
#define RADIUS_Y   (RANGE_Y)/2.0
#define RADIUS_Z   (RANGE_Z)/2.0
#define RADIUS_T   16

#ifdef HOTKEYS
#define _ "&"
#else
#define _
#endif

#ifdef nil
#undef nil
#endif

#define nil NULL

#ifndef __cplusplus

#ifndef true
#define true 1
#endif

#ifndef false
#define false 0
#endif

#endif

// typedefs {{{



typedef struct  TagGpeMenu {
    char       *caption;
    int         id;
    struct      TagGpeMenu *subMenu;
} GpeMenu;

typedef struct  Mouse {
    int         xnew, ynew, znew;
    int         xold, yold, zold;
    int         x1,   y1,   z1;
    int         status;
    int         xtran0, ytran0;
    int         xtran1, ytran1;
    int         xtran2, ytran2;
} Mouse;

typedef struct  View {
    float       fov;
    float       nearPlane;
    float       farPlane;
    int         windowWidth;
    int         windowHeight;
    int         surfelsSize;
    int         help;
    int         info;
    int         axis;
    int         shading;
    int         zBuffer;
} View;

typedef struct  Object {
    int         type;
    int         size;
    float       colorR;
    float       colorG;
    float       colorB;
    float       alpha;
    int         blending;
    int         surfelList;
} Object;

typedef struct  ScrollBar{
    int         xmin;
    int         xmax;
    int         ymin;
    int         ymax;
    int         position;
} Scrollbar;

typedef struct  ButtonStruct {
    void        (*callback)(void);
    int         menu;
    int         xmin;
    int         xmax;
    int         ymin;
    int         ymax;
} ButtonStruct;

typedef enum Commands {
    CommandNone=0,
    CommandModelPyramid=0,
    CommandModelTetrahedron1,
    CommandModelTetrahedron2,
    CommandModelHexahedron,
    CommandModelCube,
    CommandModelOctahedron,
    CommandModelDuodecahedron,
    CommandModelFern,
    CommandModelWing,
    CommandModelLeaf,
    CommandModelBush,
    CommandModelFlash,
    CommandModelTower,
    CommandModelArtefact1,
    CommandModelArtefact2,
    CommandModelArtefact3,
    CommandModelArtefact4,
    CommandModelArtefact5,
    CommandModelArtefact6,
    CommandModelArtefact7,
    CommandSurfelCount100,
    CommandSurfelCount400,
    CommandSurfelCount625,
    CommandSurfelCount2500,
    CommandSurfelCount10000,
    CommandSurfelCount22500,
    CommandSurfelCount40000,
    CommandSurfelCount62500,
    CommandSurfelSize1,
    CommandSurfelSize2,
    CommandSurfelSize3,
    CommandSurfelSize4,
    CommandSurfelSize5,
    CommandSurfelSize6,
    CommandSurfelSize7,
    CommandSurfelSize8,
    CommandSurfelSize9,
    CommandBlendingEnable,
    CommandBlendingDisable,
    CommandBlending01,
    CommandBlending02,
    CommandBlending03,
    CommandBlending04,
    CommandBlending05,
    CommandBlending06,
    CommandBlending07,
    CommandBlending08,
    CommandBlending09,
    CommandBlending10,
    CommandSavePositions,
    CommandSavePositionsSize,
    CommandShadingNone,
    CommandShadingX,
    CommandShadingY,
    CommandShadingZ,
    CommandShadingFog,
    CommandZBufferEnable,
    CommandZBufferDisable,
    CommandRedraw,
    CommandShowAxis,
    CommandHideAxis,
    CommandShowHelp,
    CommandHideHelp,
    CommandShowInfo,
    CommandHideInfo,
    CommandViewOriginal,
    CommandViewTop,
    CommandViewBottom,
    CommandViewLeft,
    CommandViewRight,
    CommandSettingsReset,
    CommandSettingsLoad,
    CommandSettingsSave,
    CommandSettingsSurfelsCount,
    CommandSettingsModelForeground,
    CommandSettingsModelBackground,
    CommandSettingsFogColor,
    CommandSettingsAxesColor,
    CommandSettingsActiveItemColor,
    CommandSettingsHelpForeground,
    CommandSettingsHelpBackground,
    CommandSettingsInfoForeground,
    CommandSettingsInfoBackground,
    CommandSettingsScrollBarColor,
    CommandQuitYes,
    CommandQuitNo
} MenuCommands;

typedef struct Vector3f {
    float x;
    float y;
    float z;
} Vector3f;

typedef struct      SurfelF {
    Vector3f        position;
    Vector3f        normal;
    unsigned char   size;
    unsigned int    color;
} SurfelF;

typedef struct      SurfelList {
    int             type;
    int             itemsCount;
    int             currentItem;
    union {
        SurfelF         *itemsF;
    } items;
} SurfelList;



// }}}

// function headers {{{



void     confInit(View *view, Scrollbar *scrollbar, Mouse *mouse, int *settings, int *activeItem);
int      inButton(const ButtonStruct buttons[], const int i, const int x, const int y);
int      inMainMenuButton(int x, int y);
int      inScrollbar(Scrollbar *s, int x, int y);
void     setMenuForButton(const ButtonStruct buttons[], const int x, const int y);
void     setMenuForMainButton(int x, int y);
void     processScrollbars(int x, int y);
void     processLeftMouseButton(const ButtonStruct buttons[], const int state, const int x, const int y);
void     processRightMouseButton(int state, int x, int y);
GLfloat *getAxisColor(void);
GLfloat *getHelpColor(void);
GLfloat *getInfoColor(void);
GLfloat *getModelColor(void);
GLfloat *getActiveItemColor(void);
GLfloat *getScrollBarColor(void);
GLfloat *getHelpBackground(void);
GLfloat *getInfoBackground(void);
GLfloat *getModelBackground(void);
GLfloat *getFogColor(void);
void     setModelAlpha(GLfloat alpha);
void     getCurrentColor(GLfloat *r, GLfloat *g, GLfloat *b, GLfloat *a);
void     setCurrentColor(GLfloat r, GLfloat g, GLfloat b, GLfloat a);
void     settingsReset(void);
void     settingsLoad(void);
void     settingsSave(void);
float    arandom(float max);
void     objectInit(Object *o);
void     objectCreate(Object *o, int type, int grid);
void     objectDestroy(Object *o);
void     objectSizeMove(Object *o);
void     objectSave(Object *o);
void     objectSaveSize(Object *o, View *v);
void     drawObject(Object *o, View *v);
void     drawObjectNoShading(Object *o);
void     drawObjectXShading(Object *o);
void     drawObjectYShading(Object *o);
void     drawObjectZShading(Object *o);
void     drawObjectFogShading(Object *o);
void     drawString(char *string, int x, int y, int z);
void     drawAxis(void);
void     drawScrollbar(View *v, Scrollbar *s);
void     drawInfo(Object *o, View *v, char *objectType, int activeItem);
void     drawSurfelsInfo(Object *o, View *v, Mouse *m, int activeItem);
void     drawColorScrollbars(View *v, int settings, int activeItem);
void     drawHelp(View *v);
void     drawMainMenu(View *v, int activeItem);
void     onInit(void);
void     onResize(int w, int h);
void     onDisplay(void);
void     onKeyboard(unsigned char key, int x, int y);
void     onSpecialKeyboard(int key, int x, int y);
void     onMouseButton(int button, int state, int x, int y);
void     onMouseMotion(int x, int y);
void     onPassiveMotion(int x, int y);
void     onMenu(int command);
void     mouseInit(Mouse *m);
void     viewInit(View *v);
void     updateScrollbar(Scrollbar *s, int x, int y);
void     buttonsInit(void);
void     buttonObjectClick(void);
void     buttonSurfelsSizeClick(void);
void     buttonShadingClick(void);
void     buttonZBufferClick(void);
void     buttonSurfelsCountClick(void);
void     buttonBlendingClick(void);
void     buttonSettingsClick(void);
void     createMenu(void);
int      surfelInit(void);
int      surfelListInit(int type);
int      surfelListDone(int surfelList);
int      surfelListAlloc(int surfelList, int itemCount);
int      surfelListDestroy(int surfelList);
int      surfelListSetSurfelF(int surfelList, SurfelF *surfel);
int      surfelListGetSurfelF(int surfelList, SurfelF *surfel);
int      surfelListFirst(int surfelList);
int      surfelListNext(int surfelList);
int      surfelListIsLast(int surfelList);
int      surfelGetCount(int surfelList);
int      surfelListSaveP(int surfelList, const char * fileName);
int      surfelListSavePS(int surfelList, const char * fileName);
int      gpeCreateMenuFromData(GpeMenu *menu, void (*f)(int command));
int      gpeCreateMenu(GpeMenu *menu, void (*f)(int command));
int      main(int argc, char *argv[]);



// }}}

// variables {{{



Object    o;
int       modelMenu;
int       surfelMenu;
int       shadingMenu;
int       zBufferMenu;
int       surfelCountMenu;
int       blendingMenu;
int       settingsMenu;
int       mainMenu;
const int CommandModelFirst=CommandModelPyramid;
const int CommandModelLast=CommandModelArtefact7;
static Mouse     m;
static View      v;
static Scrollbar s={230, 480, 55, 68, 100};
static float     rotX=0.0f;
static float     rotY=0.0f;
static float     rotXd=0.0f;
static float     rotYd=0.0f;
static int       settings=CommandSettingsSurfelsCount;
static int       activeItem=0;
View      *v_conf=nil;
Scrollbar *s_conf=nil;
Mouse     *m_conf=nil;
int       *set=nil;
int       *active=0;
GLfloat   axisColor[4];
GLfloat   helpColor[4];
GLfloat   infoColor[4];
GLfloat   modelColor[4];
GLfloat   scrollBarColor[4];
GLfloat   activeItemColor[4];
GLfloat   helpBackground[4];
GLfloat   infoBackground[4];
GLfloat   modelBackground[4];
GLfloat   fogColor[4];



// }}}
// ButtonStruct buttons[] {{{



ButtonStruct buttons[]={
    {buttonObjectClick,      0,  10, 200, 70, 85},
    {buttonSurfelsSizeClick, 0,  10, 200, 55, 70},
    {buttonShadingClick,     0,  10, 200, 40, 55},
    {buttonZBufferClick,     0,  10, 200, 25, 40},
    {buttonSurfelsCountClick,0, 220, 556, 40, 54},
    {buttonBlendingClick,    0,  10, 200, 10, 25},
    {buttonSettingsClick,    0, 230, 556, 69, 85},
    {nil,                    0,   0,   0,  0,  0}
};



// }}}
// char *modelString() {{{



char *modelString[]={
    "Pyramid",
    "Tetrahedron1",
    "Tetrahedron2",
    "Hexahedron",
    "Cube",
    "Octahedron",
    "Duodecahedron",
    "Fern",
    "Wing",
    "Leaf",
    "Bush",
    "Flash",
    "Tower",
    "Artefact 1",
    "Artefact 2",
    "Artefact 3",
    "Artefact 4",
    "Artefact 5",
    "Artefact 6",
    "Artefact 7"
};



// }}}
// char *shadingString[] {{{



char *shadingString[]={
    "none",
    "X-axis",
    "Y-axis",
    "Z-axis",
    "fog"
};



// }}}
// menuModel1[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuModel1[]={
    {_"Pyramid",                        CommandModelPyramid,            nil},
    {_"Tetrahedron 1",                  CommandModelTetrahedron1,       nil},
    {"Tetrahedron "_"2",                CommandModelTetrahedron2,       nil},
    {_"Hexahedron",                     CommandModelHexahedron,         nil},
    {_"Cube",                           CommandModelCube,               nil},
    {_"Octahedron",                     CommandModelOctahedron,         nil},
    {_"Duodecahedron",                  CommandModelDuodecahedron,      nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuModel2[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuModel2[]={
    {_"Fern",                           CommandModelFern,               nil},
    {_"Wing",                           CommandModelWing,               nil},
    {_"Leaf",                           CommandModelLeaf,               nil},
    {_"Bush",                           CommandModelBush,               nil},
    {"Fl"_"ash",                        CommandModelFlash,              nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuModel3[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuModel3[]={
    {_"Tower",                          CommandModelTower,              nil},
    {"Artefact "_"1",                   CommandModelArtefact1,          nil},
    {"Artefact "_"2",                   CommandModelArtefact2,          nil},
    {"Artefact "_"3",                   CommandModelArtefact3,          nil},
    {"Artefact "_"4",                   CommandModelArtefact4,          nil},
    {"Artefact "_"5",                   CommandModelArtefact5,          nil},
    {"Artefact "_"6",                   CommandModelArtefact6,          nil},
    {"Artefact "_"7",                   CommandModelArtefact7,          nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuModel[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuModel[]={
    {_"Geometric models",               CommandNone,                    menuModel1},
    {_"Nature models",                  CommandNone,                    menuModel2},
    {_"Artifical structures",           CommandNone,                    menuModel3},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuSurfelCount[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuSurfelCount[]={
    {_"100",                            CommandSurfelCount100,          nil},
    {_"400",                            CommandSurfelCount400,          nil},
    {_"625",                            CommandSurfelCount625,          nil},
    {_"2500",                           CommandSurfelCount2500,         nil},
    {"1"_"0000",                        CommandSurfelCount10000,        nil},
    {"22"_"500",                        CommandSurfelCount22500,        nil},
    {"40000",                           CommandSurfelCount40000,        nil},
    {_"62500",                          CommandSurfelCount62500,        nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuSurfelSize[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuSurfelSize[]={
    {"Surfel size "_"1",                CommandSurfelSize1,             nil},
    {"Surfel size "_"2",                CommandSurfelSize2,             nil},
    {"Surfel size "_"3",                CommandSurfelSize3,             nil},
    {"Surfel size "_"4",                CommandSurfelSize4,             nil},
    {"Surfel size "_"5",                CommandSurfelSize5,             nil},
    {"Surfel size "_"6",                CommandSurfelSize6,             nil},
    {"Surfel size "_"7",                CommandSurfelSize7,             nil},
    {"Surfel size "_"8",                CommandSurfelSize8,             nil},
    {"Surfel size "_"9",                CommandSurfelSize9,             nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuShading[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuShading[]={
    {_"None\tN",                        CommandShadingNone,             nil},
    {"Along "_"X-axis\tX",              CommandShadingX,                nil},
    {"Along "_"Y-axis\tY",              CommandShadingY,                nil},
    {"Along "_"Z-axis\tZ",              CommandShadingZ,                nil},
    {"F"_"og\tO",                       CommandShadingFog,              nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuBlendFactor[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuBlendFactor[]={
    {"0."_"1\tF1",                      CommandBlending01,              nil},
    {"0."_"2\tF2",                      CommandBlending02,              nil},
    {"0."_"3\tF3",                      CommandBlending03,              nil},
    {"0."_"4\tF4",                      CommandBlending04,              nil},
    {"0."_"5\tF5",                      CommandBlending05,              nil},
    {"0."_"6\tF6",                      CommandBlending06,              nil},
    {"0."_"7\tF7",                      CommandBlending07,              nil},
    {"0."_"8\tF8",                      CommandBlending08,              nil},
    {"0."_"9\tF9",                      CommandBlending09,              nil},
    {"1."_"0\tF10",                     CommandBlending10,              nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuBlending[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuBlending[]={
    {_"Enable blending",                CommandBlendingEnable,          nil},
    {_"Disable blending",               CommandBlendingDisable,         nil},
    {"Blend "_"factor",                 CommandNone,                    menuBlendFactor},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuZBuffer[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuZBuffer[]={
    {_"Enable depth buffer",            CommandZBufferEnable,           nil},
    {_"Disable depth buffer",           CommandZBufferDisable,          nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuSave[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuSave[]={
    {_"Position only\tP",               CommandSavePositions,           nil},
    {"Position and "_"size\tS",         CommandSavePositionsSize,       nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuAxis[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuAxis[]={
    {_"Show axes",                      CommandShowAxis,                nil},
    {_"Hide axes",                      CommandHideAxis,                nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuHelp[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuHelp[]={
    {_"Show help",                      CommandShowHelp,                nil},
    {_"Hide help",                      CommandHideHelp,                nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuInfo[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuInfo[]={
    {_"Show info",                      CommandShowInfo,                nil},
    {_"Hide info",                      CommandHideInfo,                nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuQuit[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuQuit[]={
    {_"Quit now",                       CommandQuitYes,                 nil},
    {_"Not yet",                        CommandQuitNo,                  nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuView[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuView[]={
    {_"Original view\tInsert",          CommandViewOriginal,            nil},
    {"View from "_"top\tPage Up",       CommandViewTop,                 nil},
    {"View from "_"bottom\tPage Down",  CommandViewBottom,              nil},
    {"View from "_"left\tHome",         CommandViewLeft,                nil},
    {"View from "_"right\tEnd",         CommandViewRight,               nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuSettings[] {{{



// ----------------------------------------------------------------------------
// submenu definition
// ----------------------------------------------------------------------------
GpeMenu menuSettings[]={
    {_"Surfels count",                  CommandSettingsSurfelsCount,    nil},
    {"",                                CommandNone,                    nil},
    {_"Model foreground",               CommandSettingsModelForeground, nil},
    {"Model "_"background",             CommandSettingsModelBackground, nil},
    {_"Fog color",                      CommandSettingsFogColor,        nil},
    {_"Axes color",                     CommandSettingsAxesColor,       nil},
    {"",                                CommandNone,                    nil},
    {"Active item color",               CommandSettingsActiveItemColor, nil},
    {_"Help foreground",                CommandSettingsHelpForeground,  nil},
    {"H"_"elp background",              CommandSettingsHelpBackground,  nil},
    {_"Info foreground",                CommandSettingsInfoForeground,  nil},
    {"I"_"nfo background",              CommandSettingsInfoBackground,  nil},
    {"",                                CommandNone,                    nil},
    {_"Reset settings\t^R",             CommandSettingsReset,           nil},
    {_"Load settings\t^L",              CommandSettingsLoad,            nil},
    {_"Save settings\t^S",              CommandSettingsSave,            nil},
    {nil,                               CommandNone,                    nil}
};



// }}}
// menuMain[] {{{



// ----------------------------------------------------------------------------
// main menu definition
// ----------------------------------------------------------------------------
GpeMenu menuMain[]={
    {_"Model type",                     CommandNone,                    menuModel},
    {"Surfel count\tC",                 CommandNone,                    menuSurfelCount},
    {_"Redraw\tR",                      CommandRedraw,                  nil},
    {_"Save",                           CommandNone,                    menuSave},
    {"",                                CommandNone,                    nil},
    {_"View",                           CommandNone,                    menuView},
    {"S"_"urfel size\t1-9",             CommandNone,                    menuSurfelSize},
    {"Sha"_"ding",                      CommandNone,                    menuShading},
    {_"Blending\tB",                    CommandNone,                    menuBlending},
    {_"Depth buffer\tD",                CommandNone,                    menuZBuffer},
    {"",                                CommandNone,                    nil},
    {_"Axes\tA",                        CommandNone,                    menuAxis},
    {_"Help\tH",                        CommandNone,                    menuHelp},
    {_"Info\tI",                        CommandNone,                    menuInfo},
    {"",                                CommandNone,                    nil},
    {"S"_"ettings",                     CommandNone,                    menuSettings},
    {_"Quit\tQ",                        CommandNone,                    menuQuit},
    {nil,                               CommandNone,                    nil}
};



// }}}
// ifs_artefact1[][] {{{



float ifs_artefact1[][13]={
    {-0.101858f,-0.150842f, 0.308003f,-0.481334f, 0.166339f,-0.579352f, 0.044036f,-0.514029f, 0.164516f, 0.492382f, 0.146172f, 0.064375f, -0.225623f},
    {-0.022852f, 0.296328f, 0.814079f,-0.746566f,-0.254458f, 0.766551f,-0.297938f, 0.454955f,-0.947957f,-0.212907f, 0.060350f,-1.015431f,  1.000000f}
};



// }}}
// ifs_artefact2[][] {{{



float ifs_artefact2[][13]={
    {-0.071315f, 0.200444f,-0.210993f, 0.308965f,-0.258325f,-0.059292f, 0.008314f,-0.599626f,-0.017553f, 0.058221f, 0.734876f,-0.583363f, -0.267495f},
    {-0.198031f, 0.444311f,-0.710999f, 0.611886f, 0.584716f,-0.338408f,-0.473771f, 0.949758f,-0.500297f,-0.571381f,-0.272282f,-0.087467f,  0.809442f},
    { 0.328285f, 0.149096f,-0.492353f,-0.100800f, 0.207878f, 0.073338f, 0.864173f, 0.175989f, 0.339481f,-0.189086f,-0.053052f, 1.111021f,  0.989044f},
    {-0.501541f,-0.532668f,-0.115721f,-0.198741f, 0.118444f,-0.628877f, 0.263749f, 0.964651f,-0.406249f, 0.474261f, 0.219763f,-0.686276f,  1.000000f}
};



// }}}
// ifs_artefact3[][] {{{



float ifs_artefact3[][13]={
    {-0.149219f,-0.218931f,-0.076128f,-0.176103f, 0.119121f,-0.149684f, 0.491947f,-0.820411f, 0.134988f,-0.109922f,-0.518273f, 0.132760f, -0.073428f},
    { 0.887463f,-0.026903f,-0.067110f,-0.148618f, 0.130967f,-0.538636f, 0.174685f,-0.248019f,-0.193720f,-0.487402f,-0.189343f, 0.704726f,  0.400433f},
    {-0.894439f,-0.336771f, 0.024013f,-0.434810f, 0.081183f,-0.514214f,-0.139469f,-0.340855f, 0.365726f,-0.709481f, 0.089686f, 0.706895f,  0.891415f},
    { 0.075945f,-0.080308f,-0.207685f, 0.178539f,-0.315027f, 0.237405f,-0.052465f, 0.850269f,-0.120275f,-0.672524f, 0.006280f, 0.122273f,  1.000000f}
};



// }}}
// ifs_artefact4[][] {{{



float ifs_artefact4[][13]={
    { 0.364565f, 0.038670f, 0.008728f, 0.394244f, 0.338922f,-0.050364f, 0.005845f,-0.428889f,-0.596382f,-0.004983f, 0.008657f,-1.043205f, -0.010163f},
    {-0.243982f,-0.465263f,-0.424944f, 0.456958f, 0.076742f, 0.739098f,-0.369429f,-0.000908f, 0.412581f,-0.412611f,-0.182578f,-0.889257f,  0.032746f},
    { 0.099827f, 0.140258f,-0.312280f,-0.525080f, 0.185134f, 0.376114f, 0.122140f, 0.772410f, 0.578573f,-0.144551f, 0.014798f,-1.088071f,  0.129276f},
    { 0.059707f, 0.522051f,-0.160214f,-0.187567f, 0.516023f,-0.140507f,-0.005455f, 0.919340f,-0.078583f,-0.526006f,-0.157552f, 0.819254f,  0.207984f},
    { 0.250889f,-0.030707f, 0.890280f,-0.180622f, 0.586237f, 0.306830f,-0.171777f,-1.132464f, 0.513647f,-0.335193f,-0.238801f, 0.232543f,  0.563189f},
    {-0.769092f, 0.011206f, 0.444428f, 0.870842f, 0.082195f,-0.147360f, 0.177503f,-0.338234f,-0.565983f,-0.036628f,-0.578138f, 0.185934f,  0.587542f},
    {-0.009563f,-0.485699f,-0.086817f, 0.690251f, 0.006773f, 0.439292f,-0.104347f, 0.384353f, 0.016006f,-0.476090f,-0.007712f,-0.282015f,  0.873501f},
    {-0.144162f, 0.017065f, 0.848653f,-0.640743f, 0.331367f, 0.063816f, 0.066138f,-0.681175f, 0.316759f,-0.058992f, 0.317047f,-0.268826f,  1.000000f}
};



// }}}
// ifs_artefact5[][] {{{



float ifs_artefact5[][13]={
    {-0.014308f,-0.028272f, 0.916465f, 0.792812f,-0.010415f, 0.421076f,-0.042898f, 0.848069f,-0.033863f,-0.117565f,-0.374037f, 0.320556f, -0.333811f},
    {-0.382406f,-0.083106f, 0.146682f,-0.587406f,-0.294822f, 0.855944f,-0.007971f, 0.041135f,-0.789595f,-0.279347f,-0.068063f, 0.858230f,  0.511887f},
    {-0.467792f, 0.235933f,-0.073547f,-0.870659f,-0.156239f,-0.730864f, 0.192101f, 0.145745f, 0.010314f,-0.370541f,-0.425734f, 0.950115f,  1.000000f}
};



// }}}
// ifs_artefact6[][] {{{



float ifs_artefact6[][13]={
    { 0.088555f,-0.326833f,-0.211715f,-0.475499f, 0.056903f, 0.576230f, 0.288616f, 0.572544f,-0.006163f, 0.624204f,-0.377288f,-0.179581f,-0.441847f},
    {-0.242021f, 0.059674f, 0.805669f,-0.445266f,-0.704437f, 0.107637f,-0.279418f,-0.452460f,-0.096128f,-0.939020f, 0.019171f,-0.526309f, 1.000000f}
};



// }}}
// ifs_artefact7[][] {{{



float ifs_artefact7[][13]={
    { 0.118002f,-0.367313f,-0.082903f, 0.432253f,-0.391844f, 0.012465f,-0.390282f,-0.042140f,-0.519441f,-0.092846f, 0.275579f, 1.331511f,-0.264534f},
    {-0.192128f,-0.237729f, 0.644365f,-0.236597f,-0.622120f, 0.312954f, 0.225223f, 0.411871f,-0.689610f,-0.216094f,-0.382704f,-0.759115f, 1.000000f}
};



// }}}
// ifs_tower[][] {{{



float ifs_tower[][13]={
    {-0.972522f, 0.035970f, 0.055638f, 0.712389f,-0.057478f,-0.836075f,-0.384403f,-0.326122f,-0.035977f, 0.363412f,-0.889874f, 0.681205f,-0.966287f},
    { 0.245092f,-0.498526f,-0.160138f,-0.375638f, 0.473636f, 0.395872f,-0.091942f,-0.649507f, 0.352847f,-0.185108f, 0.234650f, 0.442588f, 0.200000f}
};



// }}}
// ifs_fern[][] {{{



float ifs_fern[][13]={
    { 0.000000f, 0.000000f, 0.000000f, 0.000000f, 0.180000f, 0.000000f, 0.000000f, 0.000000f, 0.000000f, 0.000000f, 0.000000f, 0.000000f, 0.010000f},
    { 0.850000f, 0.000000f, 0.000000f, 0.000000f, 0.850000f, 0.100000f, 0.000000f,-0.100000f, 0.850000f, 0.000000f, 1.600000f, 0.000000f, 0.850000f},
    { 0.200000f,-0.200000f, 0.000000f, 0.200000f, 0.200000f, 0.000000f, 0.000000f, 0.000000f, 0.300000f, 0.000000f, 0.800000f, 0.000000f, 0.070000f},
    {-0.200000f, 0.200000f, 0.000000f, 0.200000f, 0.200000f, 0.000000f, 0.000000f, 0.000000f, 0.300000f, 0.000000f, 0.800000f, 0.000000f, 0.070000f},
};



// }}}
// ifs_bush[][] {{{



float ifs_bush[][13]={
    {-0.373749f, 0.184692f, 0.105947f,-0.832341f,-0.453663f,-0.152631f, 0.124736f, 0.460184f, 0.197566f,-0.001087f, 0.486855f, 0.378884f,-0.020051f},
    { 0.166209f,-0.133945f,-0.080310f, 0.495707f,-0.797325f,-0.134969f,-0.012847f,-0.015179f, 0.145659f,-0.585965f, 0.021317f, 0.128416f, 0.161809f},
    {-0.648603f, 0.270537f, 0.003552f, 0.794061f,-0.293407f,-0.643705f,-0.003235f,-0.441188f, 0.077220f,-0.173481f, 0.017543f,-0.928678f, 0.506607f},
    { 0.292940f, 0.142934f,-0.216388f, 0.393835f,-0.063308f,-0.879776f,-0.043157f,-0.004582f,-0.916890f, 0.106412f,-0.066155f,-0.670893f, 1.000000f}
};



// }}}
// ifs_wing[][] {{{



float ifs_wing[][13]={
    {-0.863301f, 0.015541f, 0.106781f,-0.233617f, 0.098683f, 0.547759f, 0.401727f,-0.492123f,-0.098135f, 0.414103f,-0.535395f, 0.254419f, -0.496811f},
    {-0.510493f, 0.370321f,-0.285759f, 0.295526f,-0.107999f,-0.794018f,-0.174678f, 0.809436f, 0.719463f, 0.143569f,-0.228981f,-0.054059f,  1.000000f}
};



// }}}
// ifs_leaf[][] {{{



float ifs_leaf[][13]={
    {-0.492737f,-0.010404f, 0.180206f, 0.351519f,-0.530563f, 0.570329f,-0.108801f, 1.057364f,-0.380220f,-0.782360f,-0.081711f,-0.458607f, -0.217750f},
    {-0.856946f,-0.299423f, 0.035138f, 0.708119f,-0.322467f, 0.841126f,-0.041265f, 0.669464f, 0.073766f, 0.198542f, 0.227810f, 0.531253f,  1.000000f}
};



// }}}
// ifs_flash[][] {{{



float ifs_flash[][13]={
    {-0.009669f, 0.031249f, 0.794159f,-0.190141f, 0.035952f, 0.572048f, 0.123748f, 0.045626f, 0.026162f,-0.774558f, 0.123434f,-0.211259f, -0.228614f},
    { 0.067100f, 0.338221f,-0.383701f, 0.483533f,-0.052567f, 0.242058f,-0.618321f,-0.859729f, 0.015527f,-0.642140f,-0.435178f,-0.834466f,  1.000000f}
};



// }}}
// ifs_pyramid[][] {{{



float ifs_pyramid[][13]={
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 1.000000f, 0.000000f,  0.200000f},
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.500000f, 0.000000f, 0.500000f,  0.200000f},
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f,-0.500000f, 0.000000f, 0.500000f,  0.200000f},
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f,-0.500000f, 0.000000f,-0.500000f,  0.200000f},
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.500000f, 0.000000f,-0.500000f,  0.200000f}
};



// }}}
// ifs_tetrahedron1[][] {{{



float ifs_tetrahedron1[][13]={
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 1.000000f,  0.250000f},
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.870000f,-0.500000f,  0.250000f},
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f,-0.870000f,-0.500000f,-0.500000f,  0.250000f},
    { 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.000000f, 0.000000f, 0.000000f, 0.500000f, 0.870000f,-0.500000f,-0.500000f,  0.250000f},
};



// }}}
// ifs_tetrahedron2[][] {{{



float ifs_tetrahedron2[][13]={
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 1.000000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.870000f,-0.500000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f,-0.870000f,-0.500000f,-0.500000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.870000f,-0.500000f,-0.500000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f,  0.200000f},
};



// }}}
// ifs_hexahedron[][] {{{



float ifs_hexahedron[][13]={
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.900000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.870000f,-0.500000f, 0.000000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f,-0.870000f,-0.500000f, 0.000000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 1.000000f, 0.000000f,  0.200000f},
    { 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f, 0.000000f, 0.440000f, 0.000000f, 0.000000f,-0.900000f,  0.200000f},
};



// }}}
// ifs_cube[][] {{{



float ifs_cube[][13]={
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 1.000000f, 1.000000f, 1.000000f,  0.120000f},
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 1.000000f, 1.000000f,-1.000000f,  0.130000f},
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 1.000000f,-1.000000f, 1.000000f,  0.120000f},
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 1.000000f,-1.000000f,-1.000000f,  0.130000f},
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f,-1.000000f, 1.000000f, 1.000000f,  0.120000f},
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f,-1.000000f, 1.000000f,-1.000000f,  0.130000f},
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f,-1.000000f,-1.000000f, 1.000000f,  0.120000f},
    { 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f, 0.000000f, 0.000000f, 0.000000f, 0.350000f,-1.000000f,-1.000000f,-1.000000f,  0.130000f},
};



// }}}
// ifs_octahedron[][] {{{



float ifs_octahedron[][13]={
    { 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f, 1.000000f,  0.170000f},
    { 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 1.000000f, 0.000000f, 0.000000f,  0.160000f},
    { 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 1.000000f, 0.000000f,  0.170000f},
    { 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f,-1.000000f, 0.000000f, 0.000000f,  0.170000f},
    { 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f,-1.000000f, 0.000000f,  0.160000f},
    { 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f, 0.000000f, 0.400000f, 0.000000f, 0.000000f,-1.000000f,  0.170000f},
};



// }}}
// ifs_duodecahedron[][] {{{



float ifs_duodecahedron[][13]={
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.960000f,  0.090000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.850000f, 0.430000f,  0.080000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.810000f, 0.260000f, 0.430000f,  0.080000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f,-0.810000f, 0.260000f, 0.430000f,  0.090000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.500000f,-0.690000f, 0.430000f,  0.080000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f,-0.500000f,-0.690000f, 0.430000f,  0.080000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.500000f, 0.690000f,-0.430000f,  0.090000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f,-0.500000f, 0.690000f,-0.430000f,  0.080000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.810000f,-0.260000f,-0.430000f,  0.080000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f,-0.810000f,-0.260000f,-0.430000f,  0.090000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f,-0.850000f,-0.430000f,  0.080000f},
    { 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f, 0.000000f, 0.280000f, 0.000000f, 0.000000f,-0.960000f,  0.080000f},
};



// }}}
// surfelInit() {{{



int surfelInit(void)
{
    return false;
}



// }}}
// surfelListSaveP() {{{



int surfelListSaveP(int surfelList, const char * fileName)
{
    FILE *fout;
    int  i;
    SurfelList *sl=(SurfelList *)surfelList;
    fout=fopen(fileName, "wt");
    if (fout) {
        fprintf(fout, "pf\n"); // p-position n-normal c-color s-size o-object
        fprintf(fout, "%d\n", sl->itemsCount);
        for (i=0; i<sl->itemsCount; i++)
            fprintf(fout, "%6.3f %6.3f %6.3f\n",
                    sl->items.itemsF[i].position.x,
                    sl->items.itemsF[i].position.y,
                    sl->items.itemsF[i].position.z);
        fclose(fout);
        return true;
    }
    else {
        return false;
    }
}



// }}}
// surfelListSavePS() {{{



int surfelListSavePS(int surfelList, const char * fileName)
{
    FILE *fout;
    int  i;
    SurfelList *sl=(SurfelList *)surfelList;
    fout=fopen(fileName, "wt");
    if (fout) {
        fprintf(fout, "pfsb\n"); // p-position n-normal c-color s-size o-object
        fprintf(fout, "%d\n", sl->itemsCount);
        for (i=0; i<sl->itemsCount; i++)
            fprintf(fout, "%6.3f %6.3f %6.3f %d\n",
                    sl->items.itemsF[i].position.x,
                    sl->items.itemsF[i].position.y,
                    sl->items.itemsF[i].position.z,
                    (int)sl->items.itemsF[i].size);
        fclose(fout);
        return true;
    }
    else {
        return false;
    }
}



// }}}
// surfelListInit() {{{



int surfelListInit(int type)
{
    SurfelList *surfelList;
    switch (type) {
        case SURFEL_LIST_FLOAT:
            surfelList=(SurfelList *)malloc(sizeof(SurfelList));
            if (!surfelList) return 0;
            surfelList->type=SURFEL_LIST_FLOAT;
            surfelList->itemsCount=0;
            surfelList->currentItem=-1;
            surfelList->items.itemsF=nil;
            return (int)surfelList;
        default:
            return false;
    }
}



// }}}
// surfelListDone() {{{



int surfelListDone(int surfelList)
{
    SurfelList *sl=(SurfelList *)surfelList;
    free(sl);
    return true;
}



// }}}
// surfelListDestroy() {{{



int surfelListDestroy(int surfelList)
{
    SurfelList *sl=(SurfelList *)surfelList;
    switch (sl->type) {
        case SURFEL_LIST_FLOAT:
            if (sl->items.itemsF) {
                free(sl->items.itemsF);
                return true;
            }
            else {
                return false;
            }
        default:
            return false;
    }
}



// }}}
// surfelListAlloc() {{{



int surfelListAlloc(int surfelList, int itemCount)
{
    SurfelList *sl=(SurfelList *)surfelList;
    switch (sl->type) {
        case SURFEL_LIST_FLOAT:
            sl->items.itemsF=(SurfelF*)malloc(sizeof(SurfelF)*itemCount);
            sl->itemsCount=itemCount;
            if (sl->items.itemsF) return true;
            else return false;
        default:
            return false;
    }
}



// }}}
// surfelListSetSurfelF() {{{



int surfelListSetSurfelF(int surfelList, SurfelF *surfel)
{
    SurfelList *sl=(SurfelList *)surfelList;
    switch (sl->type) {
        case SURFEL_LIST_FLOAT:
            memcpy(&(sl->items.itemsF[sl->currentItem]), surfel, sizeof(SurfelF));
            return true;
        default:
            return false;
    }
}



// }}}
// surfelListGetSurfelF() {{{



int surfelListGetSurfelF(int surfelList, SurfelF *surfel)
{
    SurfelList *sl=(SurfelList *)surfelList;
    switch (sl->type) {
        case SURFEL_LIST_FLOAT:
            memcpy(surfel, &(sl->items.itemsF[sl->currentItem]), sizeof(SurfelF));
            return true;
        default:
            return false;
    }
}



// }}}
// surfelListFirst() {{{



int surfelListFirst(int surfelList)
{
    SurfelList *sl=(SurfelList *)surfelList;
    if (sl->itemsCount) sl->currentItem=0;
    return true;
}



// }}}
// surfelListNext() {{{



int surfelListNext(int surfelList)
{
    SurfelList *sl=(SurfelList *)surfelList;
    sl->currentItem++;
    return true;
}



// }}}
// surfelListIsLast() {{{



int surfelListIsLast(int surfelList)
{
    SurfelList *sl=(SurfelList *)surfelList;
    return sl->currentItem==sl->itemsCount;
}



// }}}
// surfelGetCount() {{{



int surfelGetCount(int surfelList)
{
    SurfelList *sl=(SurfelList *)surfelList;
    return sl->itemsCount;
}



// }}}
// confInit() {{{



// ----------------------------------------------------------------------------
// This function initializes configuration module for this application.
// ----------------------------------------------------------------------------
void confInit(View *view, Scrollbar *scrollbar, Mouse *mouse, int *settings, int *activeItem)
{
    v_conf=view;
    s_conf=scrollbar;
    m_conf=mouse;
    set=settings;
    active=activeItem;
}



// }}}
// inButton() {{{



// ----------------------------------------------------------------------------
// This function returns "true", if mouse pointer is positioned over some
// button. It returns "false" otherwise.
// ----------------------------------------------------------------------------
int inButton(const ButtonStruct buttons[], const int i, const int x, const int y)
{
    return (x>buttons[i].xmin &&
            x<buttons[i].xmax &&
            (v_conf->windowHeight-y)>buttons[i].ymin &&
            (v_conf->windowHeight-y)<buttons[i].ymax);
}



// }}}
// inMainMenuButton() {{{



// ----------------------------------------------------------------------------
// This function returns "true", if mouse pointer is positioned over main menu
// button. It returns "false" otherwise.
// ----------------------------------------------------------------------------
int inMainMenuButton(int x, int y)
{
    return (x>=10 && x<=220 && y>=8 && y<=24);
}



// }}}
// inScrollbar() {{{



// ----------------------------------------------------------------------------
// This function returns "true", if mouse pointer is positioned over scrollbar.
// It returns "false" otherwise.
// ----------------------------------------------------------------------------
int inScrollbar(Scrollbar *s_conf, int x, int y)
{
    return (x>s_conf->xmin) && (x<s_conf->xmax) && (y>s_conf->ymin) && (y<s_conf->ymax);
}



// }}}
// setMenuForButton() {{{



// ----------------------------------------------------------------------------
// This function sets context menu for button under mouse pointer.
// ----------------------------------------------------------------------------
void setMenuForButton(const ButtonStruct buttons[], const int x, const int y)
{
    int i;
    int old=*active;
    *active=0;
    for (i=0; buttons[i].callback; i++) {           // check if mouse cursor is in some button
        if (*set==CommandSettingsSurfelsCount || i!=4) {
            if (inButton(buttons, i, x, y)) {
                glutSetMenu(buttons[i].menu);
                glutAttachMenu(GLUT_RIGHT_BUTTON);  // context menu under right mouse button
                *active=buttons[i].menu;
                break;
            }
        }
    }
    if (*active!=old) glutPostRedisplay();
}



// }}}
// setMenuForMainButton() {{{



// ----------------------------------------------------------------------------
// This function sets context menu for main menu button, but only when mouse
// pointer is positioned over this button.
// ----------------------------------------------------------------------------
void setMenuForMainButton(int x, int y)
{
    int old=*active;
    if (inMainMenuButton(x, y)) {
        glutSetMenu(mainMenu);
        glutAttachMenu(GLUT_LEFT_BUTTON);
        glutAttachMenu(GLUT_RIGHT_BUTTON);
        *active=mainMenu;
    }
    if (*active!=old) glutPostRedisplay();
}



// }}}
// processScrollbars() {{{



// ----------------------------------------------------------------------------
// This function processes all scrollbar messages.
// ----------------------------------------------------------------------------
void processScrollbars(int x, int y)
{
    if (*set==CommandSettingsSurfelsCount) {
        if (inScrollbar(s_conf, x, v_conf->windowHeight-y)) { // surfel count scrollbar
            updateScrollbar(s_conf, x, y);
            glutSetCursor(GLUT_CURSOR_WAIT);
            objectCreate(&o, o.type, s_conf->position);
            objectSizeMove(&o);
            glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
            glutPostRedisplay();
        }
    }
    else {
        if (x>=340 && x<=540) {                     // color scrollbars
            GLfloat r, g, b, a;
            int yy=v_conf->windowHeight-y;
            getCurrentColor(&r, &g, &b, &a);
            if (yy>=56 && yy<=62) {                 // red color component
                r=(x-340)/200.0f;
                setCurrentColor(r, g, b, a);
                glutPostRedisplay();
            }
            if (yy>=41 && yy<=47) {                 // green color component
                g=(x-340)/200.0f;
                setCurrentColor(r, g, b, a);
                glutPostRedisplay();
            }
            if (yy>=26 && yy<=32) {                 // blue color component
                b=(x-340)/200.0f;
                setCurrentColor(r, g, b, a);
                glutPostRedisplay();
            }
            if (yy>=11 && yy<=17) {                 // alpha color component
                a=(x-340)/200.0f;
                setCurrentColor(r, g, b, a);
                glutPostRedisplay();
            }
        }
    }
}



// }}}
// processRightMouseButton() {{{



// ----------------------------------------------------------------------------
// This function processes messages for right mouse button press/release.
// ----------------------------------------------------------------------------
#ifdef __BORLANDC__                                 // avoid compiler warnings
#pragma option -w-par
#endif
void processRightMouseButton(int state, int x, int y)
{
    if (state==GLUT_DOWN) {                         // mouse button press
        m_conf->status=2;
        m_conf->z1=y;
    }
    else {                                          // mouse button release
        m_conf->status=0;
        m_conf->zold=m_conf->znew;
    }
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



// }}}
// processLeftMouseButton() {{{



// ----------------------------------------------------------------------------
// This function processes messages for left mouse button press/release.
// ----------------------------------------------------------------------------
void processLeftMouseButton(const ButtonStruct buttons[], const int state, const int x, const int y)
{
    int doTransformation=true;
    int i;
    if (state==GLUT_DOWN) {
        if (!v_conf->info) {                             // rotate fractal object
            m_conf->status=1;
            m_conf->x1=x;
            m_conf->y1=y;
            glutPostRedisplay();
            return;
        }
        if (*set==CommandSettingsSurfelsCount) {    // change surfels count
            if (inScrollbar(s_conf, x, v_conf->windowHeight-y)) {
                updateScrollbar(s_conf, x, y);
                glutSetCursor(GLUT_CURSOR_WAIT);
                objectCreate(&o, o.type, s_conf->position);
                objectSizeMove(&o);
                glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
                doTransformation=false;
            }
            for (i=0; buttons[i].callback; i++) {   // check if mouse pointer
                if (inButton(buttons, i, x, y)) {   // is in some button
                    buttons[i].callback();
                    doTransformation=false;
                    break;
                }
            }
        }
        else {
            if (x>=340 && x<=540) {                 // color scrollbars
                GLfloat r, g, b, a;
                int yy=v_conf->windowHeight-y;
                getCurrentColor(&r, &g, &b, &a);
                if (yy>=56 && yy<=62) {             // red color component
                    r=(x-340)/200.0f;
                    setCurrentColor(r, g, b, a);
                    doTransformation=false;
                }
                if (yy>=41 && yy<=47) {             // green color component
                    g=(x-340)/200.0f;
                    setCurrentColor(r, g, b, a);
                    doTransformation=false;
                }
                if (yy>=26 && yy<=32) {             // blue color component
                    b=(x-340)/200.0f;
                    setCurrentColor(r, g, b, a);
                    doTransformation=false;
                }
                if (yy>=11 && yy<=17) {             // alpha color component
                    a=(x-340)/200.0f;
                    setCurrentColor(r, g, b, a);
                    doTransformation=false;
                }
            }
            for (i=0; buttons[i].callback; i++) {   // check if mouse pointer
                if (inButton(buttons, i, x, y) && i!=4) {// is in some button
                    buttons[i].callback();
                    doTransformation=false;
                    break;
                }
            }
        }
        if (doTransformation) {                     // if user wants to do some transformation
            if (glutGetModifiers() & GLUT_ACTIVE_CTRL) {
                m_conf->xtran1=x;
                m_conf->ytran1=y;
                m_conf->status=3;
            }
            else {
                m_conf->status=1;
                m_conf->x1=x;
                m_conf->y1=y;
            }
        }
    }
    else {                                          // GLUT_UP
        m_conf->status=0;
        m_conf->xold=m_conf->xnew;
        m_conf->yold=m_conf->ynew;
        m_conf->xtran2=m_conf->xtran0;
        m_conf->ytran2=m_conf->ytran0;
    }
}



// }}}
// getAxisColor() {{{



// ----------------------------------------------------------------------------
// This function returns current axis color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getAxisColor(void)
{
    return axisColor;
}



// }}}
// getHelpColor() {{{



// ----------------------------------------------------------------------------
// This function returns current help foreground color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getHelpColor(void)
{
    return helpColor;
}



// }}}
// getInfoColor() {{{



// ----------------------------------------------------------------------------
// This function returns current info foreground color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getInfoColor(void)
{
    return infoColor;
}



// }}}
// getModelColor() {{{



// ----------------------------------------------------------------------------
// This function returns current model color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getModelColor(void)
{
    return modelColor;
}



// }}}
// getScrollBarColor() {{{



// ----------------------------------------------------------------------------
// This function returns current scroll bar color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getScrollBarColor(void)
{
    return scrollBarColor;
}



// }}}
// getActiveItemColor() {{{



// ----------------------------------------------------------------------------
// This function returns current active (highlited) item color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getActiveItemColor(void)
{
    return activeItemColor;
}



// }}}
// getHelpBackground() {{{



// ----------------------------------------------------------------------------
// This function returns current help background color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getHelpBackground(void)
{
    return helpBackground;
}



// }}}
// getInfoBackground() {{{



// ----------------------------------------------------------------------------
// This function returns current info background color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getInfoBackground(void)
{
    return infoBackground;
}



// }}}
// getModelBackground() {{{



// ----------------------------------------------------------------------------
// This function returns current model background color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getModelBackground(void)
{
    return modelBackground;
}



// }}}
// getFogColor() {{{



// ----------------------------------------------------------------------------
// This function returns current fog color
// (pointer to four color components).
// ----------------------------------------------------------------------------
GLfloat *getFogColor(void)
{
    return fogColor;
}



// }}}
// getCurrentColor() {{{



// ----------------------------------------------------------------------------
// This function gets current color for some GUI item.
// ----------------------------------------------------------------------------
void getCurrentColor(GLfloat *r, GLfloat *g, GLfloat *b, GLfloat *a)
{
    #ifndef __BORLANDC__
    GLfloat *color=nil;
    #else
    GLfloat *color;
    #endif
    switch (*set) {
        case CommandSettingsModelForeground: color=modelColor;      break;
        case CommandSettingsModelBackground: color=modelBackground; break;
        case CommandSettingsFogColor:        color=fogColor;        break;
        case CommandSettingsAxesColor:       color=axisColor;       break;
        case CommandSettingsActiveItemColor: color=activeItemColor; break;
        case CommandSettingsHelpForeground:  color=helpColor;       break;
        case CommandSettingsHelpBackground:  color=helpBackground;  break;
        case CommandSettingsInfoForeground:  color=infoColor;       break;
        case CommandSettingsInfoBackground:  color=infoBackground;  break;
        case CommandSettingsScrollBarColor:  color=scrollBarColor;  break;
        default:                             color=modelColor;      break;
    }
    if (color) {
        *r=color[0];
        *g=color[1];
        *b=color[2];
        *a=color[3];
    }
}



// }}}
// setModelAlpha() {{{



// ----------------------------------------------------------------------------
// This function sets alpha color component for blending.
// ----------------------------------------------------------------------------
void setModelAlpha(GLfloat alpha)
{
    modelColor[3]=alpha;
}



// }}}
// setCurrentColor() {{{



// ----------------------------------------------------------------------------
// This function sets current color for some GUI item.
// ----------------------------------------------------------------------------
void setCurrentColor(GLfloat r, GLfloat g, GLfloat b, GLfloat a)
{
    GLfloat *color=nil;
    switch (*set) {
        case CommandSettingsModelForeground: color=modelColor;      break;
        case CommandSettingsModelBackground: color=modelBackground; break;
        case CommandSettingsFogColor:        color=fogColor;        break;
        case CommandSettingsAxesColor:       color=axisColor;       break;
        case CommandSettingsActiveItemColor: color=activeItemColor; break;
        case CommandSettingsHelpForeground:  color=helpColor;       break;
        case CommandSettingsHelpBackground:  color=helpBackground;  break;
        case CommandSettingsInfoForeground:  color=infoColor;       break;
        case CommandSettingsInfoBackground:  color=infoBackground;  break;
        case CommandSettingsScrollBarColor:  color=scrollBarColor;  break;
    }
    if (color) {
        color[0]=r;
        color[1]=g;
        color[2]=b;
        color[3]=a;
    }
}



// }}}
// readOneLine() {{{



// ----------------------------------------------------------------------------
// This function reads one line from config file.
// ----------------------------------------------------------------------------
void readOneLine(FILE *fin, GLfloat (*colorArray)[4])
{
    char str[1000];
    GLfloat r, g, b, a;                             // four color components
    if (fscanf(fin, "%s%f%f%f%f\n", str, &r, &g, &b, &a)==5) {
        (*colorArray)[0]=r;
        (*colorArray)[1]=g;
        (*colorArray)[2]=b;
        (*colorArray)[3]=a;
    }
}



// }}}
// settingsReset() {{{



// ----------------------------------------------------------------------------
// This function resets all color settings.
// ----------------------------------------------------------------------------
void settingsReset(void)
{
    const GLfloat c_axisColor[]=      {0.5f, 0.5f, 1.0f, 1.0f};
    const GLfloat c_helpColor[]=      {0.2f, 0.9f, 0.9f, 1.0f};
    const GLfloat c_infoColor[]=      {0.2f, 0.9f, 0.9f, 1.0f};
    const GLfloat c_modelColor[]=     {1.0f, 1.0f, 1.0f, 0.5f};
    const GLfloat c_scrollBarColor[]= {0.5f, 0.5f, 1.0f, 1.0f};
    const GLfloat c_activeItemColor[]={1.0f, 1.0f, 0.5f, 1.0f};
    const GLfloat c_helpBackground[]= {0.3f, 0.3f, 0.7f, 0.7f};
    const GLfloat c_infoBackground[]= {0.3f, 0.3f, 0.7f, 0.7f};
    const GLfloat c_modelBackground[]={0.0f, 0.0f, 0.0f, 1.0f};
    const GLfloat c_fogColor[]=       {0.1f, 0.1f, 0.1f, 0.0f};
    // set default colors
    memcpy(axisColor,       c_axisColor,       sizeof(c_axisColor));
    memcpy(helpColor,       c_helpColor,       sizeof(c_helpColor));
    memcpy(infoColor,       c_infoColor,       sizeof(c_infoColor));
    memcpy(modelColor,      c_modelColor,      sizeof(c_modelColor));
    memcpy(scrollBarColor,  c_scrollBarColor,  sizeof(c_scrollBarColor));
    memcpy(activeItemColor, c_activeItemColor, sizeof(c_activeItemColor));
    memcpy(helpBackground,  c_helpBackground,  sizeof(c_helpBackground));
    memcpy(infoBackground,  c_infoBackground,  sizeof(c_infoBackground));
    memcpy(modelBackground, c_modelBackground, sizeof(c_modelBackground));
    memcpy(fogColor,        c_fogColor,        sizeof(c_fogColor));
}



// }}}
// settingsLoad() {{{



// ----------------------------------------------------------------------------
// This function reads all color settings from config file.
// ----------------------------------------------------------------------------
void settingsLoad(void)
{
    FILE *fin;

    fin=fopen("surf_ifs.ini", "rt");                // try to open config file for reading
    if (fin) {
        readOneLine(fin, &axisColor);
        readOneLine(fin, &helpColor);
        readOneLine(fin, &infoColor);
        readOneLine(fin, &modelColor);
        readOneLine(fin, &scrollBarColor);
        readOneLine(fin, &activeItemColor);
        readOneLine(fin, &helpBackground);
        readOneLine(fin, &infoBackground);
        readOneLine(fin, &modelBackground);
        readOneLine(fin, &fogColor);
        fclose(fin);
    }
    else {
        settingsReset();                            // file could not be opened
    }
}



// }}}
// settingsSave() {{{



// ----------------------------------------------------------------------------
// This function writes color settings to config file.
// ----------------------------------------------------------------------------
void settingsSave(void)
{
    FILE *fout;
    fout=fopen("surf_ifs.ini", "wt");               // try to open config file for writing
    if (fout) {
        fprintf(fout, "AxisColor\t %5.3f %5.3f %5.3f %5.3f\n",
                axisColor[0], axisColor[1], axisColor[2], axisColor[3]);
        fprintf(fout, "HelpColor\t %5.3f %5.3f %5.3f %5.3f\n",
                helpColor[0], helpColor[1], helpColor[2], helpColor[3]);
        fprintf(fout, "InfoColor\t %5.3f %5.3f %5.3f %5.3f\n",
                infoColor[0], infoColor[1], infoColor[2], infoColor[3]);
        fprintf(fout, "ModelColor\t %5.3f %5.3f %5.3f %5.3f\n",
                modelColor[0], modelColor[1], modelColor[2], modelColor[3]);
        fprintf(fout, "ScrollBarColor\t %5.3f %5.3f %5.3f %5.3f\n",
                scrollBarColor[0], scrollBarColor[1], scrollBarColor[2], scrollBarColor[3]);
        fprintf(fout, "ActiveItemColor\t %5.3f %5.3f %5.3f %5.3f\n",
                activeItemColor[0], activeItemColor[1], activeItemColor[2], activeItemColor[3]);
        fprintf(fout, "HelpBackground\t %5.3f %5.3f %5.3f %5.3f\n",
                helpBackground[0], helpBackground[1], helpBackground[2], helpBackground[3]);
        fprintf(fout, "InfoBackground\t %5.3f %5.3f %5.3f %5.3f\n",
                infoBackground[0], infoBackground[1], infoBackground[2], infoBackground[3]);
        fprintf(fout, "ModelBackground\t %5.3f %5.3f %5.3f %5.3f\n",
                modelBackground[0], modelBackground[1], modelBackground[2], modelBackground[3]);
        fprintf(fout, "FogColor\t %5.3f %5.3f %5.3f %5.3f\n",
                fogColor[0], fogColor[1], fogColor[2], fogColor[3]);
        fclose(fout);
    }
}



// }}}
// arandom() {{{



// ----------------------------------------------------------------------------
// This function works as pseudo-random number generator.
// ----------------------------------------------------------------------------
float arandom(float max)
{
    return (float)rand()*max/RAND_MAX;
}



// }}}
// getMinMax() {{{



// ----------------------------------------------------------------------------
// This function returns minimums and maximums coordinates of surfel positions.
// ----------------------------------------------------------------------------
void getMinMax(int surfelList, float *minx, float *maxx,
                               float *miny, float *maxy,
                               float *minz, float *maxz)
{
    SurfelF surfel;
    *minx=*miny=*minz=1.0e9;
    *maxx=*maxy=*maxz=-1.0e9;
    surfelListFirst(surfelList);
    while (!surfelListIsLast(surfelList)) {
        surfelListGetSurfelF(surfelList, &surfel);
        *minx=MIN(*minx, surfel.position.x);
        *maxx=MAX(*maxx, surfel.position.x);
        *miny=MIN(*miny, surfel.position.y);
        *maxy=MAX(*maxy, surfel.position.y);
        *minz=MIN(*minz, surfel.position.z);
        *maxz=MAX(*maxz, surfel.position.z);
        surfelListNext(surfelList);
    }
}



// }}}
// getArray() {{{



// ----------------------------------------------------------------------------
// This function returns pointer to proper data of selected IFS system.
// ----------------------------------------------------------------------------
void getArray(int type, float (**p)[13])
{
    switch (type) {
        case CommandModelPyramid:       *p=ifs_pyramid;       break;
        case CommandModelTetrahedron1:  *p=ifs_tetrahedron1;  break;
        case CommandModelTetrahedron2:  *p=ifs_tetrahedron2;  break;
        case CommandModelHexahedron:    *p=ifs_hexahedron;    break;
        case CommandModelCube:          *p=ifs_cube;          break;
        case CommandModelOctahedron:    *p=ifs_octahedron;    break;
        case CommandModelDuodecahedron: *p=ifs_duodecahedron; break;
        case CommandModelFern:          *p=ifs_fern;          break;
        case CommandModelWing:          *p=ifs_wing;          break;
        case CommandModelLeaf:          *p=ifs_leaf;          break;
        case CommandModelBush:          *p=ifs_bush;          break;
        case CommandModelFlash:         *p=ifs_flash;         break;
        case CommandModelTower:         *p=ifs_tower;         break;
        case CommandModelArtefact1:     *p=ifs_artefact1;     break;
        case CommandModelArtefact2:     *p=ifs_artefact2;     break;
        case CommandModelArtefact3:     *p=ifs_artefact3;     break;
        case CommandModelArtefact4:     *p=ifs_artefact4;     break;
        case CommandModelArtefact5:     *p=ifs_artefact5;     break;
        case CommandModelArtefact6:     *p=ifs_artefact6;     break;
        case CommandModelArtefact7:     *p=ifs_artefact7;     break;
        default:                        *p=NULL;              break;
    }
}



// }}}
// centerSurfels() {{{



// ----------------------------------------------------------------------------
// This function centers whole set of surfels.
// ----------------------------------------------------------------------------
void centerSurfels(int surfelList, int midx, int midy, int midz)
{
    SurfelF surfel;
    surfelListFirst(surfelList);
    while (!surfelListIsLast(surfelList)) {         // center object around origin
        surfelListGetSurfelF(surfelList, &surfel);
        surfel.position.x+=ORIGIN_X-midx;
        surfel.position.y+=ORIGIN_Y-midy;
        surfel.position.z+=ORIGIN_Z-midz;
        surfelListSetSurfelF(surfelList, &surfel);
        surfelListNext(surfelList);
    }
}



// }}}
// scaleAndMoveSurfels() {{{



// ----------------------------------------------------------------------------
// This function scales and moves whole set of surfels to fit to an unit cube.
// ----------------------------------------------------------------------------
void scaleAndMoveSurfels(int surfelList, float scale)
{
    SurfelF surfel;
    surfelListFirst(surfelList);
    while (!surfelListIsLast(surfelList)) {         // scale object into unit cube
        surfelListGetSurfelF(surfelList, &surfel);
        surfel.position.x-=ORIGIN_X;
        surfel.position.y-=ORIGIN_Y;
        surfel.position.z-=ORIGIN_Z;
        surfel.position.x*=scale;
        surfel.position.y*=scale;
        surfel.position.z*=scale;
        surfel.position.x+=ORIGIN_X;
        surfel.position.y+=ORIGIN_Y;
        surfel.position.z+=ORIGIN_Z;
        surfelListSetSurfelF(surfelList, &surfel);
        surfelListNext(surfelList);
    }
}



// }}}
// objectInit() {{{



// ----------------------------------------------------------------------------
// This function initializes new surfel-based object.
// ----------------------------------------------------------------------------
void objectInit(Object *o)
{
    o->type=CommandModelFirst;
    o->colorR=1.0;                                  // set initial values
    o->colorG=1.0;                                  // for all color components
    o->colorB=1.0;
    o->blending=0;
    o->alpha=0.5f;
    o->surfelList=surfelListInit(SURFEL_LIST_FLOAT);
}



// }}}
// objectCreate() {{{



// ----------------------------------------------------------------------------
// This function creates new surfel-based object.
// ----------------------------------------------------------------------------
void objectCreate(Object *o, int type, int grid)
{
    int     subtype;
    int     pts=grid*grid;
    int     i, k;
    float   x,y,z,x1,y1,z1;
    float   pp, sum;
    SurfelF surfel;
    float   (*ifs)[13];

    o->type=type;
    o->size=grid;
    getArray(type, &ifs);
    if (!ifs) return;
    surfelListDestroy(o->surfelList);
    surfelListAlloc(o->surfelList, pts);

    if (ifs[0][12]<0) {                             // check object type
        subtype=1;
        ifs[0][12]=-ifs[0][12];
    }
    else {                                          // bad object type
        subtype=0;
    }

    x=y=z=0.0;
    i=0;
    surfelListFirst(o->surfelList);
    if (!subtype) {                                 // generate model as normal IFS system
        while (!surfelListIsLast(o->surfelList)) {
            pp=arandom(999.0)/1000.0;
            sum=0;
            for (k=0; sum<=pp; k++)
                sum+=ifs[k][12];
            k--;
            x1=ifs[k][0]*x+ifs[k][1]*y+ifs[k][2]*z+ifs[k][9];
            y1=ifs[k][3]*x+ifs[k][4]*y+ifs[k][5]*z+ifs[k][10];
            z1=ifs[k][6]*x+ifs[k][7]*y+ifs[k][8]*z+ifs[k][11];
            x=x1;y=y1;z=z1;
            if (i>=100) {                           // after starting iterations
                surfel.position.x=x*20.0;           // generate surfel
                surfel.position.y=y*20.0;
                surfel.position.z=z*20.0;
                surfel.size=1;
                surfelListSetSurfelF(o->surfelList, &surfel);
                surfelListNext(o->surfelList);
            }
            i++;
        }
    }
    else {                                          // generate model as IFS with alternating coordinates
        while (!surfelListIsLast(o->surfelList)) {
            pp=arandom(999.0)/1000.0;
            sum=0;
            for (k=0; sum<=pp; k++)
                sum+=ifs[k][12];
            k--;
            x1=ifs[k][0]*x+ifs[k][1]*y+ifs[k][2]*z+ifs[k][3];
            y1=ifs[k][4]*x+ifs[k][5]*y+ifs[k][6]*z+ifs[k][7];
            z1=ifs[k][8]*x+ifs[k][9]*y+ifs[k][10]*z+ifs[k][11];
            x=-x1;y=-y1;z=-z1;
            if (i>=100) {                           // after starting iterations
                surfel.position.x=x*20.0;           // generate surfel
                surfel.position.y=y*20.0;
                surfel.position.z=z*20.0;
                surfel.size=1;
                surfelListSetSurfelF(o->surfelList, &surfel);
                surfelListNext(o->surfelList);
            }
            i++;
        }
        ifs[0][12]=-ifs[0][12];
    }
}



// }}}
// objectSizeMove() {{{



// ----------------------------------------------------------------------------
// This function centers surfel-based object along origin.
// ----------------------------------------------------------------------------
void objectSizeMove(Object *o)
{
    float minx, miny, minz;
    float maxx, maxy, maxz;
    float midx, midy, midz;
    float scale;

    getMinMax(o->surfelList, &minx, &maxx, &miny, &maxy, &minz, &maxz);
    midx=(minx+maxx)/2.0;
    midy=(miny+maxy)/2.0;
    midz=(minz+maxz)/2.0;
    centerSurfels(o->surfelList, midx, midy, midz);
    scale=RANGE_X/(maxx-minx);
    scale=MIN(scale, RANGE_Y/(maxy-miny));
    scale=MIN(scale, RANGE_Z/(maxz-minz));
    scaleAndMoveSurfels(o->surfelList, scale);
}



// }}}
// objectSave() {{{



// ----------------------------------------------------------------------------
// This function saves surfel-based object to an external file.
// ----------------------------------------------------------------------------
void objectSave(Object *o)
{
    time_t timer;
    struct tm *t;
    char fileName[100];
    time(&timer);
    t=localtime(&timer);                            // get current date and time

    sprintf(fileName, "%04d%02d%02d-%02d%02d%02d.sfl", // prepare file name
            t->tm_year+1900, t->tm_mon+1, t->tm_mday,
            t->tm_hour, t->tm_min, t->tm_sec);
    surfelListSaveP(o->surfelList, fileName);       // write surfels to file
}



// }}}
// objectSaveSize() {{{



// ----------------------------------------------------------------------------
// This function saves surfel-based object to file, including surfel' sizes.
// ----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void objectSaveSize(Object *o, View *v)
{
    time_t timer;
    struct tm *t;
    char fileName[100];
    time(&timer);
    t=localtime(&timer);                            // get current date and time

    sprintf(fileName, "%04d%02d%02d-%02d%02d%02d.sfl", // prepare file name
            t->tm_year+1900, t->tm_mon+1, t->tm_mday,
            t->tm_hour, t->tm_min, t->tm_sec);
    surfelListSavePS(o->surfelList, fileName);      // write surfels to file
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



// }}}
// drawString() {{{



// ----------------------------------------------------------------------------
// This function draws string at world' specified co-ordinates
// ----------------------------------------------------------------------------
void drawString(char *string, int x, int y, int z)
{
    glRasterPos3i(x, y, z);
    while (*string)                                 // for all characters in string
        glutBitmapCharacter(FONT, *string++);       // draw each character
}



// }}}
// drawObjectNoShading() {{{



// ----------------------------------------------------------------------------
// This function draws the surfel object using no shading
// ----------------------------------------------------------------------------
void drawObjectNoShading(Object *o)
{
    SurfelF surfel;
    if (o->blending) {                              // if blending is enabled
        glEnable(GL_BLEND);                         // enable it
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    }
    glColor4fv(getModelColor());                    // constant object color
    glBegin(GL_POINTS);
    surfelListFirst(o->surfelList);                 // rewind to first surfel in object
    while (!surfelListIsLast(o->surfelList)) {      // for all surfels in object
        surfelListGetSurfelF(o->surfelList, &surfel);// get surfel
        glVertex3f(surfel.position.x, surfel.position.y, surfel.position.z);
        surfelListNext(o->surfelList);              // move to next surfel in list
    }
    glEnd();
    if (o->blending) {                              // if blending is enabled
        glDisable(GL_BLEND);                        // disable it (for GUI)
    }
}



// }}}
// drawObjectXShading() {{{



// ----------------------------------------------------------------------------
// This function draws the surfel object using shading along x-axis
// ----------------------------------------------------------------------------
void drawObjectXShading(Object *o)
{
    GLfloat weight;
    GLfloat *color;
    GLfloat *fog;
    SurfelF surfel;

    color=getModelColor();
    fog=getFogColor();
    if (o->blending) {                              // if blending is enabled
        glEnable(GL_BLEND);                         // enable it
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    }
    glBegin(GL_POINTS);
    surfelListFirst(o->surfelList);                 // rewind to first surfel in object
    while (!surfelListIsLast(o->surfelList)) {      // for all surfels in object
        surfelListGetSurfelF(o->surfelList, &surfel);
        weight=(float)surfel.position.x/RANGE_X+0.2;// calculate surfel color
        glColor4f(color[0]*weight+fog[0]*(1.0f-weight),
                  color[1]*weight+fog[1]*(1.0f-weight),
                  color[2]*weight+fog[2]*(1.0f-weight),
                  color[3]);                        // set color and draw surfel
        glVertex3f(surfel.position.x, surfel.position.y, surfel.position.z);
        surfelListNext(o->surfelList);              // goto next surfel in list
    }
    glEnd();
    if (o->blending) {                              // if blending is enabled
        glDisable(GL_BLEND);                        // disable it (for GUI)
    }
}



// }}}
// drawObjectYShading() {{{



// ----------------------------------------------------------------------------
// This function draws the surfel object using shading along y-axis
// ----------------------------------------------------------------------------
void drawObjectYShading(Object *o)
{
    GLfloat weight;
    GLfloat *color;
    GLfloat *fog;
    SurfelF surfel;

    color=getModelColor();
    fog=getFogColor();
    if (o->blending) {                              // if blending is enabled
        glEnable(GL_BLEND);                         // enable it
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    }
    glBegin(GL_POINTS);
    surfelListFirst(o->surfelList);                 // rewind to first surfel in object
    while (!surfelListIsLast(o->surfelList)) {      // for all surfels in object
        surfelListGetSurfelF(o->surfelList, &surfel);
        weight=(float)surfel.position.y/RANGE_Y+0.2;// calculate surfel color
        glColor4f(color[0]*weight+fog[0]*(1.0f-weight),
                  color[1]*weight+fog[1]*(1.0f-weight),
                  color[2]*weight+fog[2]*(1.0f-weight),
                  color[3]);                        // set color and draw surfel
        glVertex3f(surfel.position.x, surfel.position.y, surfel.position.z);
        surfelListNext(o->surfelList);              // goto next surfel in list
    }
    glEnd();
    if (o->blending) {                              // if blending is enabled
        glDisable(GL_BLEND);                        // disable it (for GUI)
    }
}



// }}}
// drawObjectZShading() {{{



// ----------------------------------------------------------------------------
// This function draws the surfel object using shading along z-axis
// ----------------------------------------------------------------------------
void drawObjectZShading(Object *o)
{
    GLfloat weight;
    GLfloat *color;
    GLfloat *fog;
    SurfelF surfel;

    color=getModelColor();
    fog=getFogColor();
    if (o->blending) {                              // if blending is enabled
        glEnable(GL_BLEND);                         // enable it
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    }
    glBegin(GL_POINTS);
    surfelListFirst(o->surfelList);                 // rewind to first surfel in object
    while (!surfelListIsLast(o->surfelList)) {      // for all surfels in object
        surfelListGetSurfelF(o->surfelList, &surfel);
        weight=(float)surfel.position.z/RANGE_Z+0.2;// calculate surfel color
        glColor4f(color[0]*weight+fog[0]*(1.0f-weight),
                  color[1]*weight+fog[1]*(1.0f-weight),
                  color[2]*weight+fog[2]*(1.0f-weight),
                  color[3]);                        // set color and draw surfel
        glVertex3f(surfel.position.x, surfel.position.y, surfel.position.z);
        surfelListNext(o->surfelList);              // goto next surfel in list
    }
    glEnd();
    if (o->blending) {                              // if blending is enabled
        glDisable(GL_BLEND);                        // disable it (for GUI)
    }
}



// }}}
// drawObjectFogShading() {{{



// ----------------------------------------------------------------------------
// This function draws the surfel object using fog
// ----------------------------------------------------------------------------
void drawObjectFogShading(Object *o)
{
    SurfelF surfel;
    GLfloat *fogColor=getFogColor();
    glEnable(GL_FOG);                               // set fog properties
    glFogi(GL_FOG_MODE, GL_LINEAR);
    glFogfv(GL_FOG_COLOR, fogColor);
    glFogf(GL_FOG_DENSITY, 0.1f);
    glHint(GL_FOG_HINT, GL_DONT_CARE);
    glFogf(GL_FOG_START, 220.0);                    // near and far planes
    glFogf(GL_FOG_END, 320.0);                      // fog increases inbetween these planes
    if (o->blending) {                              // if blending is enabled
        glEnable(GL_BLEND);                         // enable it
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    }
    glColor4fv(getModelColor());
    glBegin(GL_POINTS);
    surfelListFirst(o->surfelList);
    while (!surfelListIsLast(o->surfelList)) {      // for all surfels in object
        surfelListGetSurfelF(o->surfelList, &surfel);
        glVertex3f(surfel.position.x, surfel.position.y, surfel.position.z);
        surfelListNext(o->surfelList);              // goto next surfel in list
    }
    glEnd();
    glDisable(GL_FOG);
    if (o->blending) {                              // if blending is enabled
        glDisable(GL_BLEND);                        // disable it (for GUI)
    }
}



// }}}
// drawObject() {{{



// ----------------------------------------------------------------------------
// This function draws the surfel object
// ----------------------------------------------------------------------------
void drawObject(Object *o, View *v)
{
    if (v->zBuffer)
        glEnable(GL_DEPTH_TEST);
    switch (v->shading) {
        case CommandShadingNone: drawObjectNoShading(o);  break;
        case CommandShadingX:    drawObjectXShading(o);   break;
        case CommandShadingY:    drawObjectYShading(o);   break;
        case CommandShadingZ:    drawObjectZShading(o);   break;
        case CommandShadingFog:  drawObjectFogShading(o); break;
        default:                                          break;
    }
    if (v->zBuffer)
        glDisable(GL_DEPTH_TEST);
}



// }}}
// drawAxis() {{{



// ----------------------------------------------------------------------------
// This function draws axes
// ----------------------------------------------------------------------------
void drawAxis(void)
{
    glEnable(GL_BLEND);
    glColor4fv(getAxisColor());
    drawString("origin", MINX+1, MINY+1, MINZ+1);   // text labels
    drawString("xmax", MAXX+1, MINY+1, MINZ+1);
    drawString("ymax", MINX+1, MAXY+1, MINZ+1);
    drawString("zmax", MINX+1, MINY+1, MAXZ+1);

    glBegin(GL_LINE_STRIP);                         // bottom side
        glVertex3f(MINX, MINY, MINZ);
        glVertex3f(MAXX, MINY, MINZ);
        glVertex3f(MAXX, MAXY, MINZ);
        glVertex3f(MINX, MAXY, MINZ);
        glVertex3f(MINX, MINY, MINZ);
    glEnd();
    glBegin(GL_LINE_STRIP);                         // top side
        glVertex3f(MINX, MINY, MAXZ);
        glVertex3f(MAXX, MINY, MAXZ);
        glVertex3f(MAXX, MAXY, MAXZ);
        glVertex3f(MINX, MAXY, MAXZ);
        glVertex3f(MINX, MINY, MAXZ);
    glEnd();
    glBegin(GL_LINES);                              // left, right, front and back side
        glVertex3f(MINX, MINY, MINZ);
        glVertex3f(MINX, MINY, MAXZ);
        glVertex3f(MAXX, MINY, MINZ);
        glVertex3f(MAXX, MINY, MAXZ);
        glVertex3f(MAXX, MAXY, MINZ);
        glVertex3f(MAXX, MAXY, MAXZ);
        glVertex3f(MINX, MAXY, MINZ);
        glVertex3f(MINX, MAXY, MAXZ);
        glVertex3f(MINX, MINY, MINZ);
        glVertex3f(MINX, MINY, MAXZ);
    glEnd();
    glDisable(GL_BLEND);
}



// }}}
// drawScrollbar() {{{



// ----------------------------------------------------------------------------
// This function draws scrollbar
// ----------------------------------------------------------------------------
void drawScrollbar(View *v, Scrollbar *s)
{
    if (v->windowHeight<120) return;                // ensure proper window size
    if (v->windowWidth<s->xmax+2) return;

    glEnable(GL_BLEND);
    glColor4fv(getInfoColor());                     // display border
    glBegin(GL_LINE_LOOP);
        glVertex2i(s->xmin, s->ymin);
        glVertex2i(s->xmin, s->ymax);
        glVertex2i(s->xmax, s->ymax);
        glVertex2i(s->xmax, s->ymin);
    glEnd();

    glColor4fv(getScrollBarColor());                // display slider
    glBegin(GL_QUADS);
        glVertex2i(s->xmin+1, s->ymin+2);
        glVertex2i(s->xmin+1, s->ymax-1);
        glVertex2i(s->xmin+s->position, s->ymax-1);
        glVertex2i(s->xmin+s->position, s->ymin+2);
    glEnd();
    glDisable(GL_BLEND);
}



// }}}
// drawInfo() {{{



// ----------------------------------------------------------------------------
// This function displays informations at window' bottom area
// ----------------------------------------------------------------------------
void drawInfo(Object *o, View *v, char *objectType, int activeItem)
{
    char *enableDisableStr[]={"disabled", "enabled"};
    char str[100];

    if (v->windowHeight<120) return;                // ensure proper window size
    if (v->windowWidth<189) return;

    glEnable(GL_BLEND);                             // draw background
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glColor4fv(getInfoBackground());
    glRecti(0, 0, v->windowWidth, 90);

    if (activeItem==modelMenu)                      // highlight menu if necessary
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    sprintf(str, "Object type:  %s", objectType);
    drawString(str, 10, 71, 0);
    if (activeItem==surfelMenu)                     // highlight menu if necessary
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    sprintf(str, "Surfels size: %d", v->surfelsSize);
    drawString(str, 10, 55, 0);
    if (activeItem==shadingMenu)
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    sprintf(str, "Shading:      %s", shadingString[v->shading-CommandShadingNone]);
    drawString(str, 10, 40, 0);
    if (activeItem==zBufferMenu)
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    sprintf(str, "Depth buffer: %s", enableDisableStr[v->zBuffer]);
    drawString(str, 10, 25, 0);
    if (activeItem==blendingMenu)
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    sprintf(str, "Blending:     %s", enableDisableStr[o->blending]);
    drawString(str, 10, 10, 0);
    glDisable(GL_BLEND);
}



// }}}
// drawSurfelsInfo() {{{



// ----------------------------------------------------------------------------
// This function displays surfels informations at window' bottom area
// ----------------------------------------------------------------------------
void drawSurfelsInfo(Object *o, View *v, Mouse *m, int activeItem)
{
    char str[100];

    if (v->windowHeight<120) return;                // ensure proper window size
    if (v->windowWidth<390) return;

    glEnable(GL_BLEND);
    if (activeItem==settingsMenu)                   // highlight menu item
        glColor4fv(getActiveItemColor());           // if necessary
    else
        glColor4fv(getInfoColor());
    drawString("Model settings", 230, 73, 0);
    if (activeItem==surfelCountMenu)
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    sprintf(str, "Surfels count: %d", surfelGetCount(o->surfelList));
    drawString(str, 230, 40, 0);
    glColor4fv(getInfoColor());
    sprintf(str, "Rotation:     %d %d", m->ynew, m->xnew);
    drawString(str, 230, 25, 0);
    sprintf(str, "Translation:  %d", m->znew);
    drawString(str, 230, 10, 0);
    if (v->windowWidth<556) return;                 // ensure proper window size
    if (activeItem==surfelCountMenu)
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    sprintf(str, "sqrt(surfels): %d", o->size);
    drawString(str, 410, 40, 0);
    glDisable(GL_BLEND);
}



// }}}
// drawColorScrollbars() {{{



// ----------------------------------------------------------------------------
// This function displays RGBA scrollbars
// ----------------------------------------------------------------------------
void drawColorScrollbars(View *v, int settings, int activeItem)
{
    char *prompt[]={
        "Model foreground",
        "Model background",
        "Fog color",
        "Axes color",
        "Active item",
        "Help foreground",
        "Help background",
        "Info foreground",
        "Info background",
        "Scroll bar color"
    };
    char str[100];
    GLfloat r, g, b, a;

    if (v->windowHeight<120) return;                // ensure proper window size
    if (v->windowWidth<350) return;

    glEnable(GL_BLEND);
    glColor4fv(getInfoColor());
    if (activeItem==settingsMenu)
        glColor4fv(getActiveItemColor());
    drawString(prompt[settings], 230, 73, 0);       // draw title
    getCurrentColor(&r, &g, &b, &a);

    glColor3f(0.9f, 0.5f, 0.5f);                    // red scrollbar stuff
    sprintf(str, "Red:   %3.0f%%", r*100.0f);
    drawString(str, 230, 55, 0);
    if (v->windowWidth>542) {
        glBegin(GL_QUADS);
            glVertex2i(340, 58);
            glVertex2f(340+r*200.0f, 58.0f);
            glVertex2f(340+r*200.0f, 61.0f);
            glVertex2i(340, 61);
        glEnd();
        glColor3f(0.8f, 0.4f, 0.4f);
        glBegin(GL_LINE_LOOP);
            glVertex2i(340, 56);
            glVertex2i(540, 56);
            glVertex2i(540, 62);
            glVertex2i(340, 62);
        glEnd();
    }

    glColor3f(0.5f, 0.9f, 0.5f);                    // green scrollbar stuff
    sprintf(str, "Green: %3.0f%%", g*100.0f);
    drawString(str, 230, 40, 0);
    if (v->windowWidth>542) {
        glBegin(GL_QUADS);
            glVertex2i(340, 43);
            glVertex2f(340+g*200.0f, 43.0f);
            glVertex2f(340+g*200.0f, 46.0f);
            glVertex2i(340, 46);
        glEnd();
        glColor3f(0.4f, 0.8f, 0.4f);
        glBegin(GL_LINE_LOOP);
            glVertex2i(340, 41);
            glVertex2i(540, 41);
            glVertex2i(540, 47);
            glVertex2i(340, 47);
        glEnd();
    }

    glColor3f(0.5f, 0.5f, 0.9f);                    // blue scrollbar stuff
    sprintf(str, "Blue:  %3.0f%%", b*100.0f);
    drawString(str, 230, 25, 0);
    if (v->windowWidth>542) {
        glBegin(GL_QUADS);
            glVertex2i(340, 28);
            glVertex2f(340+b*200.0f, 28.0f);
            glVertex2f(340+b*200.0f, 31.0f);
            glVertex2i(340, 31);
        glEnd();
        glColor3f(0.4f, 0.4f, 0.8f);
        glBegin(GL_LINE_LOOP);
            glVertex2i(340, 26);
            glVertex2i(540, 26);
            glVertex2i(540, 32);
            glVertex2i(340, 32);
        glEnd();
    }

    glColor3f(0.7f, 0.7f, 0.7f);                    // alpha scrollbar stuff
    sprintf(str, "Alpha: %3.0f%%", a*100.0f);
    drawString(str, 230, 10, 0);
    if (v->windowWidth>542) {
        glBegin(GL_QUADS);
            glVertex2i(340, 13);
            glVertex2f(340+a*200.0f, 13.0f);
            glVertex2f(340+a*200.0f, 16.0f);
            glVertex2i(340, 16);
        glEnd();
        glColor3f(0.6f, 0.6f, 0.6f);
        glBegin(GL_LINE_LOOP);
            glVertex2i(340, 11);
            glVertex2i(540, 11);
            glVertex2i(540, 17);
            glVertex2i(340, 17);
        glEnd();
    }
    glDisable(GL_BLEND);
}



// }}}
// drawHelp() {{{



// ----------------------------------------------------------------------------
// This function displays help at window' top area
// ----------------------------------------------------------------------------
void drawHelp(View *v)
{
    char *helpStr[]={
        "F-full screen",
        "W-window",
        "R-redraw",
        "A-axes on/off",
        "I-info on/off",
        "H-help on/off",
        "D-depth buffer",
        "B-blending",
        "N-none shading",
        "X-ax.x shading",
        "Y-ax.y shading",
        "Z-ax.z shading",
        "O-fog shading",
        "P-save pos.",
        "S-save size",
        "Q-quit",
        "ESC-quit",
        NULL
    };
    int i;

    if (v->windowHeight<396) return;                // ensure proper window size
    if (v->windowWidth<140) return;

    glEnable(GL_BLEND);                             // draw background
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glColor4fv(getHelpBackground());
    glRecti(0, v->info ? 90:0, 140, v->windowHeight-30);

    glColor4fv(getHelpColor());                     // get text color from configuration
    for (i=0; helpStr[i]; i++) {                    // print all help-lines
        drawString(helpStr[i], 10, v->windowHeight-50-i*15, 0);
    }
    glDisable(GL_BLEND);
}



// }}}
// drawMainMenu() {{{



// ----------------------------------------------------------------------------
// This function displays area and text for main menu rectangle
// ----------------------------------------------------------------------------
void drawMainMenu(View *v, int activeItem)
{
    if (v->windowWidth<230) return;                 // ensure proper window size

    glEnable(GL_BLEND);                             // draw background
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glColor4fv(getInfoBackground());
    glRecti(0, v->windowHeight, 230, v->windowHeight-30);

    if (activeItem==mainMenu)                       // highlight menu when necessary
        glColor4fv(getActiveItemColor());
    else
        glColor4fv(getInfoColor());
    drawString("Click here for main menu", 20, v->windowHeight-20, 0);
    glColor4fv(getAxisColor());
    glBegin(GL_LINE_LOOP);
        glVertex2i( 10, v->windowHeight-24);
        glVertex2i(220, v->windowHeight-24);
        glVertex2i(220, v->windowHeight-8);
        glVertex2i( 10, v->windowHeight-8);
    glEnd();
    glDisable(GL_BLEND);
}



// }}}
// buttonsInit() {{{



// ----------------------------------------------------------------------------
// This function initializes Button structure
// ----------------------------------------------------------------------------
void buttonsInit(void)
{
    buttons[0].menu=modelMenu;                      // fill in all fields
    buttons[1].menu=surfelMenu;
    buttons[2].menu=shadingMenu;
    buttons[3].menu=zBufferMenu;
    buttons[4].menu=surfelCountMenu;
    buttons[5].menu=blendingMenu;
    buttons[6].menu=settingsMenu;
}



// }}}
// buttonObjectClick() {{{



// ----------------------------------------------------------------------------
// This callback function is called when user click on [Object type] button
// ----------------------------------------------------------------------------
void buttonObjectClick(void)
{
    o.type++;
    if (o.type>CommandModelLast)                    // check type counter
        o.type=CommandModelFirst;
    if (o.type<CommandModelFirst)
        o.type=CommandModelLast;
    glutSetCursor(GLUT_CURSOR_WAIT);
    objectCreate(&o, o.type, s.position);           // create and align new object
    objectSizeMove(&o);
    glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
}



// }}}
// buttonSurfelsSizeClick() {{{



// ----------------------------------------------------------------------------
// This callback function is called when user click on [Surfel size] button
// ----------------------------------------------------------------------------
void buttonSurfelsSizeClick(void)
{
    v.surfelsSize++;                                // increase surfel size
    v.surfelsSize%=10;                              // and check ranges
    if (!v.surfelsSize)
        v.surfelsSize=1;
}



// }}}
// buttonShadingClick() {{{



// ----------------------------------------------------------------------------
// This callback function is called when user click on [Shading] button
// ----------------------------------------------------------------------------
void buttonShadingClick(void)
{
    v.shading++;
    if (v.shading>CommandShadingFog)
        v.shading=CommandShadingNone;
}



// }}}
// buttonZBufferClick() {{{



// ----------------------------------------------------------------------------
// This callback function is called when user click on [Z-buffer] button
// ----------------------------------------------------------------------------
void buttonZBufferClick(void)
{
    v.zBuffer=!v.zBuffer;                           // toggle z-buffer flag
}



// }}}
// buttonBlendingClick() {{{



// ----------------------------------------------------------------------------
// This callback function is called when user click on [Blending] button
// ----------------------------------------------------------------------------
void buttonBlendingClick(void)
{
    o.blending=!o.blending;                         // toggle blending flag
}



// }}}
// buttonSurfelsCountClick() {{{



// ----------------------------------------------------------------------------
// This callback function is called when user click on Surfels Count button
// ----------------------------------------------------------------------------
void buttonSurfelsCountClick(void)
{
    int sizes[]={10, 20, 25, 50, 100, 150, 200, 250};
    int size=s.position;
    int i;
    for (i=0; i<8; i++) {                           // find proper size
        if (size<sizes[i]) {
            s.position=sizes[i];
            break;
        }
        s.position=sizes[0];
    }
    glutSetCursor(GLUT_CURSOR_WAIT);
    objectCreate(&o, o.type, s.position);           // create and align new object
    objectSizeMove(&o);
    glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
    glutPostRedisplay();
}



// }}}
// buttonSettingsClick() {{{



// ----------------------------------------------------------------------------
// This callback function is called when user click on Settings button
// ----------------------------------------------------------------------------
void buttonSettingsClick(void)
{
    settings++;
    if (settings>CommandSettingsScrollBarColor)
        settings=CommandSettingsSurfelsCount;
    glutPostRedisplay();
}



// }}}
// updateScrollbar() {{{



// ----------------------------------------------------------------------------
// This function updates scrollbar
// ----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void updateScrollbar(Scrollbar *s, int x, int y)
{
    s->position=x-s->xmin+1;
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



// }}}
// viewInitMouse() {{{



// ----------------------------------------------------------------------------
// This function initializes mouse structure
// ----------------------------------------------------------------------------
void viewInitMouse(Mouse *m)
{
    m->xnew=m->ynew=m->znew=0;                      // initial mouse cursor
    m->xold=m->yold=m->zold=0;                      // position
    m->x1=m->y1=m->z1=0;                            // and derived values
    m->xtran0=m->ytran0=0;
    m->xtran1=m->ytran1=0;
    m->xtran2=m->ytran2=0;
}



// }}}
// viewInit() {{{



// ----------------------------------------------------------------------------
// This function initializes view structure
// ----------------------------------------------------------------------------
void viewInit(View *v)
{
    v->fov=45.0;
    v->nearPlane=0.1f;
    v->farPlane=1000.0;
    v->windowWidth=WINDOW_WIDTH;
    v->windowHeight=WINDOW_HEIGHT;
    v->surfelsSize=2.0;
    v->help=true;
    v->info=true;
    v->axis=true;
    v->shading=CommandShadingNone;
    v->zBuffer=false;
}



// }}}
// viewLeft() {{{



// ----------------------------------------------------------------------------
// This function changes camera to left-view
// ----------------------------------------------------------------------------
void viewLeft(Mouse *m)
{
    m->xnew=m->xold=m->x1=90;
    m->ynew=m->yold=m->y1=0;
    m->znew=m->zold=m->z1=0;
    glutPostRedisplay();
}



// }}}
// viewRight() {{{



// ----------------------------------------------------------------------------
// This function changes camera to right-view
// ----------------------------------------------------------------------------
void viewRight(Mouse *m)
{
    m->xnew=m->xold=m->x1=-90;
    m->ynew=m->yold=m->y1=0;
    m->znew=m->zold=m->z1=0;
    glutPostRedisplay();
}



// }}}
// viewTop() {{{



// ----------------------------------------------------------------------------
// This function changes camera to top-view
// ----------------------------------------------------------------------------
void viewTop(Mouse *m)
{
    m->xnew=m->xold=m->x1=0;
    m->ynew=m->yold=m->y1=90;
    m->znew=m->zold=m->z1=0;
    glutPostRedisplay();
}



// }}}
// viewBottom() {{{



// ----------------------------------------------------------------------------
// This function changes camera to bottom-view
// ----------------------------------------------------------------------------
void viewBottom(Mouse *m)
{
    m->xnew=m->xold=m->x1=0;
    m->ynew=m->yold=m->y1=-90;
    m->znew=m->zold=m->z1=0;
    glutPostRedisplay();
}



// }}}
// viewOriginal() {{{



// ----------------------------------------------------------------------------
// This function changes camera to original view
// ----------------------------------------------------------------------------
void viewOriginal(Mouse *m)
{
    m->xnew=m->xold=m->x1=0;
    m->ynew=m->yold=m->y1=0;
    m->znew=m->zold=m->z1=0;
    glutPostRedisplay();
}



// }}}
// viewRotateByMouse() {{{



// ----------------------------------------------------------------------------
// This function performs object rotation
// ----------------------------------------------------------------------------
void viewRotateByMouse(Mouse *m, int x, int y)
{
    m->xnew=m->xold+x-m->x1;
    m->ynew=m->yold+y-m->y1;
    glutPostRedisplay();
}



// }}}
// viewTranslateByMouse() {{{



// ----------------------------------------------------------------------------
// This function performs translation to back/forward
// ----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void viewTranslateByMouse(Mouse *m, int x, int y)
{
    m->znew=m->zold+y-m->z1;
    glutPostRedisplay();
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



// }}}
// onInit() {{{



// ----------------------------------------------------------------------------
// Callback function called before main loop begins
// ----------------------------------------------------------------------------
void onInit(void)
{
    viewInit(&v);                                   // initialize view and mouse
    viewInitMouse(&m);
    objectInit(&o);
    glutSetCursor(GLUT_CURSOR_WAIT);
    objectCreate(&o, o.type, 100);                  // create and align new object
    objectSizeMove(&o);
    glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
    glClearColor(0.0, 0.0, 0.0, 0.0);               // set OpenGL state
    glClearDepth(1.0f);
    glDepthFunc(GL_LESS);
    glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST);
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL);
    glEnable(GL_POINT_SMOOTH);
    settingsReset();
}



// }}}
// onResize() {{{



// ----------------------------------------------------------------------------
// Callback function called when system needs to resize window
// ----------------------------------------------------------------------------
void onResize(int w, int h)
{
    glViewport(0, 0, w, h);
    v.windowWidth=w;
    v.windowHeight=h;
}



// }}}
// onDisplay() {{{



// ----------------------------------------------------------------------------
// Callback function called when system needs repaint window
// ----------------------------------------------------------------------------
void onDisplay(void)
{
    GLfloat *rgba;
    rgba=getModelBackground();
    glClearColor(rgba[0], rgba[1], rgba[2], rgba[3]);
    if (v.zBuffer)                                  // clear Z-buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    else
        glClear(GL_COLOR_BUFFER_BIT);
    glPointSize(v.surfelsSize);

    glMatrixMode(GL_PROJECTION);                    // set projection matrix
    glLoadIdentity();
    gluPerspective(v.fov,(double)v.windowWidth/(double)v.windowHeight, v.nearPlane, v.farPlane);

    glMatrixMode(GL_MODELVIEW);                     // set modelview matrix
    glLoadIdentity();
    glViewport(m.xtran0, -m.ytran0, v.windowWidth, v.windowHeight);

    glTranslatef(v.help ? 15.0f:0.0f, v.info ? 15.0f:0.0f, -250.0f); // rotate and
    glTranslatef(0.0f,0.0f,m.znew);                                  // translate model
    glRotatef(m.ynew+rotX, 1.0, 0.0, 0.0);
    glRotatef(m.xnew+rotY, 0.0, 1.0, 0.0);
    glTranslatef(-(MINX+MAXX)/2.0, -(MINY+MAXY)/2.0, -(MINZ+MAXZ)/2.0);
    if (v.axis) drawAxis();
    drawObject(&o, &v);

    glViewport(0, 0, v.windowWidth, v.windowHeight);
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0, v.windowWidth, 0, v.windowHeight, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    o.size=s.position;
    drawMainMenu(&v, activeItem);
    if (v.info) {
        drawInfo(&o, &v, modelString[o.type-CommandModelFirst], activeItem);
        if (settings==CommandSettingsSurfelsCount) {
            drawSurfelsInfo(&o, &v, &m, activeItem);
            drawScrollbar(&v, &s);
        }
        else
            drawColorScrollbars(&v, settings-CommandSettingsSurfelsCount-1, activeItem);
    }
    if (v.help) drawHelp(&v);
    glFlush();
    glutSwapBuffers();
}



// }}}
// onKeyboard() {{{



// ----------------------------------------------------------------------------
// Callback function called when user presses some ASCII key
// ----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void onKeyboard(unsigned char key, int x, int y)
{
    if (key>='A' && key<='Z')                       // change letter' case
        key+='a'-'A';
    
    if (key>='1' && key<='9') {                     // set surfel size
        v.surfelsSize=key-'0';
        glutPostRedisplay();
        return;
    }

    switch (key) {
        case 27:    exit(0);                                                 break;
        case 'q':   exit(0);                                                 break;
        case 'f':   glutFullScreen();                                        break;
        case 'w':   glutReshapeWindow(620, 460); glutPositionWindow(20, 20); break;
        case 's':   objectSaveSize(&o, &v);                                  break;
        case 'p':   objectSave(&o);                                          break;
        case 'r':   glutSetCursor(GLUT_CURSOR_WAIT);
                    objectCreate(&o, o.type, s.position);
                    objectSizeMove(&o);
                    glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
                    glutPostRedisplay();                                     break;
        case 'h':   v.help=!v.help;                glutPostRedisplay();      break;
        case 'i':   v.info=!v.info;                glutPostRedisplay();      break;
        case 'a':   v.axis=!v.axis;                glutPostRedisplay();      break;
        case 'n':   v.shading=CommandShadingNone;  glutPostRedisplay();      break;
        case 'x':   v.shading=CommandShadingX;     glutPostRedisplay();      break;
        case 'y':   v.shading=CommandShadingY;     glutPostRedisplay();      break;
        case 'z':   v.shading=CommandShadingZ;     glutPostRedisplay();      break;
        case 'o':   v.shading=CommandShadingFog;   glutPostRedisplay();      break;
        case 'd':   v.zBuffer=!v.zBuffer;          glutPostRedisplay();      break;
        case 'b':   o.blending=!o.blending;        glutPostRedisplay();      break;
        case 'c':   buttonSurfelsCountClick();                               break;
        // CTRL+letter
        case 'M'-64:rotXd=rotYd=0.0f;                                        break;
        case 'R'-64:settingsReset();               glutPostRedisplay();      break; // reset settings
        case 'L'-64:settingsLoad();                glutPostRedisplay();      break; // load settings
        case 'S'-64:settingsSave();                glutPostRedisplay();      break; // save settings
        // non-alphabet keys
        case '.':
        case '>':   buttonObjectClick();                                     break;
        case ',':
        case '<':   o.type-=2; buttonObjectClick();                          break;
        default:                                                             break;
    }
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



// }}}
// onSpecialKeyboard() {{{



// ----------------------------------------------------------------------------
// Callback function called when user presses some non-ASCII key
// ----------------------------------------------------------------------------
#ifdef __BORLANDC__
#pragma option -w-par
#endif
void onSpecialKeyboard(int key, int x, int y)
{
    switch (key) {
        case GLUT_KEY_F1:        setModelAlpha(0.1f); glutPostRedisplay();   break;
        case GLUT_KEY_F2:        setModelAlpha(0.2f); glutPostRedisplay();   break;
        case GLUT_KEY_F3:        setModelAlpha(0.3f); glutPostRedisplay();   break;
        case GLUT_KEY_F4:        setModelAlpha(0.4f); glutPostRedisplay();   break;
        case GLUT_KEY_F5:        setModelAlpha(0.5f); glutPostRedisplay();   break;
        case GLUT_KEY_F6:        setModelAlpha(0.6f); glutPostRedisplay();   break;
        case GLUT_KEY_F7:        setModelAlpha(0.7f); glutPostRedisplay();   break;
        case GLUT_KEY_F8:        setModelAlpha(0.8f); glutPostRedisplay();   break;
        case GLUT_KEY_F9:        setModelAlpha(0.9f); glutPostRedisplay();   break;
        case GLUT_KEY_F10:       setModelAlpha(1.0f); glutPostRedisplay();   break;
        case GLUT_KEY_HOME:      viewLeft(&m);                               break;
        case GLUT_KEY_END:       viewRight(&m);                              break;
        case GLUT_KEY_PAGE_UP:   viewTop(&m);                                break;
        case GLUT_KEY_PAGE_DOWN: viewBottom(&m);                             break;
        case GLUT_KEY_INSERT:    viewOriginal(&m);                           break;
        case GLUT_KEY_LEFT:      rotXd-=0.5f;                                break;
        case GLUT_KEY_RIGHT:     rotXd+=0.5f;                                break;
        case GLUT_KEY_UP:        rotYd-=0.5f;                                break;
        case GLUT_KEY_DOWN:      rotYd+=0.5f;                                break;
        default:                                                             break;
    }
}
#ifdef __BORLANDC__
#pragma option -w+par
#endif



// }}}
// onMouseButton() {{{



// ----------------------------------------------------------------------------
// Callback function called on mouse click
// ----------------------------------------------------------------------------
void onMouseButton(int button, int state, int x, int y)
{
    if (button==GLUT_LEFT_BUTTON) {                 // if left mouse button is pressed or released
        processLeftMouseButton(buttons, state, x, y);
        glutPostRedisplay();
    }
    if (button==GLUT_RIGHT_BUTTON) {                // if right mouse button is pressed or released
        processRightMouseButton(state, x, y);
        glutPostRedisplay();
    }
}



// }}}
// onMouseMotion() {{{



// ----------------------------------------------------------------------------
// Callback function called when user moves mouse pointer with button pressed
// ----------------------------------------------------------------------------
void onMouseMotion(int x, int y)
{
    switch (m.status) {
        case 1: viewRotateByMouse(&m, x, y); break; // rotate object
        case 2: viewTranslateByMouse(&m, x, y); break; // translate object
        case 3:                                     // translate camera
                m.xtran0=m.xtran2+x-m.xtran1;
                m.ytran0=m.ytran2+y-m.ytran1;
                glutPostRedisplay();
                break;
        default:
            processScrollbars(x, y);
            break;
    }
}



// }}}
// onPassiveMotion() {{{



// ----------------------------------------------------------------------------
// Callback function called when user moves mouse pointer without button pressed
// ----------------------------------------------------------------------------
void onPassiveMotion(int x, int y)
{
    glutDetachMenu(GLUT_LEFT_BUTTON);
    glutDetachMenu(GLUT_RIGHT_BUTTON);
    setMenuForButton(buttons, x, y);
    setMenuForMainButton(x, y);
}



// }}}
// onTimer() {{{



// ----------------------------------------------------------------------------
// Callback function triggered in a specified number of milliseconds
// ----------------------------------------------------------------------------
void onTimer(int value)
{
    rotX+=rotXd;                                    // update rotation angles
    rotY+=rotYd;
    if (fabs(rotXd)>0.1f || fabs(rotYd)>0.1f)
        glutPostRedisplay();
    glutTimerFunc(20, onTimer, value);
}



// }}}
// onMenu() {{{



// ----------------------------------------------------------------------------
// Callback function called when user selects command from main menu
// ----------------------------------------------------------------------------
void onMenu(int command)
{
    if (command>=CommandModelFirst && command<=CommandModelLast) {
        o.type=command;
        glutSetCursor(GLUT_CURSOR_WAIT);
        objectCreate(&o, o.type, s.position);
        objectSizeMove(&o);
        glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
        glutPostRedisplay();
        return;
    }
    if (command>=CommandSurfelCount100 && command<=CommandSurfelCount62500) {
        int sizes[]={10, 20, 25, 50, 100, 150, 200, 250};
        s.position=sizes[command-CommandSurfelCount100];
        glutSetCursor(GLUT_CURSOR_WAIT);
        objectCreate(&o, o.type, s.position);
        objectSizeMove(&o);
        glutSetCursor(GLUT_CURSOR_LEFT_ARROW);
        glutPostRedisplay();
        return;
    }
    if (command>=CommandSurfelSize1 && command<=CommandSurfelSize9) {
        v.surfelsSize=command-CommandSurfelSize1+1;
        glutPostRedisplay();
        return;
    }
    if (command>=CommandBlending01 && command<=CommandBlending10) {
        setModelAlpha((command-CommandBlending01)/10.0f+0.1f);
        glutPostRedisplay();
    }
    switch (command) {
        case CommandSavePositions:          objectSave(&o);                         break;
        case CommandSavePositionsSize:      objectSaveSize(&o, &v);                 break;
        case CommandRedraw:                 glutPostRedisplay();                    break;
        case CommandViewLeft:               viewLeft(&m);                           break;
        case CommandViewRight:              viewRight(&m);                          break;
        case CommandViewTop:                viewTop(&m);                            break;
        case CommandViewBottom:             viewBottom(&m);                         break;
        case CommandViewOriginal:           viewOriginal(&m);                       break;
        case CommandShadingNone:
        case CommandShadingX:
        case CommandShadingY:
        case CommandShadingZ:
        case CommandShadingFog:             v.shading=command; glutPostRedisplay(); break;
        case CommandZBufferEnable:          v.zBuffer=true;    glutPostRedisplay(); break;
        case CommandZBufferDisable:         v.zBuffer=false;   glutPostRedisplay(); break;
        case CommandBlendingEnable:         o.blending=true;   glutPostRedisplay(); break;
        case CommandBlendingDisable:        o.blending=false;  glutPostRedisplay(); break;
        case CommandShowHelp:               v.help=true;       glutPostRedisplay(); break;
        case CommandHideHelp:               v.help=false;      glutPostRedisplay(); break;
        case CommandShowInfo:               v.info=true;       glutPostRedisplay(); break;
        case CommandHideInfo:               v.info=false;      glutPostRedisplay(); break;
        case CommandShowAxis:               v.axis=true;       glutPostRedisplay(); break;
        case CommandHideAxis:               v.axis=false;      glutPostRedisplay(); break;
        case CommandSettingsReset:          settingsReset();   glutPostRedisplay(); break;
        case CommandSettingsLoad:           settingsLoad();    glutPostRedisplay(); break;
        case CommandSettingsSave:           settingsSave();    glutPostRedisplay(); break;
        case CommandSettingsSurfelsCount:
        case CommandSettingsModelForeground:
        case CommandSettingsModelBackground:
        case CommandSettingsFogColor:
        case CommandSettingsAxesColor:
        case CommandSettingsActiveItemColor:
        case CommandSettingsHelpForeground:
        case CommandSettingsHelpBackground:
        case CommandSettingsInfoForeground:
        case CommandSettingsInfoBackground:
        case CommandSettingsScrollBarColor:
                                             settings=command; glutPostRedisplay(); break;
        case CommandQuitYes:                 exit(0);                               break;
        case CommandQuitNo:                                                         break;
        default:                                                                    break;
    }
}



// }}}
// createMainWindow() {{{



// ----------------------------------------------------------------------------
// This function creates main window
// ----------------------------------------------------------------------------
void createMainWindow(void)
{
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT);// set window properties
    glutInitWindowPosition(WINDOW_LEFT, WINDOW_TOP);
    glutCreateWindow(WINDOW_TITLE);
    glutDisplayFunc(onDisplay);                     // register all callback functions
    glutReshapeFunc(onResize);
    glutKeyboardFunc(onKeyboard);
    glutSpecialFunc(onSpecialKeyboard);
    glutMouseFunc(onMouseButton);
    glutMotionFunc(onMouseMotion);
    glutPassiveMotionFunc(onPassiveMotion);
    glutTimerFunc(20, onTimer, 0x1234);
}



// }}}
// createMenu() {{{



// ----------------------------------------------------------------------------
// This function creates main menu and submenus
// ----------------------------------------------------------------------------
void createMenu(void)
{
    modelMenu=gpeCreateMenu(menuModel, onMenu);
    surfelMenu=gpeCreateMenu(menuSurfelSize, onMenu);
    shadingMenu=gpeCreateMenu(menuShading, onMenu);
    zBufferMenu=gpeCreateMenu(menuZBuffer, onMenu);
    surfelCountMenu=gpeCreateMenu(menuSurfelCount, onMenu);
    blendingMenu=gpeCreateMenu(menuBlending, onMenu);
    settingsMenu=gpeCreateMenu(menuSettings, onMenu);
    mainMenu=gpeCreateMenu(menuMain, onMenu);
}



// }}}
// gpeCreateMenuFromData() {{{



// ----------------------------------------------------------------------------
// This function creates menu from given data structure
// ----------------------------------------------------------------------------
int gpeCreateMenuFromData(GpeMenu *menu, void (*f)(int command))
{
    int i=0;
    int menuID;

    menuID=glutCreateMenu(f);
    glutSetMenu(menuID);
    while (menu[i].caption!=NULL) {
        if (menu[i].subMenu) {
            int subMenu=gpeCreateMenuFromData(menu[i].subMenu, f);
            glutSetMenu(menuID);
            glutAddSubMenu(menu[i].caption, subMenu);
        }
        else {
            glutAddMenuEntry(menu[i].caption, menu[i].id);
        }
        i++;
    }
    return menuID;
}



// }}}
// gpeCreateMenu() {{{



// ----------------------------------------------------------------------------
// This function creates context menu
// ----------------------------------------------------------------------------
int gpeCreateMenu(GpeMenu *menu, void (*f)(int command))
{
    int result=gpeCreateMenuFromData(menu, f);
    return result;
}



// }}}
// main() {{{



// ----------------------------------------------------------------------------
// Main function
// ----------------------------------------------------------------------------
int main(int argc, char *argv[])
{
    glutInit(&argc, argv);                          // initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH);
    createMainWindow();                             // create main window
    createMenu();                                   // create main menu and all submenus
    buttonsInit();                                  // initialize buttons
    confInit(&v, &s, &m, &settings, &activeItem);   // initialize configuration module
    onInit();                                       // initialize OpenGL
    glutMainLoop();                                 // enter main loop
    return 0;                                       // return error code
}



// }}}



// ----------------------------------------------------------------------------
// finito
// ----------------------------------------------------------------------------

// vim:expandtab:foldenable:foldmethod=marker:foldclose=:foldmarker={{{,}}}
//
