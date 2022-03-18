#!/usr/bin/env python

import pyglet


def prepare_scene():
    # priprava seznamu vertexu
    # parametry:
    #     8   - pocet vertexu
    #     v2f - format: vertex se dvema souradnicemi typu 'float'
    #     ()  - n-tice s osmi vertexy (8x2 = 16 hodnot typu 'float')
    #     c3b - format: barva se tremi slozkami typu 'byte'
    #     ()  - n-tice s osmi barvami (8x3 = 24 hodnot typu 'byte')
    return pyglet.graphics.vertex_list(
        8,
        (
            "v2f",
            (
                -0.5,
                -0.5,
                -0.5,
                +0.5,
                +0.5,
                +0.5,
                +0.5,
                -0.5,
                +0.2,
                +0.2,
                -0.2,
                -0.2,
                -0.2,
                +0.2,
                +0.2,
                -0.2,
            ),
        ),
        (
            "c3B",
            (
                0xFF,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0x00,
                0x00,
                0x00,
                0xFF,
                0x00,
                0xFF,
                0x00,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0x00,
                0xFF,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0xFF,
                0x00,
            ),
        ),
    )


def print_array(name, array):
    print(name)
    print("   type: %s" % type(array))
    print("   length: %d" % len(array))
    print("   content:")
    for element in array:
        print("        %6.1f" % element)


vertex_list = prepare_scene()

print("Vertex list size: %d" % vertex_list.get_size())
print_array("Colors:", vertex_list.colors)
print_array("Vertices:", vertex_list.vertices)
