"""Jednoduchý L-systém: C-křivka."""

#
# Použito v článku:
#
# Patologické křivky a jiná matematická monstra
# https://www.root.cz/clanky/patologicke-krivky-a-jina-matematicka-monstra/
#
# Součást seriálu:
#
# Křivky nejen v počítačové grafice
# https://www.root.cz/serialy/krivky-nejen-v-pocitacove-grafice/
#

from turtle import *

# krok želvy pro příkazy "F" a "B"
step = 10

# úhel otočení želvy pro příkazy "+" a "-"
angle = 45

# startovní symbol
axiom = "F"

# přepisovací pravidla
rewrite_rules = {}
rewrite_rules["F"] = "+F--F+"

# počet aplikací přepisovacích pravidel
iterations = 8

# počáteční pozice želvy
start_x = -100
start_y = 0


def apply_rule(rules, c):
    """Aplikace přepisovacího pravidla."""
    output = ""
    for rule, result in rules.items():
        if c == rule:
            return result
        else:
            output = c
    return output


def produce_control_string(axiom, rewrite_rules, n):
    """Výpočet řídicího řetězce."""
    s = axiom
    for i in range(n):
        tmp = ""
        for c in s:
            tmp += apply_rule(rewrite_rules, c)
        s = tmp
    return s


def draw_l_system(control_string, step, angle, start_x, start_y):
    """Vykreslení L-systému na obrazovku s využitím želví grafiky."""
    # styl vykreslování
    color("red")
    pensize(2)
    penup()
    setpos(start_x, start_y)
    pendown()

    # projít všemi příkazy z řídicího řetězce
    for command in control_string:
        if command == "F":
            forward(step)
        elif command == "B":
            backward(step)
        elif command == "+":
            left(angle)
        elif command == "-":
            right(angle)

    # dokončení vykreslení a čekání na zavření okna
    done()


# výpočet řídicího řetězce
control_string = produce_control_string(axiom, rewrite_rules, iterations)
print(control_string)

# vykreslení L-systému
speed(0)
hideturtle()
draw_l_system(control_string, step, angle, start_x, start_y)
