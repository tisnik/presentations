# Lexers and parsers in Go

## Lexers in Go

* Perform lexical analysis
* Lexer transforms an input text to sequence of tokens
* Lexer as standard Go package
   - `go/scanner`
   - `go/token`


### Usage of standard lexer

```go
package main

import (
	"fmt"
	"go/scanner"
	"go/token"
)

const source = `
var x int = 1    + 2 * 3
`

func main() {
	var s scanner.Scanner

	fset := token.NewFileSet()
	file := fset.AddFile("", fset.Base(), len(source))

	s.Init(file, []byte(source), nil, scanner.ScanComments)

	for {
		pos, tok, lit := s.Scan()
		if tok == token.EOF {
			fmt.Println("<EOF>")
			break
		}
		fmt.Printf("%s\t%s\t%q\n", fset.Position(pos), tok, lit)
	}

}
```

### Lexer for source with unsupported operator

```go
package main

import (
	"fmt"
	"go/scanner"
	"go/token"
)

const source = `
var x int = 2 < 3 ? 10 : 20
`

func main() {
	var s scanner.Scanner

	fset := token.NewFileSet()
	file := fset.AddFile("", fset.Base(), len(source))

	s.Init(file, []byte(source), nil, scanner.ScanComments)

	for {
		pos, tok, lit := s.Scan()
		if tok == token.EOF {
			fmt.Println("<EOF>")
			break
		}
		fmt.Printf("%s\t%s\t%q\n", fset.Position(pos), tok, lit)
	}

}
```

## Parser

* Perform syntactic analysis
* Builds Abstract Syntax Tree (AST) from sequence of tokens
* It is possible to traverse AST
    - depth-first algorithm
    - (visitor pattern)


### Visiting all nodes in AST

```go
package main

import (
	"fmt"
	"log"
	"strings"

	"go/ast"
	"go/parser"
	"go/token"
)

const source = `
package main

var answer int = 42
`

type visitor int

func (v visitor) Visit(n ast.Node) ast.Visitor {
	if n == nil {
		fmt.Printf("%3d\t", v)
		fmt.Printf("%s%T\n", strings.Repeat("\t", int(v)), n)
		return nil
	}

	fmt.Printf("%3d\t", v)
	fmt.Printf("%s%T\n", strings.Repeat("\t", int(v)), n)
	return v + 1
}

func main() {
	fileSet := token.NewFileSet()

	f, err := parser.ParseFile(fileSet, "", source, parser.AllErrors)
	if err != nil {
		log.Fatal(err)
	}

	var v visitor
	ast.Walk(v, f)
}
```

### Tree of an expression

```go
package main

import (
	"fmt"
	"log"
	"strings"

	"go/ast"
	"go/parser"
)

const source = `
1 + 2 * 3 + x + y * z - 1
`

type visitor int

func (v visitor) Visit(n ast.Node) ast.Visitor {
	if n == nil {
		return nil
	}

	fmt.Printf("%3d\t", v)
	var s string

	switch x := n.(type) {
	case *ast.BasicLit:
		s = x.Value
	case *ast.Ident:
		s = x.Name
	case *ast.UnaryExpr:
		s = x.Op.String()
	case *ast.BinaryExpr:
		s = x.Op.String()
	}

	indent := strings.Repeat("  ", int(v))
	if s != "" {
		fmt.Printf("%s%s\n", indent, s)
	} else {
		fmt.Printf("%s%T\n", indent, n)
	}
	return v + 1
}

func main() {
	f, err := parser.ParseExpr(source)
	if err != nil {
		log.Fatal(err)
	}

	var v visitor
	ast.Walk(v, f)
}
```

### Yoda condition detection

```go
package main

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
)

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

func inspectCallback(n ast.Node) bool {
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
	fileSet := token.NewFileSet()

	file, err := parser.ParseFile(fileSet, "", source, parser.ParseComments)
	if err != nil {
		panic(err)
	}

	ast.Inspect(file, inspectCallback)
}
```

### Function calls detector

```go
package main

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
)

const source = `
package main

var answer int = 42
var x []int = make([]int, 10)
var y = len(x)
var z = cap(x)
var w = len(x) + cap(x)
var a = append(x, 10)
`

func inspectCallback(n ast.Node) bool {
	funcCall, ok := n.(*ast.CallExpr)
	if ok {
		fmt.Printf("Function: %s ", funcCall.Fun)
		fmt.Printf("with %d arguments:\n", len(funcCall.Args))

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
	fileSet := token.NewFileSet()

	file, err := parser.ParseFile(fileSet, "", source, parser.ParseComments)
	if err != nil {
		panic(err)
	}

	ast.Inspect(file, inspectCallback)
}
```

### Infix->postfix notation transformer

* Based on shutting-yard algorithm

```go
package main

import (
	"fmt"

	"go/scanner"
	"go/token"
)

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

loop:
	for {
		_, tok, lit := s.Scan()
		switch tok {
		case token.INT:
			fallthrough
		case token.FLOAT:
			fallthrough
		case token.IDENT:
			fmt.Printf("%v ", lit)
		case token.LPAREN:
			stack = append(stack, tok)
		case token.RPAREN:
			var tok token.Token
			for {
				tok, stack = stack[len(stack)-1], stack[:len(stack)-1]
				if tok == token.LPAREN {
					break
				}
				fmt.Printf("%v ", tok)
			}
		case token.EOF:
			break loop
		default:
			priority1, isOperator := operators[tok]
			if isOperator {
				for len(stack) > 0 {
					tok := stack[len(stack)-1]
					priority2 := operators[tok]

					if priority1 > priority2 {
						break
					}

					stack = stack[:len(stack)-1] // POP
					fmt.Printf("%s ", tok)
				}

				stack = append(stack, tok)
			}
		}
	}
	for len(stack) > 0 {
		fmt.Printf("%s ", stack[len(stack)-1])
		stack = stack[:len(stack)-1]
	}
}

func main() {
	var s scanner.Scanner

	fset := token.NewFileSet()

	file := fset.AddFile("", fset.Base(), len(source))

	s.Init(file, []byte(source), nil, scanner.ScanComments)

	toRPN(s)
}
```

### RPN calculator

```go
package main

import (
	"fmt"
	"strconv"
	"strings"
)

// original:
// 1 + 2 * (3 + 4) + 5 * (6 - 7)

// converted:
const expr = "1 2 3 4 + * + 5 6 7 - * +"

type Stack struct {
	stack []int
}

func (stack *Stack) Push(value int) {
	stack.stack = append(stack.stack, value)
}

func (stack *Stack) Pop() (int, error) {
	if stack.Empty() {
		return -1, fmt.Errorf("Empty stack")
	}

	tos := len(stack.stack) - 1

	element := stack.stack[tos]

	stack.stack = stack.stack[:tos]
	return element, nil
}

func (stack *Stack) Empty() bool {
	return len(stack.stack) == 0
}

type Operator func(int, int) int

func evaluate(expr string) (Stack, error) {
	operators := map[string]Operator{
		"+": func(x int, y int) int { return x + y },
		"-": func(x int, y int) int { return x - y },
		"*": func(x int, y int) int { return x * y },
		"/": func(x int, y int) int { return x / y },
	}

	parts := strings.Fields(expr)

	var stack Stack

	for _, part := range parts {
		operator, isOperator := operators[part]
		if isOperator {
			err := performArithmeticOperation(&stack, operator)
			if err != nil {
				return stack, err
			}
		} else {
			val, err := strconv.Atoi(part)
			if err != nil {
				return stack, fmt.Errorf("Incorrect input: %s", part)
			} else {
				stack.Push(val)
			}
		}
	}

	return stack, nil
}

func performArithmeticOperation(stack *Stack, operator Operator) error {
	y, err := stack.Pop()
	if err != nil {
		return err
	}

	x, err := stack.Pop()
	if err != nil {
		return err
	}

	result := operator(x, y)

	stack.Push(result)

	return nil
}

func printStack(stack Stack) {
	if stack.Empty() {
		fmt.Println("Empty stack!")
		return
	}

	for !stack.Empty() {
		value, _ := stack.Pop()
		fmt.Printf("%d\n", value)
	}
}

func main() {
	stack, err := evaluate(expr)
	if err != nil {
		fmt.Println(err)
		return
	}

	printStack(stack)
}
```
