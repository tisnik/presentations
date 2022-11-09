package main

import "math"
import "github.com/Konstantin8105/c4go/noarch"
import "fmt"

type fx int32

// atans - transpiled function from  /root/fx.c:33
// hlavičky použitých funkcí
// tabulka arkustangentu úhlů
var atans []fx = make([]fx, 16)

// pows - transpiled function from  /root/fx.c:36
// tabulka záporných celočíselných mocnin hodnoty 2
var pows []fx = make([]fx, 16)

// fx_print - transpiled function from  /root/fx.c:42
func fx_print(x fx) {
	//
	// * Tisk numerické hodnoty uložené ve formátu pevné
	// * řádové binární čárky (FX)
	//
	var i int32
	// pomocná proměnná pro převod do dvojkové soustavy
	var val uint32 = uint32((x))
	fmt.Printf("bin: ")
	{
		// převod na řetězec bitů (do dvojkové soustavy)
		for i = 0; i < 16+16; i++ {
			// výpis hodnoty aktuálně nejvyššího bitu
			bit := val & (1 << (16 + 16 - 1))
			noarch.Putchar(noarch.BoolToInt(!noarch.Not(bit)) + int32('0'))
			if i == 16-1 {
				// po řádové binární čárce vypsat značku
				noarch.Putchar(int32('.'))
			}
			// posun na další (méně významný) bit
			val = val << uint64(1)
		}
	}
	noarch.Printf([]byte("   hex: %08x   fp: %+11.5f\n\x00"), x, fx2fp(x))
}

// fp2fx - transpiled function from  /root/fx.c:61
func fp2fx(x float64) fx {
	//
	// * Převod z formátu plovoucí řádové binární čárky (FP)
	// * do formátu pevné řádové binární čárky (FX)
	//
	return fx(x * float64(2<<uint64(16-1)))
}

// int2fx - transpiled function from  /root/fx.c:70
func int2fx(x int32) fx {
	//
	// * Převod z celočíselného formátu (integer)
	// * do formátu pevné řádové binární čárky (FX)
	//
	return fx(x << uint64(16))
}

// fx2fp - transpiled function from  /root/fx.c:79
func fx2fp(x fx) float64 {
	//
	// * Převod z formátu pevné řádové binární čárky (FX)
	// * do formátu plovoucí řádové binární čárky (FP)
	//
	return float64(int32((x))) / float64(2<<uint64(16-1))
}

// fx_add - transpiled function from  /root/fx.c:88
func fx_add(x fx, y fx) fx {
	//
	// * Součet dvou hodnot uložených ve shodném formátu
	// * pevné binární řádové čárky (FX)
	//
	return x + y
}

// fx_sub - transpiled function from  /root/fx.c:97
func fx_sub(x fx, y fx) fx {
	//
	// * Rozdíl dvou hodnot uložených ve shodném formátu
	// * pevné binární řádové čárky (FX)
	//
	return x - y
}

// fx_mul - transpiled function from  /root/fx.c:106
func fx_mul(x fx, y fx) fx {
	//
	// * Součin dvou hodnot uložených ve shodném formátu
	// * pevné binární řádové čárky (FX)
	//
	var result fx = x >> uint64(16/2) * (y >> uint64(16/2))
	return result
}

// fx_div - transpiled function from  /root/fx.c:116
func fx_div(x fx, y fx) fx {
	//
	// * Podíl dvou hodnot uložených ve shodném formátu
	// * pevné binární řádové čárky (FX)
	//
	var result fx = x / (y >> uint64(16/2))
	return result << uint64(16/2)
}

// fx_create_tables - transpiled function from  /root/fx.c:126
func fx_create_tables() {
	//
	// * Vytvoření tabulky pro výpočet goniometrických
	// * funkcí pomocí algoritmu CORDIC
	//
	var i int32
	for i = 0; i < 16; i++ {
		var p float64 = math.Pow(2, float64(-i))
		atans[i] = fp2fx(math.Atan(p))
		pows[i] = fp2fx(p)
	}
}

// fx_tan_cordic - transpiled function from  /root/fx.c:138
func fx_tan_cordic(delta fx) (c4goDefaultReturn fx) {
	// výpočet funkce tan() pro zadaný úhel delta
	// (neoptimalizovaná verze)
	var i int32
	// nastavení počátečních podmínek
	var x0 fx = fp2fx(1)
	var y0 fx
	var xn fx
	if delta == fx((0)) {
		// ošetření nulového úhlu
		return fx((0))
	}
	{
		// iterační smyčka
		for i = 0; i < 16; i++ {
			if delta < fx((0)) {
				// úhel je záporný =&gt; rotace doleva
				xn = fx_add(x0, fx_mul(y0, pows[i]))
				y0 = fx_sub(y0, fx_mul(x0, pows[i]))
				delta = fx_add(delta, atans[i])
			} else {
				// úhel je kladný =&gt; rotace doprava
				xn = fx_sub(x0, fx_mul(y0, pows[i]))
				y0 = fx_add(y0, fx_mul(x0, pows[i]))
				delta = fx_sub(delta, atans[i])
			}
			x0 = xn
		}
	}
	if x0 == fx((0)) {
		if y0 < fx((0)) {
			//        printf("%i\t%+f\t%+f\t%+f\n", i, fx2fp(x0), fx2fp(y0), fx2fp(delta));
			// ošetření tangenty pravého úhlu
			return fx((0))
		} else {
			return fx((0))
		}
	} else {
		// vrátit výsledek operace
		return fx_div(y0, x0)
	}
	return
}

// fx_tan_cordic_optim - transpiled function from  /root/fx.c:171
func fx_tan_cordic_optim(delta fx) (c4goDefaultReturn fx) {
	// výpočet funkce tan() pro zadaný úhel delta
	// (optimalizovaná verze)
	var i int32
	// nastavení počátečních podmínek
	var x0 fx = int2fx(1)
	var y0 fx = fx((0))
	var xn fx
	if delta == fx((0)) {
		// ošetření nulového úhlu
		return fx((0))
	}
	{
		// iterační smyčka
		for i = 0; i < 16; i++ {
			if delta < fx((0)) {
				// úhel je záporný =&gt; rotace doleva
				// místo násobení bitový posuv
				xn = fx_add(x0, y0>>uint64(i))
				y0 = fx_sub(y0, x0>>uint64(i))
				delta = fx_add(delta, atans[i])
			} else {
				// úhel je kladný =&gt; rotace doprava
				xn = fx_sub(x0, y0>>uint64(i))
				y0 = fx_add(y0, x0>>uint64(i))
				delta = fx_sub(delta, atans[i])
			}
			x0 = xn
		}
	}
	if x0 == fx((0)) {
		if y0 < fx((0)) {
			// ošetření tangenty pravého úhlu
			return fx((0))
		} else {
			return fx((0))
		}
	} else {
		// vrátit výsledek operace
		return fx_div(y0, x0)
	}
	return
}

// fx_sin_cordic_optim - transpiled function from  /root/fx.c:202
func fx_sin_cordic_optim(delta fx) fx {
	// výpočet funkce sin() pro zadaný úhel delta
	var i int32
	var K_fx fx = fx(math.Round(0.6073 * float64(2<<uint64(16-1))))
	// nastavení počátečních podmínek
	var x0 fx = int2fx(1)
	var y0 fx = fx((0))
	var xn fx
	{
		// iterační smyčka
		for i = 0; i < 16; i++ {
			if delta < fx((0)) {
				// úhel je záporný =&gt; rotace doleva
				// místo násobení bitový posuv
				xn = fx_add(x0, y0>>uint64(i))
				y0 = fx_sub(y0, x0>>uint64(i))
				delta = fx_add(delta, atans[i])
			} else {
				// úhel je kladný =&gt; rotace doprava
				xn = fx_sub(x0, y0>>uint64(i))
				y0 = fx_add(y0, x0>>uint64(i))
				delta = fx_sub(delta, atans[i])
			}
			x0 = xn
		}
	}
	// opravit "zesílení" výsledku
	return fx_mul(y0, K_fx)
}

// fx_cos_cordic_optim - transpiled function from  /root/fx.c:226
func fx_cos_cordic_optim(delta fx) fx {
	// výpočet funkce cos() pro zadaný úhel delta
	var i int32
	var K_fx fx = fx(math.Round(0.6073 * float64(2<<uint64(16-1))))
	// nastavení počátečních podmínek
	var x0 fx = int2fx(1)
	var y0 fx = fx((0))
	var xn fx
	{
		// iterační smyčka
		for i = 0; i < 16; i++ {
			if delta < fx((0)) {
				// úhel je záporný =&gt; rotace doleva
				// místo násobení bitový posuv
				xn = fx_add(x0, y0>>uint64(i))
				y0 = fx_sub(y0, x0>>uint64(i))
				delta = fx_add(delta, atans[i])
			} else {
				// úhel je kladný =&gt; rotace doprava
				xn = fx_sub(x0, y0>>uint64(i))
				y0 = fx_add(y0, x0>>uint64(i))
				delta = fx_sub(delta, atans[i])
			}
			x0 = xn
		}
	}
	// opravit "zesílení" výsledku
	return fx_mul(x0, K_fx)
}

// fx_sin_cordic_optim_iter - transpiled function from  /root/fx.c:250
func fx_sin_cordic_optim_iter(delta fx, iter int32) fx {
	// výpočet funkce sin() pro zadaný úhel delta
	var i int32
	var K_fx fx = fx(math.Round(0.6073 * float64(2<<uint64(16-1))))
	// nastavení počátečních podmínek
	var x0 fx = int2fx(1)
	var y0 fx = fx((0))
	var xn fx
	{
		// iterační smyčka
		for i = 0; i < iter; i++ {
			if delta < fx((0)) {
				// úhel je záporný =&gt; rotace doleva
				// místo násobení bitový posuv
				xn = fx_add(x0, y0>>uint64(i))
				y0 = fx_sub(y0, x0>>uint64(i))
				delta = fx_add(delta, atans[i])
			} else {
				// úhel je kladný =&gt; rotace doprava
				xn = fx_sub(x0, y0>>uint64(i))
				y0 = fx_add(y0, x0>>uint64(i))
				delta = fx_sub(delta, atans[i])
			}
			x0 = xn
		}
	}
	// opravit "zesílení" výsledku
	return fx_mul(y0, K_fx)
}

// fx_cos_cordic_optim_iter - transpiled function from  /root/fx.c:274
func fx_cos_cordic_optim_iter(delta fx, iter int32) fx {
	// výpočet funkce cos() pro zadaný úhel delta
	var i int32
	var K_fx fx = fx(math.Round(0.6073 * float64(2<<uint64(16-1))))
	// nastavení počátečních podmínek
	var x0 fx = int2fx(1)
	var y0 fx = fx((0))
	var xn fx
	{
		// iterační smyčka
		for i = 0; i < iter; i++ {
			if delta < fx((0)) {
				// úhel je záporný =&gt; rotace doleva
				// místo násobení bitový posuv
				xn = fx_add(x0, y0>>uint64(i))
				y0 = fx_sub(y0, x0>>uint64(i))
				delta = fx_add(delta, atans[i])
			} else {
				// úhel je kladný =&gt; rotace doprava
				xn = fx_sub(x0, y0>>uint64(i))
				y0 = fx_add(y0, x0>>uint64(i))
				delta = fx_sub(delta, atans[i])
			}
			x0 = xn
		}
	}
	// opravit "zesílení" výsledku
	return fx_mul(x0, K_fx)
}

// main - transpiled function from  /root/fx.c:297
func main() {
	defer noarch.AtexitRun()
	var i int32
	var cosfx fx
	// úhel, ze kterého se funkce počítá
	var delta float64
	// vypočtené hodnoty
	var value float64
	// absolutní chyby
	var abs_err float64
	// relativní chyby
	var rel_err float64
	// ukazatele na konstantní řetězce pro
	var zvyr1 []byte
	var zvyr2 []byte
	// generování HTML
	fx_create_tables()
	noarch.Puts([]byte("\n<h2>Výpočet funkce cos() optimalizovanou metodou CORDIC</h2>\n\x00"))
	noarch.Puts([]byte("<table>\x00"))
	fmt.Printf("<tr><th>Úhel</th><th>cos FP</th><th>cos FX</th><th>Abs.chyba</th><th>Rel.chyba</th></tr>\n")
	{
		// výpočetní smyčka
		for i = 0; i <= 90; i++ {
			// převod úhlu na radiány
			delta = float64(i) / 180 * 3.141592653589793
			// aplikace algoritmu CORDIC
			cosfx = fx_cos_cordic_optim(fp2fx(delta))
			// výpočet funkce cos
			value = fx2fp(cosfx)
			// výpočet absolutních chyb
			abs_err = math.Abs(value - math.Cos(delta))
			if math.Cos(delta) <= 1e-10 {
				rel_err = 0
			} else {
				rel_err = 100 * abs_err / math.Cos(delta)
			}
			if rel_err <= 1 {
				zvyr1 = []byte("<strong>\x00")
				zvyr2 = []byte("</strong>\x00")
			} else {
				zvyr1 = []byte("\x00")
				zvyr2 = []byte("\x00")
			}
			noarch.Printf([]byte("<tr><td>%02d</td><td>%5.3f</td><td>%5.3f%%</td><td>%5.3f</td><td>%s%5.3f%%%s</td></tr>\n\x00"), i, value, math.Cos(delta), abs_err, zvyr1, rel_err, zvyr2)
		}
	}
	noarch.Puts([]byte("</table>\x00"))
	return
}

// finito
