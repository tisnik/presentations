package main

import (
	"fmt"
	"strconv"
	"strings"
)

// původní výraz v infixové notaci
// 1 + 2 * (3 + 4) + 5 * (6 - 7)

// výraz převedený do postfixové notace
const expr = "1 2 3 4 + * + 5 6 7 - * +"

// primitivní neoptimalizovaná varianta zásobníku
type Stack struct {
	stack []int
}

// uložení hodnoty na zásobník
func (stack *Stack) Push(value int) {
	stack.stack = append(stack.stack, value)
}

// přečtení hodnoty ze zásobníku s kontrolou, zda není zásobník prázdný
func (stack *Stack) Pop() (int, error) {
	if stack.Empty() {
		return -1, fmt.Errorf("Empty stack")
	}

	// index nejvyššího prvku na zásobníku
	tos := len(stack.stack) - 1

	// přečtení elementru ze zásobníku
	element := stack.stack[tos]

	// odstranění elementu ze zásobníku
	stack.stack = stack.stack[:tos]
	return element, nil
}

// test, zda je zásobník prázdný
func (stack *Stack) Empty() bool {
	return len(stack.stack) == 0
}

// funkce provádějící výpočet na základě použitého operátoru
type Operator func(int, int) int

// vyhodnocení výrazu zapsaného v postfixové notaci
func evaluate(expr string) (Stack, error) {
	// všechny dostupné aritmetické operátory
	operators := map[string]Operator{
		"+": func(x int, y int) int { return x + y },
		"-": func(x int, y int) int { return x - y },
		"*": func(x int, y int) int { return x * y },
		"/": func(x int, y int) int { return x / y },
	}

	// rozdělení původního výrazu na jednotlivé části
	parts := strings.Fields(expr)

	// zásobník operandů (na začátku prázdný)
	var stack Stack

	// postupné zpracování jednotlivých částí původního výrazu
	for _, part := range parts {
		// test, zda se jedná o operátor
		operator, isOperator := operators[part]
		if isOperator {
			// našli jsme operátor
			// -> provést zvolenou operaci
			//    + uložit výsledek na zásobník
			err := performArithmeticOperation(&stack, operator)
			if err != nil {
				return stack, err
			}
		} else {
			// nejedná se o operátor
			// -> zkusíme tedy vstup zpracovat jako číslo
			val, err := strconv.Atoi(part)
			if err != nil {
				// neočekávaný vstup
				return stack, fmt.Errorf("Incorrect input: %s", part)
			} else {
				// našli jsme číselnou hodnotu
				// ta se uloží na zásobník operandů
				stack.Push(val)
			}
		}
	}

	// nyní by měl zásobník operandů obsahovat jedinou hodnotu
	return stack, nil
}

// provedení vybrané aritmetické operace
func performArithmeticOperation(stack *Stack, operator Operator) error {
	// získat druhý operand ze zásobníku
	y, err := stack.Pop()
	if err != nil {
		return err
	}

	// získat první operand ze zásobníku
	x, err := stack.Pop()
	if err != nil {
		return err
	}

	// vlastní provedení operace
	result := operator(x, y)

	// uložení výsledku operace zpět na zásobník
	stack.Push(result)

	return nil
}

// tisk obsahu zásobníku operandů
func printStack(stack Stack) {
	if stack.Empty() {
		fmt.Println("Empty stack!")
		return
	}

	// zásobník není prázdný, proto postupně vytiskneme uložené operandy
	for !stack.Empty() {
		value, _ := stack.Pop()
		fmt.Printf("%d\n", value)
	}
}

func main() {
	// vyhodnocení výrazu zapsaného v postfixové notaci
	stack, err := evaluate(expr)
	if err != nil {
		fmt.Println(err)
		return
	}

	// výpis obsahu zásobníku operandů
	printStack(stack)
}
