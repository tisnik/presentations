package main

import "unsafe"
import "math"
import "fmt"

// atans - transpiled function from  /root/fp.c:20
// --------------------------------------------------------
// Výpočet hodnot funkcí sin() a cos() pomocí iteračního
// algoritmu CORDIC.
// --------------------------------------------------------
// maximální počet iterací při běhu algoritmu
// "zesílení" při rotacích
// tabulka arkustangentu úhlů
var atans []float64 = make([]float64, 10)

// pows - transpiled function from  /root/fp.c:23
// tabulka záporných celočíselných mocnin hodnoty 2
var pows []float64 = make([]float64, 10)

// createTables - transpiled function from  /root/fp.c:26
func createTables() {
	// naplnění tabulek atans[] a pows[]
	var i int32
	for i = 0; i < 10; i++ {
		var p float64 = math.Pow(2, float64(-i))
		atans[i] = math.Atan(p)
		pows[i] = p
	}
}

// sincos - transpiled function from  /root/fp.c:37
func sincos(delta float64, sinval *float64, cosval *float64) {
	// výpočet funkcí sin() a cos() pro zadaný úhel delta
	var i int32
	// nastavení počátečních podmínek
	var x0 float64 = 1
	var y0 float64
	var xn float64
	{
		// iterační smyčka
		for i = 0; i < 10; i++ {
			if delta < 0 {
				// úhel je záporný => rotace doleva
				xn = x0 + y0*pows[i]
				y0 -= x0 * pows[i]
				delta += atans[i]
			} else {
				// úhel je kladný => rotace doprava
				xn = x0 - y0*pows[i]
				y0 += x0 * pows[i]
				delta -= atans[i]
			}
			x0 = xn
		}
	}
	// opravit "zesílení" výsledku
	*sinval = y0 * 0.6073
	*cosval = x0 * 0.6073
}

// main - transpiled function from  /root/fp.c:59
func main() {
	var i int32
	createTables()
	{
		// výpočetní smyčka
		for i = 0; i <= 90; i++ {
			// úhel, ze kterého se počítá sin a cos
			var delta float64
			// vypočtené hodnoty
			var sinval float64
			var cosval float64
			// absolutní chyby
			var sinerr float64
			var coserr float64
			// převod úhlu na radiány
			delta = float64(i) * 3.141592653589793 / 180
			// výpočet sinu a kosinu
			sincos(delta, &sinval, &cosval)
			// výpočet absolutních chyb
			sinerr = math.Abs(sinval - math.Sin(delta))
			coserr = math.Abs(cosval - math.Cos(delta))
			// tisk výsledků
			fmt.Printf("%02d\t%12.10f\t%12.10f\t%12.10f\t%12.10f\t%8.3f%%\t%8.3f%%\n", i, sinval, cosval, sinerr, coserr, 100*sinerr/sinval, 100*coserr/cosval)
		}
	}
	return
}

// c4goUnsafeConvert_float64 : created by c4go
func c4goUnsafeConvert_float64(c4go_name *float64) []float64 {
	return (*[1000000]float64)(unsafe.Pointer(c4go_name))[:]
}

// finito
