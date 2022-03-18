#!/usr/bin/env python

import pyglet


def prepare_scene():
    # priprava seznamu vertexu
    # parametry:
    #     8   - pocet vertexu
    #     v2i - format: vertex se dvema souradnicemi typu 'int'
    #     ()  - n-tice s osmi vertexy (8x2 = 16 hodnot typu 'int')
    #     t2f - format: souradnice v texturovacim prostoru se dvema
    #           souradnicemi typu 'float'
    #     ()  - n-tice s osmi souradnicemi (8x2 = 16 hodnot typu 'float')
    #     n3f - format: normalovy vektor se slozkami typu 'float'
    #     ()  - n-tice s osmi barvami (8x3 = 24 hodnot typu 'float')
    #     c3b - format: barva se tremi slozkami typu 'byte'
    #     ()  - n-tice s osmi barvami (8x3 = 24 hodnot typu 'byte')
    return pyglet.graphics.vertex_list(
        8,
        (
            "v2i",
            (
                -50,
                -50,
                -50,
                +50,
                +50,
                +50,
                +50,
                -50,
                +20,
                +20,
                -20,
                -20,
                -20,
                +20,
                +20,
                -20,
            ),
        ),
        (
            "t2f",
            (
                0.0,
                0.0,
                1.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                0.0,
                0.0,
                1.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
            ),
        ),
        (
            "n3f",
            (
                0.0,
                0.0,
                1.0,
                1.0,
                0.0,
                0.0,
                0.0,
                1.0,
                0.0,
                1.0,
                1.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                0.0,
                0.0,
                0.0,
                1.0,
                0.0,
                1.0,
                1.0,
                0.0,
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
print_array("Tex.cords:", vertex_list.tex_coords)
print_array("Normals:", vertex_list.normals)
