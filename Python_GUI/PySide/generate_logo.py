#!/usr/bin/env python

from math import sin, cos


def main():
    size = 480
    with open("logo.svg", "w") as fout:
        fout.write("<?xml version='1.0' encoding='UTF-8'?>")
        fout.write(
            "<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='{w}' height='{h}'>\n".format(
                w=size, h=size
            )
        )
        green = 255
        for i, r, red, blue in zip(
            range(0, 128), range(128, 0, -1), range(255, 0, -2), range(0, 256, 2)
        ):
            a = i / 12.0
            b = i + 80.0
            x = size / 2 + b * cos(a)
            y = size / 2 + b * sin(a)
            p = "<circle cx='{x}' cy='{y}' r='{r}' ".format(x=x, y=y, r=r)
            q = "fill='rgb({r}, {g}, {b})' style='fill-opacity:.06'/>\n".format(
                r=red, g=green, b=blue
            )
            r = "fill='none' stroke='black'/>\n"
            fout.write(p + q)
            fout.write(p + r)

        fout.write("</svg>\n")


if __name__ == "__main__":
    main()
