package main

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
)

// zdrojový kód, který se má naparsovat
const source = `
package main

var answer int = 42
var x []int = make([]int, 10)
var y = len(x)
var z = cap(x)
var w = len(x) + cap(x)
var a = append(x, 10)
`

// funkce volaná při průchodu AST
func inspectCallback(n ast.Node) bool {
	// pokud se jedná o volání funkce, vrátí se hodnota + true
	funcCall, ok := n.(*ast.CallExpr)
	if ok {
		// výpis podrobnějších informací o volané funkci
		fmt.Printf("Function: %s ", funcCall.Fun)
		fmt.Printf("with %d arguments:\n", len(funcCall.Args))
		// výpis informací o argumentech funkce
		for i, arg := range funcCall.Args {
			fmt.Printf("\t%d\t", i+1)
			switch v := arg.(type) {
			case *ast.BasicLit:
				fmt.Printf("Constant: %s\n", v.Value)
			case *ast.Ident:
				fmt.Printf("Variable: '%s'\n", v.Name)
			default:
				fmt.Println("Unrecognized type")
			}
		}
		fmt.Println()
	}
	return true
}

func main() {
	// struktura reprezentující množinu zdrojových kódů
	fileSet := token.NewFileSet()

	// konstrukce parseru a parsing zdrojového kódu
	file, err := parser.ParseFile(fileSet, "", source, parser.ParseComments)
	if err != nil {
		panic(err)
	}

	// zahájení průchodu abstraktním syntaktickým stromem
	ast.Inspect(file, inspectCallback)
}
