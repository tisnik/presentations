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

func main() {
    var x = 10
    var y = 20

    if x > 0 {
    }

    if x != y {
    }

    if 0 < x {
    }

    if 0 > 1 {
    }
}
`

const (
	nodeTypeLiteral = iota
	nodeTypeIdentifier
	nodeTypeArray
	nodeTypeUnknown
)

func getValueAndType(n ast.Expr) (string, int) {
	switch v := n.(type) {
	case *ast.BasicLit:
		return v.Value, nodeTypeLiteral
	case *ast.Ident:
		return v.Name, nodeTypeIdentifier
	case *ast.ArrayType:
		if v.Len == nil {
			return fmt.Sprintf("Slice of %s\n", v.Elt), nodeTypeArray
		} else {
			return fmt.Sprintf("Array of %s\n", v.Elt), nodeTypeArray
		}
	default:
		return fmt.Sprintf("Unrecognized type %T\n", v), nodeTypeUnknown
	}
}

// funkce volaná při průchodu AST
func inspectCallback(n ast.Node) bool {
	// pokud se jedná o volání funkce, vrátí se hodnota + true
	ifStatement, found := n.(*ast.IfStmt)
	if found {
		fmt.Print("if statement")
		condition := ifStatement.Cond
		binaryExpr, found := condition.(*ast.BinaryExpr)
		if found {
			fmt.Print(" with binary condition")
			leftValue, leftType := getValueAndType(binaryExpr.X)
			rightValue, rightType := getValueAndType(binaryExpr.Y)
			operand := binaryExpr.Op
			fmt.Printf(" %s %s %s", leftValue, operand, rightValue)
			if leftType == nodeTypeLiteral && rightType == nodeTypeIdentifier {
				fmt.Print(" (Yoda style condition detected)")
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
