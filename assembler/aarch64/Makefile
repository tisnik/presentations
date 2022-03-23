# Makefile for all examples
#
BINARY_FILES=template.s hello_world_1 hello_world_2 aritmetic1 infinite_loop loop1-aarch64-v4 move1 move2 move3 move4 move5 move6 move7 fmov1 fmov2 fmov4 fmov5 fmov6 fmov7

SOURCE_FILES = $(BINARY_FILES:%=%.s)
OBJECT_FILES = $(SOURCE_FILES:%.s=%.o)

all: $(BINARY_FILES)

%: %.s
	as -o $@.o $<
	ld -o $@ $@.o

clean:
	rm -f $(OBJECT_FILES) $(BINARY_FILES)
