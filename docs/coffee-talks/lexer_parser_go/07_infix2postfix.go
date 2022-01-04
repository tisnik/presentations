package main

import (
	"fmt"

	"go/scanner"
	"go/token"
)

// výraz, který se má převést na RPN
const source = `
1 + 2 * (3 + x) + y * (z - 1)
`

func toRPN(s scanner.Scanner) {
	var operators = map[token.Token]int{
		token.MUL: 2,
		token.QUO: 2,
		token.REM: 2,
		token.ADD: 1,
		token.SUB: 1,
	}

	var stack []token.Token

	// postupné provádění tokenizace a zpracování jednotlivých tokenů
loop:
	for {
		_, tok, lit := s.Scan()
		switch tok {
		case token.INT:
			// celé číslo přímo vypsat
			fallthrough
		case token.FLOAT:
			// číslo s plovoucí čárkou přímo vypsat
			fallthrough
		case token.IDENT:
			// identifikátor taktéž přímo vypsat
			fmt.Printf("%v ", lit)
		case token.LPAREN:
			// levá závorka se uloží na zásobník (bez výpisu)
			stack = append(stack, tok)
		case token.RPAREN:
			// pravá závorka zahájí zpracování zásobníku až do první nalezené levé závorky
			var tok token.Token
			for {
				// přečtení prvku ze zásobníku - operace POP
				tok, stack = stack[len(stack)-1], stack[:len(stack)-1]
				if tok == token.LPAREN {
					// odstranění levé závorky
					break
				}
				// ostatní tokeny získané ze zásobníku se vypíšou
				fmt.Printf("%v ", tok)
			}
		case token.EOF:
			// speciální token reprezentující konec tokenizace
			break loop
		default:
			priority1, isOperator := operators[tok]
			if isOperator {
				// průchod prvky na zásobníku
				for len(stack) > 0 {
					// operace TOP
					tok := stack[len(stack)-1]
					// získat prioritu operátoru přečteného ze zásobníku
					priority2 := operators[tok]

					if priority1 > priority2 {
						// větší priorita nového operátoru -> konec
						// (pouze ho později uložíme na zásobník)
						break
					}

					// menší či stejná priorita nového operátoru ->
					// vypsat předchozí operátor nalezený na zásobníku
					// a odstranit tento operátor ze zásobníku
					stack = stack[:len(stack)-1] // POP
					fmt.Printf("%s ", tok)
				}

				// uložit nově načtený operátor na zásobník
				stack = append(stack, tok)
			}
		}
	}
	// vyprázdnění obsahu zásobníku
	for len(stack) > 0 {
		fmt.Printf("%s ", stack[len(stack)-1])
		stack = stack[:len(stack)-1]
	}
}

func main() {
	// objekt představující scanner
	var s scanner.Scanner

	// struktura reprezentující množinu zdrojových kódů
	fset := token.NewFileSet()

	// přidání informace o zdrojovém kódu
	file := fset.AddFile("", fset.Base(), len(source))

	// inicializace scanneru
	s.Init(file, []byte(source), nil, scanner.ScanComments)

	// převod výrazu do RPN
	toRPN(s)
}
