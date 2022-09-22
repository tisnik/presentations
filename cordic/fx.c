#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/* počet míst před a za binární řádovou tečkou */
#define A 16
#define B 16

/* Ludolfovo číslo */
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

/* maximální počet iterací při běhu algoritmu */
#define MAX_ITER 16

/* "zesílení" při rotacích */
#define K_float 0.6073

/* převody mezi stupni a radiány */
#define rad2deg(rad) ((rad)*180.0/M_PI)
#define deg2rad(deg) ((deg)/180.0*M_PI)

/* datový typ, se kterým budeme pracovat */
typedef signed int fx;

/* hlavičky použitých funkcí */
void fx_print(fx x);
fx fp2fx(double x);
double fx2fp(fx x);

/* tabulka arkustangentu úhlů */
fx atans[MAX_ITER];

/* tabulka záporných celočíselných mocnin hodnoty 2 */
fx pows[MAX_ITER];

/*
 * Tisk numerické hodnoty uložené ve formátu pevné
 * řádové binární čárky (FX)
 */
void fx_print(fx x)
{
    int i;
    int val = x;                /* pomocná proměnná pro převod do dvojkové soustavy */
    printf("bin: ");
    for (i = 0; i < A + B; i++) {       /* převod na řetězec bitů (do dvojkové soustavy) */
        putchar(!!(val & (1 << (A + B - 1))) + '0');    /* výpis hodnoty aktuálně nejvyššího bitu */
        if (i == B - 1)
            putchar('.');       /* po řádové binární čárce vypsat značku */
        val = val << 1;         /* posun na další (méně významný) bit */
    }

    printf("   hex: %08x   fp: %+11.5f\n", x, fx2fp(x));
}

/*
 * Převod z formátu plovoucí řádové binární čárky (FP)
 * do formátu pevné řádové binární čárky (FX)
 */
fx fp2fx(double x)
{
    return (fx) (x * (2 << (B - 1)));
}

/*
 * Převod z celočíselného formátu (integer)
 * do formátu pevné řádové binární čárky (FX)
 */
fx int2fx(int x)
{
    return (fx) (x << B);
}

/*
 * Převod z formátu pevné řádové binární čárky (FX)
 * do formátu plovoucí řádové binární čárky (FP)
 */
double fx2fp(fx x)
{
    return (double) x / (2 << (B - 1));
}

/*
 * Součet dvou hodnot uložených ve shodném formátu
 * pevné binární řádové čárky (FX)
 */
fx fx_add(fx x, fx y)
{
    return x + y;
}

/*
 * Rozdíl dvou hodnot uložených ve shodném formátu
 * pevné binární řádové čárky (FX)
 */
fx fx_sub(fx x, fx y)
{
    return x - y;
}

/*
 * Součin dvou hodnot uložených ve shodném formátu
 * pevné binární řádové čárky (FX)
 */
fx fx_mul(fx x, fx y)
{
    fx result = (x >> (B / 2)) * (y >> (B / 2));
    return result;
}

/*
 * Podíl dvou hodnot uložených ve shodném formátu
 * pevné binární řádové čárky (FX)
 */
fx fx_div(fx x, fx y)
{
    fx result = x / (y >> (B / 2));
    return result << (B / 2);
}

/*
 * Vytvoření tabulky pro výpočet goniometrických
 * funkcí pomocí algoritmu CORDIC
 */
void fx_create_tables(void)
{
    int i;
    for (i = 0; i < MAX_ITER; i++) {
        double p = pow(2.0, -i);
        atans[i] = fp2fx(atan(p));
        pows[i] = fp2fx(p);
    }
}

/* výpočet funkce tan() pro zadaný úhel delta */
/* (neoptimalizovaná verze) */
fx fx_tan_cordic(fx delta)
{
    int i;
    /* nastavení počátečních podmínek */
    fx x0 = fp2fx(1.0);
    fx y0 = fp2fx(0.0);
    fx xn;
    if (delta == 0)
        return 0;               /* ošetření nulového úhlu */
    for (i = 0; i < MAX_ITER; i++) {    /* iterační smyčka */
        if (delta < 0) {        /* úhel je záporný =&gt; rotace doleva */
            xn = fx_add(x0, fx_mul(y0, pows[i]));
            y0 = fx_sub(y0, fx_mul(x0, pows[i]));
            delta = fx_add(delta, atans[i]);
        } else {                /* úhel je kladný =&gt; rotace doprava */
            xn = fx_sub(x0, fx_mul(y0, pows[i]));
            y0 = fx_add(y0, fx_mul(x0, pows[i]));
            delta = fx_sub(delta, atans[i]);
        }
        x0 = xn;
/*        printf("%i\t%+f\t%+f\t%+f\n", i, fx2fp(x0), fx2fp(y0), fx2fp(delta)); */
    }
    if (x0 == 0)                /* ošetření tangenty pravého úhlu */
        if (y0 < 0)
            return 0;
        else
            return 0;
    else
        return fx_div(y0, x0);  /* vrátit výsledek operace */
}

/* výpočet funkce tan() pro zadaný úhel delta */
/* (optimalizovaná verze) */
fx fx_tan_cordic_optim(fx delta)
{
    int i;
    /* nastavení počátečních podmínek */
    fx x0 = int2fx(1);
    fx y0 = 0;
    fx xn;
    if (delta == 0)
        return 0;               /* ošetření nulového úhlu */
    for (i = 0; i < MAX_ITER; i++) {    /* iterační smyčka */
        if (delta < 0) {        /* úhel je záporný =&gt; rotace doleva */
            xn = fx_add(x0, y0 >> i);   /* místo násobení bitový posuv */
            y0 = fx_sub(y0, x0 >> i);
            delta = fx_add(delta, atans[i]);
        } else {                /* úhel je kladný =&gt; rotace doprava */
            xn = fx_sub(x0, y0 >> i);
            y0 = fx_add(y0, x0 >> i);
            delta = fx_sub(delta, atans[i]);
        }
        x0 = xn;
    }
    if (x0 == 0)                /* ošetření tangenty pravého úhlu */
        if (y0 < 0)
            return 0;
        else
            return 0;
    else
        return fx_div(y0, x0);  /* vrátit výsledek operace */
}

/* výpočet funkce sin() pro zadaný úhel delta */
fx fx_sin_cordic_optim(fx delta)
{
    int i;
    static fx K_fx = (fx) (K_float * (2 << (B - 1)));
    /* nastavení počátečních podmínek */
    fx x0 = int2fx(1);
    fx y0 = 0;
    fx xn;
    for (i = 0; i < MAX_ITER; i++) {    /* iterační smyčka */
        if (delta < 0) {        /* úhel je záporný =&gt; rotace doleva */
            xn = fx_add(x0, y0 >> i);   /* místo násobení bitový posuv */
            y0 = fx_sub(y0, x0 >> i);
            delta = fx_add(delta, atans[i]);
        } else {                /* úhel je kladný =&gt; rotace doprava */
            xn = fx_sub(x0, y0 >> i);
            y0 = fx_add(y0, x0 >> i);
            delta = fx_sub(delta, atans[i]);
        }
        x0 = xn;
    }
    return fx_mul(y0, K_fx);    /* opravit "zesílení" výsledku */
}

/* výpočet funkce cos() pro zadaný úhel delta */
fx fx_cos_cordic_optim(fx delta)
{
    int i;
    static fx K_fx = (fx) (K_float * (2 << (B - 1)));
    /* nastavení počátečních podmínek */
    fx x0 = int2fx(1);
    fx y0 = 0;
    fx xn;
    for (i = 0; i < MAX_ITER; i++) {    /* iterační smyčka */
        if (delta < 0) {        /* úhel je záporný =&gt; rotace doleva */
            xn = fx_add(x0, y0 >> i);   /* místo násobení bitový posuv */
            y0 = fx_sub(y0, x0 >> i);
            delta = fx_add(delta, atans[i]);
        } else {                /* úhel je kladný =&gt; rotace doprava */
            xn = fx_sub(x0, y0 >> i);
            y0 = fx_add(y0, x0 >> i);
            delta = fx_sub(delta, atans[i]);
        }
        x0 = xn;
    }
    return fx_mul(x0, K_fx);    /* opravit "zesílení" výsledku */
}

/* výpočet funkce sin() pro zadaný úhel delta */
fx fx_sin_cordic_optim_iter(fx delta, int iter)
{
    int i;
    static fx K_fx = (fx) (K_float * (2 << (B - 1)));
    /* nastavení počátečních podmínek */
    fx x0 = int2fx(1);
    fx y0 = 0;
    fx xn;
    for (i = 0; i < iter; i++) {        /* iterační smyčka */
        if (delta < 0) {        /* úhel je záporný =&gt; rotace doleva */
            xn = fx_add(x0, y0 >> i);   /* místo násobení bitový posuv */
            y0 = fx_sub(y0, x0 >> i);
            delta = fx_add(delta, atans[i]);
        } else {                /* úhel je kladný =&gt; rotace doprava */
            xn = fx_sub(x0, y0 >> i);
            y0 = fx_add(y0, x0 >> i);
            delta = fx_sub(delta, atans[i]);
        }
        x0 = xn;
    }
    return fx_mul(y0, K_fx);    /* opravit "zesílení" výsledku */
}

/* výpočet funkce cos() pro zadaný úhel delta */
fx fx_cos_cordic_optim_iter(fx delta, int iter)
{
    int i;
    static fx K_fx = (fx) (K_float * (2 << (B - 1)));
    /* nastavení počátečních podmínek */
    fx x0 = int2fx(1);
    fx y0 = 0;
    fx xn;
    for (i = 0; i < iter; i++) {        /* iterační smyčka */
        if (delta < 0) {        /* úhel je záporný =&gt; rotace doleva */
            xn = fx_add(x0, y0 >> i);   /* místo násobení bitový posuv */
            y0 = fx_sub(y0, x0 >> i);
            delta = fx_add(delta, atans[i]);
        } else {                /* úhel je kladný =&gt; rotace doprava */
            xn = fx_sub(x0, y0 >> i);
            y0 = fx_add(y0, x0 >> i);
            delta = fx_sub(delta, atans[i]);
        }
        x0 = xn;
    }
    return fx_mul(x0, K_fx);    /* opravit "zesílení" výsledku */
}

int main(void)
{
    int i;
    fx cosfx;
    double delta;               /* úhel, ze kterého se funkce počítá */
    double value;               /* vypočtené hodnoty */
    double abs_err;             /* absolutní chyby */
    double rel_err;             /* relativní chyby */
    char *zvyr1, *zvyr2;        /* ukazatele na konstantní řetězce pro */
    /* generování HTML */

    fx_create_tables();

    puts("\n<h2>Výpočet funkce cos() optimalizovanou metodou CORDIC</h2>\n");
    puts("<table>");
    printf
        ("<tr><th>Úhel</th><th>cos FP</th><th>cos FX</th><th>Abs.chyba</th><th>Rel.chyba</th></tr>\n");
    for (i = 0; i <= 90; i++) { /* výpočetní smyčka */
        delta = deg2rad(i);     /* převod úhlu na radiány */
        cosfx = fx_cos_cordic_optim(fp2fx(delta));      /* aplikace algoritmu CORDIC */
        value = fx2fp(cosfx);   /* výpočet funkce cos */
        abs_err = fabs(value - cos(delta));     /* výpočet absolutních chyb */
        rel_err = cos(delta) <= 1e-10 ? 0 : 100.0 * abs_err / cos(delta);
        if (rel_err <= 1.0) {
            zvyr1 = "<strong>";
            zvyr2 = "</strong>";
        } else {
            zvyr1 = "";
            zvyr2 = "";
        }
        printf
            ("<tr><td>%02d</td><td>%5.3f</td><td>%5.3f%%</td><td>%5.3f</td><td>%s%5.3f%%%s</td></tr>\n",
             i, value, cos(delta), abs_err, zvyr1, rel_err, zvyr2);
    }
    puts("</table>");
    return 0;
}

// finito
