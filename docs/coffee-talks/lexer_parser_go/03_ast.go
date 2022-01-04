package main

import (
	"fmt"
	"log"
	"strings"

	"go/ast"
	"go/parser"
	"go/token"
)

// zdrojový kód, který se má naparsovat
const source = `
package main

var answer int = 42
`

// nový datový typ implementující rozhraní ast.Visitor
type visitor int

// implementace (jediné) funkce předepsané v rozhraní ast.Visitor
func (v visitor) Visit(n ast.Node) ast.Visitor {
	// dosáhli jsme koncového uzlu?
	if n == nil {

		// tisk pozice a typu uzlu
		fmt.Printf("%3d\t", v)
		fmt.Printf("%s%T\n", strings.Repeat("\t", int(v)), n)
		return nil
	}

	// tisk pozice a typu uzlu
	fmt.Printf("%3d\t", v)
	fmt.Printf("%s%T\n", strings.Repeat("\t", int(v)), n)
	return v + 1
}

func main() {
	// struktura reprezentující množinu zdrojových kódů
	fileSet := token.NewFileSet()

	// konstrukce parseru a parsing zdrojového kódu
	f, err := parser.ParseFile(fileSet, "", source, parser.AllErrors)
	if err != nil {
		log.Fatal(err)
	}

	var v visitor

	// zahájení průchodu abstraktním syntaktickým stromem
	ast.Walk(v, f)
}
