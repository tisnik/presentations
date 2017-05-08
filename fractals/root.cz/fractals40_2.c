//-----------------------------------------------------------------------------
// Fraktaly v pocitacove grafice
// Autor: Pavel Tisnovsky
//
// Program urceny pro konverzi trojrozmerneho modelu systemu iterovanych funkci
// ze souboru ve formatu SFL do zdrojoveho textu urceneho pro program POV-Ray.
//
// Pouziti programu:
// fractals40_2 soubor.sfl soubor.pov
//
// kde:
// fractals40_2 je jmeno spustitelneho souboru ziskaneho prekladem tohoto
//              zdrojoveho textu
// soubor.sfl   je jmeno souboru obsahujiciho popis 3D modelu systemu
//              iterovanych funkci
// soubor.pov   je jmeno souboru urceneho pro program POV-Ray, ktery ma byt
//              vytvoren
//-----------------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 80

typedef enum {
    file_type_unknown,
    file_type_position,
    file_type_position_size,
} file_type_enum;

typedef struct {
    float x;
    float y;
    float z;
    float size;
} item;

FILE    *fin;
FILE    *fout;
int     item_no=0;
item   *items=NULL;
file_type_enum file_type=file_type_unknown;



// ----------------------------------------------------------------------------
// kontrola argumentu zadanych uzivatelem
// ----------------------------------------------------------------------------
void check_arguments(int argc)
{
    if (argc<=2) {
        puts("Neni zadano jmeno vstupniho a/nebo vystupniho souboru!\nPouziti: ifs2pov soubor.sfl soubor.pov");
        exit(1);
    }
}



// ----------------------------------------------------------------------------
// pokus o otevreni vstupniho souboru
// ----------------------------------------------------------------------------
FILE * open_input_file(const char *fin_name)
{
    FILE *f;
    if (!(f=fopen(fin_name, "r"))) {
        printf("Nelze otevrit soubor %s\n", fin_name);
        exit(1);
    }
    return f;
}



// ----------------------------------------------------------------------------
// nacteni hlavicky souboru
// ----------------------------------------------------------------------------
file_type_enum read_header_type(FILE *fin)
{
    char input[MAX_LINE_LENGTH];
    if (!fgets(input, MAX_LINE_LENGTH, fin)) {
        puts("Nelze precist hlavicku souboru");
        fclose(fin);
        exit(1);
    }
    if (!strcmp(input, "pf\n")) {
        puts("Typ souboru: pozice bodu");
        return file_type_position;
    }
    if (!strcmp(input, "pfsb\n")) {
        puts("Typ souboru: pozice bodu a velikost");
        return file_type_position_size;
    }
    if (file_type==file_type_unknown) {
        puts("Neznamy typ souboru");
        fclose(fin);
        exit(1);
    }
    return file_type_unknown;
}



// ----------------------------------------------------------------------------
// nacteni poctu prvku v souboru
// ----------------------------------------------------------------------------
int read_header_items(FILE *fin)
{
    char input[MAX_LINE_LENGTH];
    int i;
    if (!fgets(input, MAX_LINE_LENGTH, fin)) {
        puts("Nelze precist hlavicku souboru");
        fclose(fin);
        exit(1);
    }
    i=atoi(input);
    printf("Pocet prvku: %d\n", i);
    if (i<0 || i>100000) {
        puts("Nespravny pocet prvku");
        fclose(fin);
        exit(1);
    }
    return i;
}



// ----------------------------------------------------------------------------
// alokace pameti pro vsechny prvky
// ----------------------------------------------------------------------------
void alloc_memory(int item_no)
{
    items=(item*)malloc(item_no*sizeof(item));
    if (items==NULL) {
        puts("Chybna alokace pameti");
        fclose(fin);
        exit(1);
    }
}



// ----------------------------------------------------------------------------
// nacteni prvku ze souboru
// ----------------------------------------------------------------------------
void load_items(int item_no)
{
    int  i;
    char input[MAX_LINE_LENGTH];
    float x, y, z;
    printf("Nacitani prvku ze souboru: ");
    for (i=0; i<item_no; i++) {
        if (!fgets(input, MAX_LINE_LENGTH, fin)) {
            puts("Nelze precist data ze souboru");
            fclose(fin);
            exit(1);
        }
        sscanf(input, "%f %f %f", &x, &y, &z);
        items[i].x=x;
        items[i].y=y;
        items[i].z=z;
    }
    puts("OK");
}



// ----------------------------------------------------------------------------
// zapis hlavicky POV souboru s nastavenim kamery, svetel, textur a "podlahy"
// ----------------------------------------------------------------------------
void save_pov_header(const char *fout_name)
{
    if (!(fout=fopen(fout_name, "w"))) {
        puts("Nelze otevrit vystupni soubor pro zapis");
        fclose(fin);
        exit(1);

    }
    fputs("\n"\
        "camera {\n"\
        "        location  <125, 150, 200>\n"\
        "        look_at   <0, -10, 0>\n"\
        "}\n"\
        "\n"\
        "object { light_source { <300, 100, 350>  color rgb <1.0, 1.0, 1.0> } }\n"\
        "object { light_source { < 10, 200, -100> color rgb <1.0, 1.0, 1.0> } }\n"\
        "\n"\
        "#declare PVTXTEXT =\n"\
        "texture {\n"\
        "    pigment {\n"\
        "        color rgbf <0.000, 0.500, 1.000, 0.000>\n"\
        "        turbulence <0.520, 0.600, 0.360>\n"\
        "    }\n"\
        "    normal {\n"\
        "        ripples    1.000\n"\
        "        octaves    8.400\n"\
        "        frequency  4.000\n"\
        "    }\n"\
        "    finish {\n"\
        "        phong 0.900\n"\
        "        reflection 0.0\n"\
        "    }\n"\
        "    scale 0.5\n"\
        "}\n"\
        "\n"\
        "#declare OBJTEXT=\n"\
        "texture {\n"\
        "    pigment {\n"\
        "        color rgb <1.0, 0.7, 0.7>\n"\
        "    }\n"\
        "    finish {\n"\
        "        diffuse 1.0\n"\
        "        ambient 0.5\n"\
        "    }\n"\
        "}\n"\
        "\n"\
        "plane { y, -60\n"\
        "    texture {PVTXTEXT\n"\
        "        scale 300\n"\
        "    }\n"\
        "}\n"\
        "", fout);
}



// ----------------------------------------------------------------------------
// zapis informaci o bodech do sceny
// ----------------------------------------------------------------------------
void save_pov_data(void)
{
    int i;
    for (i=0; i<item_no; i++)
        fprintf(fout, "sphere { < %f, %f, %f>, 1 texture { OBJTEXT }}\n", items[i].x, items[i].y, items[i].z);
    fclose(fout);
}



// ----------------------------------------------------------------------------
// funkce zavolana po startu aplikace
// ----------------------------------------------------------------------------
int main(int argc, char *argv[])
{
    check_arguments(argc);
    fin=open_input_file(argv[1]);
    file_type=read_header_type(fin);
    item_no=read_header_items(fin);
    alloc_memory(item_no);
    load_items(item_no);
    save_pov_header(argv[2]);
    save_pov_data();

    fclose(fin);
    return 0;
}



// ----------------------------------------------------------------------------
// finito
// ----------------------------------------------------------------------------

