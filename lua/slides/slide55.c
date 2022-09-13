/*
----------------------------------------------------
Interpret jazyka Lua vestavěný do C-čkových programů
----------------------------------------------------
*/
#include <stdio.h>
#include <stdlib.h>

/* Zakladni a doplnkove funkce interpretu jazyka Lua */
#include <lualib.h>
#include <lauxlib.h>

/* Hlavni funkce konzolove aplikace */
int main(int argc, char **argv)
{
    int result;
    if (argc != 2) {
        puts("Pouziti: lua62 script.lua");
        return 1;
    }

    /* vytisteni hlavicky */
    puts(LUA_RELEASE);
    puts(LUA_COPYRIGHT);
    puts(LUA_AUTHORS);
    putchar('\n');

    /* vytvoreni objektu, do nejz se uklada stav interpretu */
    lua_State *L = lua_open();

    /* nacteme zakladni knihovnu obsahujici mj. i funkci print() */
    luaopen_base(L);

    /* nacteni externiho skriptu, jeho preklad a nasledne spusteni */
    result = luaL_dofile(L, argv[1]);

    /* odstraneni vsech objektu asociovanych se stavem "Lua" */
    lua_close(L);
    if (result != 0) {
        printf("Error # %d\n", result);
    }

    /* vypocet navratoveho kodu */
    return (result != 0);
}
